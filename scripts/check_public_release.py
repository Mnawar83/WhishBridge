#!/usr/bin/env python3
"""Guardrail for public documentation (not a comprehensive secret scan)."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
banned_dirs = {"src", "tests", "examples", "private", ".private", "node_modules", "seller-materials"}
banned_ext = {".zip", ".sqlite", ".db", ".pem", ".key", ".p12", ".pfx", ".mjs", ".cjs", ".ts", ".tsx"}
secret_patterns = [
    re.compile(r"(?i)(?:whish_secret|stripe_secret_key|github_token)\s*[=:]\s*['\"]?(?:sk_live_|ghp_|github_pat_|[A-Za-z0-9+/]{32,})"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
errors = []
for file in root.rglob("*"):
    if not file.is_file() or ".git" in file.parts:
        continue
    rel = file.relative_to(root)
    if set(rel.parts) & banned_dirs or rel.suffix.lower() in banned_ext:
        errors.append(f"Restricted file: {rel}")
    if rel.name.startswith(".env") and rel.name != ".env.example":
        errors.append(f"Environment file: {rel}")
    if rel.suffix in {".md", ".py", ".yml", ".yaml", ".txt"} or rel.name == ".gitignore":
        body = file.read_text(encoding="utf-8")
        if any(pattern.search(body) for pattern in secret_patterns):
            errors.append(f"Potential secret: {rel}")
if errors:
    print("FAIL: public documentation check")
    print("\n".join(errors))
    sys.exit(1)
print("PASS: documentation-only tree (not a comprehensive secret audit)")

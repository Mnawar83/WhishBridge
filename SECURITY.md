# Security and responsible disclosure

This public repository contains **documentation only**. Never publish API keys, merchant secrets, paid source-code packages, customer data or private production integration files.

## Implementation checklist
- Obtain provider approval for authorized domains and products.
- Keep Whish merchant credentials on the merchant backend only.
- Authenticate each selling site server-to-server.
- Enforce fixed prices, persistent orders and unique idempotency keys.
- Allowlist HTTPS checkout and return destinations.
- Verify Whish status server-side: callbacks and redirects are not proof of payment.
- Authenticate signed server-to-server events with timestamp and replay protection.
- Grant server-side entitlements exactly once, matched to customer/product/order.
- Preserve durable data and review log exposure, backups and error handling.

## Vulnerability reporting
Do not post security vulnerabilities, credentials, paid source code or sensitive traces in public GitHub issues. Contact the seller via the [Payhip product/support channel](https://payhip.com/b/Sfr9b).

This documentation does not promise a response-time SLA.

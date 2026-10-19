# WhishBridge

**Merchant-domain bridging for Whish Pay integrations across approved websites.**

[العربية](README_AR.md) · [Architecture](docs/ARCHITECTURE.md) · [Before you buy](docs/BUYERS_GUIDE.md) · [Security](SECURITY.md)

> **Unofficial developer project.** WhishBridge is not affiliated with, certified by, endorsed by, or supported by Whish Money. This public repository contains **documentation only**, not the paid source code or merchant credentials.

## Why WhishBridge?

Imagine one business operating two websites: the merchant account is registered under the first site's domain, while the second site sells a digital report. The second site's browser must **not** receive Whish API secrets, and a browser redirect must **not** be interpreted as proof that a payment settled. The Whish mobile app may also require the customer to return to the website manually.

WhishBridge documents an approach in which the **approved merchant-domain backend** creates payment sessions and confirms their status, while authorized selling sites receive verified events and control customer access on their own servers.

**Conceptual flow:**

1. Selling-site server authenticates to the approved merchant-domain backend.
2. Merchant backend persists an idempotent order, creates the Whish payment and returns a checkout URL.
3. Browser completes checkout, perhaps in the Whish mobile app.
4. Any browser return goes through an allowlisted route on the merchant domain. **A redirect does not confirm payment.**
5. Merchant backend checks the provider's status, including through periodic reconciliation when the browser never returns.
6. Merchant backend sends a signed event to the selling-site server, which verifies it and grants access once.

See [the technical architecture](docs/ARCHITECTURE.md) for trust boundaries and limitations.

## The paid Developer Kit

The separate commercial **WhishBridge Developer Kit v0.2.1 Beta** provides:

- Node.js source for an authenticated merchant API with per-site access keys.
- Merchant-side product catalog, durable orders, checkout idempotency, and site isolation.
- Controlled return redirects and allowlisted checkout hosts.
- Server-side provider status verification and periodic payment reconciliation.
- Signed site notifications, a runnable receiving-site example, and server-owned entitlements.
- SQLite persistence for a **single persistent-server deployment**.
- English and Arabic setup docs, security notes, and **18 offline automated tests** using a simulated Whish provider.

**This is a developer reference, not a plug-and-play or Whish-certified payment gateway.** It requires an approved Whish merchant account, authorized domains, integration work, and separate provider Sandbox and production validation.

### Buy the source code

[**Get WhishBridge Developer Kit on Payhip →**](https://payhip.com/b/Sfr9b)

Check the current price, offer, license and availability on Payhip. Any promotional coupon is subject to the store's current conditions.

## Real-world origin

The architecture was inspired by a two-site integration: [FreeCVAudit.com](https://freecvaudit.com) (merchant-side integration) and [WhatMajorShouldIChoose.com](https://whatmajorshouldichoose.com) (selling site). The **commercial kit is a generalized, separately developed reference**, not a copy of those sites' private repositories and not a promise that their exact stack is included.

## Supported deployment model and boundaries

| Topic | Current beta |
|---|---|
| Application | Node.js 22+ (24 recommended) |
| Storage | SQLite with **persistent disk**, single always-on host |
| Serverless / Netlify Functions | **Not plug-and-play**; replace persistence adapter with managed transactional storage |
| Browser return from mobile Whish app | **Not guaranteed**; server-side reconciliation helps confirm payment |
| Official Whish approval / merchant credentials | **Not included** |
| Whish Sandbox or live E2E test | **Not demonstrated by offline suite** |
| Multi-merchant payment processing | **Not authorized by this software** |

## Public vs commercial material

| Public GitHub repo | Paid Payhip download |
|---|---|
| Architecture documentation and integration guidance | Implemented Node.js API and payment workflow |
| Security model and technical FAQs | Persistent storage, scheduled reconciliation, signed receiver |
| Suitability checklist | Runnable local tests and setup examples |
| No Whish API credentials or source code | One-project commercial source license |

## Provider and security notice

A bridge does **not** override Whish's terms or permit reusing an account across unapproved domains, independent merchants, or products. Verify the merchant agreement and approved return/callback domains **directly with Whish**. Provider callbacks and browser redirects must never be treated as payment confirmation.

See [Security](SECURITY.md), [FAQ](docs/FAQ.md), [NOTICE](NOTICE.md), and [public documentation terms](LICENSE.md).

**WhishBridge is independent software.** Whish Pay and Whish Money names belong to their respective owners.

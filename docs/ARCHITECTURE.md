# Technical architecture and payment trust boundaries

This document describes the **pattern**, not a deployable implementation. The commercial source code is distributed separately to licensed customers.

## Components

1. **Selling site (backend):** creates its own customer order, owns customer login and product entitlement, then authenticates to the merchant API with a site-specific key. The Whish merchant secret is never copied to this site.
2. **Merchant-domain bridge (backend):** on the provider-authorized merchant domain; owns Whish credentials, immutable price catalog, checkout idempotency, order persistence, provider status checks, return redirects and signed event dispatch.
3. **Whish Pay:** processes payment requests and exposes payment status through the provider's merchant interface.
4. **Return handler:** only chooses a preconfigured allowlisted site/route. Query-string returnUrl values must never become arbitrary destinations.
5. **Selling-site receiver:** validates HMAC signatures and timestamps, matches the preexisting local order/customer, and grants a server-side entitlement exactly once.
6. **Scheduled reconciliation:** checks unresolved orders even when the browser never returns from a mobile-app payment.

## Critical trust distinction

| Signal | Can it unlock content? | Why |
|---|---|---|
| Browser reaches a success route | **No** | Navigation/query strings are not proof of settlement. |
| Whish calls a success callback | **No, not by itself** | Query provider status server-side. |
| Provider-side status confirms payment | **Only through server-side policy** | Match stored order/customer, process once, consider refunds/disputes. |
| Signed payment event reaches selling site | **Only if locally verified** | Validate signature, freshness, replay protection and intended order/product. |

## Mobile app return limitation

Some customers are sent to the Whish mobile app and must return to the selling site manually. Browser return alone is insufficient. The bridge should reconcile unresolved payments from the merchant server and dispatch signed status events to the selling site.

**Not guaranteed:** app-to-browser automatic redirect, independent settlement amount confirmation from status alone, refund/chargeback reconciliation or Whish approval for any particular domain configuration.

## Deployment boundary

The commercial beta uses a single Node.js process with durable SQLite and a periodic worker. A serverless deployment with ephemeral storage cannot safely use that SQLite design unchanged. Add managed transactional storage and appropriate atomic operations and scheduling before horizontal scaling.

## Approved-domain constraint

This pattern assumes explicit provider permission for all relevant websites/products. A technically working redirect does not authorize processing for third-party merchants or circumvent merchant contractual restrictions.

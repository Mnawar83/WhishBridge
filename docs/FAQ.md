# Frequently asked questions

### Is this an official Whish Money plugin?
No. WhishBridge is independent beta developer software, not endorsed or certified by Whish.

### Can one merchant account process payments for unrelated businesses?
WhishBridge does **not** grant such permission. All websites, products and account usage must be authorized by Whish.

### Can I deploy it directly to Netlify Functions?
Not unchanged. The beta uses SQLite and a persistent Node.js server. A serverless deployment requires a managed transactional database and adapted scheduling.

### Does payment unlock automatically on redirect?
No. Browser returns and callbacks are only signals. Server-side provider verification and locally validated entitlements are required.

### What happens when Whish's mobile app does not return to the browser?
The intended design uses scheduled provider-side reconciliation and signed site notifications. The customer might still need to manually return.

### Is a live test or video included?
No video. The kit contains source code, documentation and offline tests with a simulated provider. Provider Sandbox and live validation remain the buyer's responsibility.

### Does the purchase include Whish merchant credentials or approval?
No.

### Is the complete code public?
No. The public GitHub repo is documentation only. [Purchase the commercial developer kit on Payhip](https://payhip.com/b/Sfr9b).

### Can I resell the code?
The commercial download contains the applicable one-project license. Standalone redistribution is not included.


# Playwright Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to Playwright.

---

## 📘 What is Playwright?

Playwright is an open-source end-to-end testing framework developed by Microsoft. It enables reliable testing of web applications across Chromium, Firefox, and WebKit browsers with a single API.

---

## ⚙️ Playwright Setup Guide

1. **Install Node.js**  
   Ensure Node.js 14+ is installed on your machine.

2. **Install Playwright**

```bash
npm install @playwright/test
```

3. **Install Browsers**

```bash
npx playwright install
```

---

## 🔍 Common Playwright Commands

| Action             | Command Example                        |
|--------------------|----------------------------------------|
| Launch Browser     | `const browser = await chromium.launch();` |
| Open New Page      | `const page = await browser.newPage();` |
| Navigate to URL    | `await page.goto('https://example.com');` |
| Click Element      | `await page.click('text=Login');` |
| Fill Input         | `await page.fill('input[name="email"]', 'test@example.com');` |
|--------------------|----------------------------------------|

---

## 🧪 Sample Test Case

```javascript
const { test, expect } = require('@playwright/test');

test('basic test', async ({ page }) => {
  await page.goto('https://example.com');
  const title = await page.title();
  expect(title).toBe('Example Domain');
});
```

---

## ✅ Best Practices

- Use `await page.waitForSelector` for reliable waits.
- Prefer locators based on accessibility (e.g., role and name).
- Structure tests using the Playwright Test runner.
- Run tests in parallel across browsers.

---

## 📚 Advanced Topics

- API Testing with Playwright
- Running Playwright tests in CI/CD pipelines
- Visual Regression Testing
- Playwright with BDD (Cucumber.js)

---

*Last Updated: April 2025*

# Cypress Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to Cypress testing framework.

---

## 📘 What is Cypress?

Cypress is a fast, reliable, and easy-to-use JavaScript-based end-to-end testing framework built for the modern web. It runs in the browser and is known for its developer-friendly interface and fast execution.

---

## ⚙️ Cypress Setup Guide

1. **Install Node.js and npm**  
   Ensure Node.js and npm are installed. Use `node -v` and `npm -v` to check.

2. **Initialize the project**

```bash
npm init -y
npm install cypress --save-dev
```

3. **Open Cypress Test Runner**

```bash
npx cypress open
```

---

## 📁 Cypress Folder Structure

- `cypress/`
  - `e2e/`: End-to-end test files
  - `support/`: Custom commands and configurations
  - `fixtures/`: Test data files

- `cypress.config.js`: Cypress configuration file

---

## 🔍 Writing a Basic Test

```javascript
describe('My First Test', () => {
  it('Visits the app', () => {
    cy.visit('https://example.com');
    cy.contains('Example Domain');
  });
});
```

---

## 🧪 Common Cypress Commands

| Command       | Description                          |
|---------------|--------------------------------------|
| `cy.visit()`  | Opens a webpage                      |
| `cy.get()`    | Gets DOM elements                    |
| `cy.contains()` | Finds elements with matching text |
| `cy.click()`  | Simulates a click event              |
| `cy.type()`   | Types into input fields              |

---

## ✅ Best Practices

- Use `data-testid` for selectors.
- Structure tests clearly with `describe` and `it`.
- Avoid `cy.wait()` unless necessary.
- Use Cypress Dashboard for CI integration.

---

## 📚 Advanced Topics

- API testing using `cy.request()`
- Running tests headlessly with `cypress run`
- Integrating with GitHub Actions or Jenkins
- Visual testing with plugins
- Handling authentication

---

*Last Updated: April 2025*
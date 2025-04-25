# XPath Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to XPath usage in automation testing.

---

## 📘 What is XPath?

XPath (XML Path Language) is a query language for selecting nodes from an XML document.  
In test automation (e.g., Selenium, Appium), XPath is used to locate elements precisely in a webpage or app.

---

## ⚙️ XPath Setup in Selenium Example

```java
WebDriver driver = new ChromeDriver();
driver.get("https://example.com");

WebElement element = driver.findElement(By.xpath("//input[@id='username']"));
element.sendKeys("admin");
```

---

## 🔍 Types of XPath

| Type           | Example | Description |
|----------------|---------|-------------|
| **Absolute**   | `/html/body/div[2]/input` | Full path from the root element. Fragile. |
| **Relative**   | `//input[@id='username']` | Partial path from any matching node. Recommended. |

---

## 🛠️ XPath Functions and Axes

| Function / Axis | Purpose | Example|
|-----------------|---------|---------------------------------------------------------------------|
| `text()`        | Selects by text | `//button[text()='Submit']` |
| `contains()`    | Partial matching | `//input[contains(@id,'user')]` |
| `starts-with()` | Prefix matching | `//div[starts-with(@class,'header')]` |
| `and/or`        | Combine conditions | `//input[@type='text' and @name='email']` |
| `ancestor::`    | Selects ancestor | `//input[@id='user']/ancestor::div` |
| `following-sibling::` | Sibling nodes after | `//label[text()='Email']/following-sibling::input` |
| `preceding-sibling::` | Sibling nodes before | `//input[@id='password']/preceding-sibling::label` |
|-----------------|----------------------------|----------------------------------------------------|


---

## ✅ Best Practices

- Always prefer **Relative XPath**.
- Use unique attributes (e.g., `id`, `name`) wherever possible.
- Avoid brittle XPaths like `/html/body/div[2]/div[1]/input`.
- Combine multiple attributes for better reliability.
- Use **contains()** and **starts-with()** for dynamic elements.

---

## 📚 Advanced Topics

- Dynamic XPath construction in automation frameworks.
- Handling Shadow DOM elements (needs different strategies).
- XPath vs CSS Selector performance and comparison.
- Building XPath for complex tables and nested structures.

---

*Last Updated: April 2025*

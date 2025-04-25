# Selenium Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to Selenium.

---

## 📘 What is Selenium?

Selenium is an open-source framework for automating web applications for testing purposes. It supports multiple browsers and programming languages like Java, Python, C#, and JavaScript.

---

## ⚙️ Selenium Setup Guide

1. **Install Java and Maven**  
   Ensure you have Java JDK 8+ and Apache Maven installed and configured in your system `PATH`.

2. **Add Selenium dependencies to pom.xml**

```xml
<dependencies>
  <dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.12.1</version>
  </dependency>
</dependencies>
```

3. **Create Page Object Model (POM) structure**  
   Organize tests using POM:
   - `pages/`: Contains page classes
   - `tests/`: Contains test classes
   - `utils/`: Utility functions

---

## 🔍 Common Selenium Locators

| Locator Type | Syntax Example                        |
|--------------|----------------------------------------|
| ID           | `driver.findElement(By.id("login"))`   |
| Name         | `driver.findElement(By.name("q"))`     |
| Class Name   | `driver.findElement(By.className("btn"))` |
| XPath        | `driver.findElement(By.xpath("//div"))` |
| CSS Selector | `driver.findElement(By.cssSelector(".btn"))` |

---

## 🧪 Sample Test Case

```java
WebDriver driver = new ChromeDriver();
driver.get("https://example.com");

WebElement searchBox = driver.findElement(By.name("q"));
searchBox.sendKeys("Selenium WebDriver");
searchBox.submit();
```

---

## ✅ Best Practices

- Use **explicit waits** instead of implicit waits.
- Store locators centrally.
- Structure your test suite using **TestNG** or **JUnit**.
- Leverage tools like **ExtentReports** for reporting.

---

## 📚 Advanced Topics

- Selenium Grid for parallel execution
- Integration with CI/CD pipelines
- Using with BDD frameworks like Cucumber
- Handling dynamic elements and Shadow DOM

---

*Last Updated: April 2025*
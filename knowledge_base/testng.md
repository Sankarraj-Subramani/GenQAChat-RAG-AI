
# TestNG Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to TestNG.

---

## 📘 What is TestNG?

TestNG is a testing framework inspired by JUnit and NUnit, designed for testing needs in Java. It supports annotations, parameterized tests, parallel execution, data-driven testing, and more.

---

## ⚙️ TestNG Setup Guide

1. **Add TestNG to `pom.xml`:**

```xml
<dependencies>
  <dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>7.9.0</version>
    <scope>test</scope>
  </dependency>
</dependencies>
```

2. **Create a Sample Test:**

```java
import org.testng.annotations.Test;
import static org.testng.Assert.assertEquals;

public class CalculatorTest {

    @Test
    public void testAddition() {
        int result = 2 + 3;
        assertEquals(result, 5);
    }
}
```

---

## ✅ TestNG Annotations

| Annotation     | Description                          |
|----------------|--------------------------------------|
| `@Test`        | Marks a method as a test method      |
| `@BeforeClass` | Runs once before any method in class |
| `@AfterClass`  | Runs once after all methods in class |
| `@BeforeMethod`| Runs before each test method         |
| `@AfterMethod` | Runs after each test method          |

---

## 🧪 TestNG Features

- Grouping and prioritizing tests
- DataProviders for data-driven tests
- Parallel execution via XML configuration
- Integration with tools like Selenium, Maven, Jenkins

---

## 🔧 testng.xml Example

```xml
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="MySuite">
  <test name="MyTests">
    <classes>
      <class name="com.example.CalculatorTest"/>
    </classes>
  </test>
</suite>
```

---

## 📚 Advanced Topics

- RetryAnalyzer for rerunning failed tests
- Custom Listeners (`ITestListener`)
- Parallel tests with thread count
- Integration with CI/CD pipelines

---

*Last Updated: April 2025*
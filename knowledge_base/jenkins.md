# Jenkins Knowledge Base

This document is part of the `GenQAChat` RAG project and contains curated QA content related to Jenkins.

---

## 📘 What is Jenkins?

Jenkins is an open-source automation server widely used for Continuous Integration (CI) and Continuous Deployment (CD). It helps automate building, testing, and deploying software.

---

## ⚙️ Jenkins Setup Guide

1. **Install Java**  
   Jenkins requires Java JDK 8 or 11.

2. **Download Jenkins**  
   Download from the [official Jenkins site](https://www.jenkins.io/download/).

3. **Start Jenkins**  
   Use the command:
   ```bash
   java -jar jenkins.war
   ```
   Then access Jenkins at `http://localhost:8080`

4. **Install Plugins**  
   Install essential plugins like Git, Maven Integration, Pipeline, Docker, etc.

---

## 🔍 Key Jenkins Concepts

| Concept         | Description                                 |
|-----------------|---------------------------------------------|
| Job/Project     | A task like building or testing a project   |
| Build           | Execution of a job                         |
| Node            | Machine where Jenkins runs jobs             |
| Pipeline        | Set of automated steps (scripted or declarative) |
| Plugin          | Extensions that add features to Jenkins    |
|-----------------|---------------------------------------------|

---

## 💡 Sample Pipeline (Declarative)

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
```

---

## ✅ Best Practices

- Use **Pipeline as Code** with Jenkinsfiles.
- Use **parameterized builds** for flexibility.
- Regularly **backup** Jenkins home directory.
- Secure Jenkins with **user authentication**.
- Keep plugins **up-to-date**.

---

## 📜 Advanced Topics

- Distributed Builds with Master-Agent architecture
- Integrate Jenkins with GitHub/GitLab/Bitbucket
- Set up Dockerized builds
- Parallel stages in Pipelines
- Notifications with Slack, Email, etc.

---

*Last Updated: April 2025*

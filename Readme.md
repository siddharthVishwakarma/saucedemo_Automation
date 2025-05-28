# Selenium POM Automation Demo

> A Python‑based Selenium automation framework using the Page Object Model (POM) design pattern, with pytest integration, Docker containerization, and GitHub Actions CI pipeline.

---

## 📖 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)

  * [1. Clone the Repository](#1-clone-the-repository)
  * [2. Create & Activate Virtual Environment](#2-create--activate-virtual-environment)
  * [3. Install Dependencies](#3-install-dependencies)
  * [4. Configure Environment Variables](#4-configure-environment-variables)
* [Running Tests Locally](#running-tests-locally)
* [Docker Usage](#docker-usage)
* [CI/CD with GitHub Actions](#cicd-with-github-actions)
* [Project Structure](#project-structure)
* [Extending the Framework](#extending-the-framework)
* [Contributing](#contributing)
* [License](#license)

---

## Project Overview

This project demonstrates a maintainable, scalable web‑automation framework using Python and Selenium. It automates end‑to‑end scenarios on the [Sauce Demo](https://www.saucedemo.com) site, showcasing:

* **Login flow** (valid and invalid)
* **Product listing** interactions
* **Shopping cart** validations

Automation is structured via the **Page Object Model (POM)**, with tests powered by **pytest**. The repository includes:

* Secure handling of credentials via environment variables
* Headless browser support for CI
* Dockerfile for containerized test execution
* GitHub Actions workflow for continuous integration

---

## Features

* 🔍 **Page Object Model** for clear separation of page structure & test logic
* 🧪 **pytest** suite covering multiple scenarios
* 🔐 **Environment variables** management with `python-dotenv`
* 🐳 **Docker** containerization for isolated runs
* 🔄 **GitHub Actions** CI workflow triggering tests on push/PR

---

## Prerequisites

* Python 3.8 or higher
* `pip` package manager
* Google Chrome / Chromium (when running locally)
* Docker (optional, for containerized execution)

---

## Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/selenium-pom-demo.git
cd selenium-pom-demo
```

### 2. Create & Activate Virtual Environment

```bash
# macOS / Linux
env/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following (replace with your own values or leave defaults for Sauce Demo):

```env
SAUCE_USERNAME=standard_user
SAUCE_PASSWORD=secret_sauce
HEADLESS=true
```

> **Note:** `.env` is included in `.gitignore` to prevent leaking secrets.

---

## Running Tests Locally

With dependencies installed and `.env` configured, run:

```bash
pytest -q
```

* Tests will launch Chrome (headless by default) and execute all scenarios.
* To run in headed mode, set `HEADLESS=false`.

---

## Docker Usage

Build the Docker image:

```bash
docker build -t selenium-pom-demo .
```

Run tests inside the container:

```bash
docker run --rm \
  -e SAUCE_USERNAME=$SAUCE_USERNAME \
  -e SAUCE_PASSWORD=$SAUCE_PASSWORD \
  selenium-pom-demo
```

* The container uses headless Chrome by default.

---

## CI/CD with GitHub Actions

A CI pipeline is defined in `.github/workflows/ci.yml`. It:

1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs `pytest` with environment variables injected via GitHub Secrets

**GitHub Secrets** to configure in Settings:

* `SAUCE_USERNAME`
* `SAUCE_PASSWORD`

---

## Project Structure

```
├── pages/                    # Page Object Model classes
│   ├── base_page.py         # Common Selenium utilities
│   ├── login_page.py        # Login page object
│   ├── inventory_page.py    # Products listing page object
│   └── cart_page.py         # Shopping cart page object
├── tests/                   # pytest test suite
│   ├── conftest.py          # WebDriver setup fixtures
│   ├── test_login.py        # Valid/invalid login tests
│   └── test_add_to_cart.py  # Add-to-cart test
├── Dockerfile               # Containerized test environment
├── requirements.txt         # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
└── README.md                # Project documentation (this file)
```

---

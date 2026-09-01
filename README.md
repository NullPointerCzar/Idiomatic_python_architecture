# Python Mastery Architecture Demo

A production-ready, idiomatic Python demonstration project covering modern architecture, modules, custom exceptions, static type annotations, custom iterators, JSON serialization, REST HTTP clients, structured logging, CLI interfaces, unit testing, and standard packaging.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Architecture & Topic Mapping](#-architecture--topic-mapping)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage & CLI Tooling](#-usage--cli-tooling)
- [Running Tests](#-running-tests)
- [Git Step-by-Step Commit Guide](#-git-step-by-step-commit-guide)

---

## 🎯 Project Overview

This repository demonstrates how to write clean, maintainable, and idiomatic Python application code without using complex metaprogramming tricks. It provides a complete workflow for fetching remote user data over HTTP, validating and serializing JSON into strongly-typed models, iterating through records in batches, logging activity, and exposing commands via a CLI interface.

---

## 🛠 Architecture & Topic Mapping

| Required Knowledge Area | Implementation Standard | File Location |
| :--- | :--- | :--- |
| **Modules & Packages** | Package layout using `src/` layout and `__init__.py` | `src/mastery_demo/` |
| **Exceptions** | Domain-specific custom exception hierarchy | `src/mastery_demo/exceptions.py` |
| **Testing** | Automated unit tests using `pytest` | `tests/test_services.py` |
| **Static Typing** | PEP 585 modern type annotations (`list[T]`, `Iterator`) | All source files |
| **Iterators** | Custom class iterator defining `__iter__` and `__next__` | `src/mastery_demo/services.py` |
| **Serialization** | JSON payload validation and model conversion via Pydantic v2 | `src/mastery_demo/services.py` |
| **HTTP Basics** | Timeout-safe REST API client using `requests` | `src/mastery_demo/services.py` |
| **Logging** | Structured stream formatting with standard `logging` | `src/mastery_demo/logger.py` |
| **CLI Tooling** | Type-driven command-line commands powered by `typer` | `src/mastery_demo/cli.py` |
| **Packaging & Build** | Declarative PEP 621 configuration via `pyproject.toml` | `pyproject.toml` |

---

## 📁 Project Structure

```text
python-mastery-demo/
├── pyproject.toml              # Build & dependency configuration
├── README.md                   # Project documentation
├── .gitignore                  # Git untracked files configuration
├── src/
│   └── mastery_demo/
│       ├── __init__.py         # Package initialization
│       ├── exceptions.py       # Custom exception classes
│       ├── logger.py           # Structured logging utility
│       ├── services.py         # HTTP client, iterators & Pydantic models
│       └── cli.py              # Typer CLI application
└── tests/
    └── test_services.py        # Pytest test suite
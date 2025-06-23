# Project for Testing

[![Python Tests](https://github.com/AndriiObuh/Project_for_Testing/actions/workflows/python-tests.yml/badge.svg)](https://github.com/AndriiObuh/Project_for_Testing/actions/workflows/python-tests.yml)

This repository contains Python utility functions and their corresponding unit tests using **pytest**.

## 🧪 API Client (Pet Project)

This module implements a simple API client for interacting with [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a fake REST API for testing.

### 📂 Files:
- `app/api_client.py` — class `APIClient` with methods:
  - `get_posts()` — get list of posts
  - `get_post(post_id)` — get post by ID
- `tests/test_api_client.py` — tests using **mock** for:
  - Successful request
  - 404 errors
  - Data structure checks

### 🔧 Used:
- `requests` — HTTP-requests
- `pytest` — testing framework
- `unittest.mock` — mock external requests
- GitHub Actions — automatic test launch

---

## 📁 Project Structure

Project_for_Testing/
├── app/
│ └── api_client.py
├── tests/
│ └── test_api_client.py
├── requirements.txt
├── README.md

## ✅ How to Run Tests

1. Install dependencies:
pip install -r requirements.txt
2. Run tests:
pytest -v

📌 Author
Andrii Obuh



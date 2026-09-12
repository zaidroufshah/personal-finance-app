# Personal Finance & Expense Management

A full-stack learning project for managing income, expenses, and monthly budgets.

## Current progress

- FastAPI backend with a working GET / endpoint
- Python virtual environment and dependency setup
- Interactive API documentation at /docs

## Planned stack

React, JavaScript, Vite, Python, FastAPI, PostgreSQL, and SQLAlchemy.

## Run locally

Requires Python 3.13. From the project root in PowerShell:

```powershell
py -3.13 -m venv backend\.venv
.\backend\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
python -m uvicorn main:app --app-dir backend --reload
```

Open http://127.0.0.1:8000/ to view the response.

## Learning notes

See [Day 1 notes](docs/Day%201.md).

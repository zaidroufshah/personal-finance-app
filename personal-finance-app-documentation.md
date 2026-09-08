Personal-finance app



main.py

Here’s what each part means:

- `from fastapi import FastAPI` brings the `FastAPI` class into this file so we can use it.
- `app = FastAPI()` creates our application and assigns it to the variable `app`.
- `@app.get("/")` registers the function below it to handle **GET requests to `/`**, the root URL.
- `def read_root():` defines a function named `read_root`. The empty parentheses mean it takes no arguments; the colon starts its body.
- `return {...}` sends a Python dictionary back to FastAPI, which converts it into a JSON response.

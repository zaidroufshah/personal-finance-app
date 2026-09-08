from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Personal Finance API is running"}
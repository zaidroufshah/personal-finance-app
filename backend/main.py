from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_routes():
    return {"message": "My app is running"}



transactions = [ {"id": 1,
    "title": "Lunch",
    "amount": 120,
    "type": "expense"
},
{"id": 2,
    "title": "salary",
    "amount": 20000,
    "type": "income"
}


]

@app.get("/transactions")
def read_transactions():
    return {"transactions": transactions}
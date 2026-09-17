from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Calculator API",
    description="A simple REST API for basic mathematical operations.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Calculator API is running!"}


@app.get("/add")
def add(num1: float, num2: float):
    result = num1 + num2

    return {
        "operation": "addition",
        "num1": num1,
        "num2": num2,
        "result": result
    }

@app.get("/subtract")
def subtract(num1: float, num2: float):
    result = num1 - num2

    return {
        "operation": "subtraction",
        "num1": num1,
        "num2": num2,
        "result": result
    }

@app.get("/multiply")
def multiply(num1: float, num2: float):
    result = num1 * num2

    return {
        "operation": "multiplication",
        "num1": num1,
        "num2": num2,
        "result": result
    }

@app.get("/divide")
def divide(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="num2 cannot be zero")
    result = num1 / num2

    return {
        "operation": "division",
        "num1": num1,
        "num2": num2,
        "result": result
    }
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в калькулятор !"}
@app.get("/add/{num1}/{num2}")
def add_numbers(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}

@app.get("/subtract/{num1}/{num2}")
def subtract_numbers(num1: float, num2: float):
    result = num1 - num2
    return {"result": result}

@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(num1: float, num2: float):
    result = num1 * num2
    return {"result": result}

@app.get("/divide/{num1}/{num2}")
def divide_numbers(num1: float, num2: float):
    if num2 == 0:
        return {"error": "На ноль делить нельзя!"}
    result = num1 / num2
    return {"result": result}
from fastapi import FastAPI
from typing import Union
from primePy import primes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "By sprawdzić czy liczba jest pierwsza - http://localhost:8000/prime/10619863  " +
            " By odwrócić kolory obrazka  - http://127.0.0.1:8000/inversion/image.jpg"
            }

@app.get("/prime/{number}")
async def isprimenum(number: int):
    if isprimenum(number):  return {"message": "Liczba jest pierwsza"}
    else:
        return {"message": "Liczba nie jest pierwsza"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

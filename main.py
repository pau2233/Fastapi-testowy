from fastapi import FastAPI
from primePy import primes
import cv2

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "By sprawdzić czy liczba jest pierwsza - http://localhost:8000/prime/10619863  " +
            " By odwrócić kolory obrazka  - http://127.0.0.1:8000/inversion/image.jpg"
            }

@app.get("/prime/{number}")
async def isprimenum(number: int):
    if primes.check(number):  return {"message": "Liczba jest pierwsza"}
    else:
        return {"message": "Liczba nie jest pierwsza"}

@app.get("/inversion/{image}")
async def inversepicture(image):
    image = cv2.imread(image)
    image = ~image
    cv2.imwrite("img_inverted.jpg", image)
    return {"message": "Obrazek jest teraz nawiedzony"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

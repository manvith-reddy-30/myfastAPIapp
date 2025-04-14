from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/greet/")
async def greet_with_greets(greets:Optional[str] = "Hello",name:str="User"):
    return f"<h1>{greets}, {name}!</h1>"
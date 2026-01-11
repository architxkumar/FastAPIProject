from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    result = httpx.get("https://jsonplaceholder.typicode.com/users")
    return result.json()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# fastapi dev main.py
from fastapi import FastAPI
from routers import pipeline

app = FastAPI()
app.include_router(pipeline.router, prefix="/pipeline", tags=["Pipeline"])


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}

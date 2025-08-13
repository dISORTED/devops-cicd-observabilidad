from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "demo"}

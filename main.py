from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello from my first backend server!"}

@app.get("/health")
def health():
    return{"status": "ok"}
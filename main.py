from fastapi import FastAPI

app = FastAPI(title="Suarez AI OS")

@app.get("/")
def root():
    return {"status": "AI OS running"}

from fastapi import FastAPI


app = FastAPI(title="Academia")

@app.get("/health")
def health_check():
    return{"status" : "ok"}
from fastapi import FastAPI

app = FastAPI(title="Mon API", version="0.1.0")


@app.get("/")
def read_root():
    return {"message": "API en ligne"}

@app.get("/health")
def read_root():
    return {"status": "ok"}


@app.get("/mycicd")
def read_root():
    return {"message": "ci et cd sont prets a 100 %"}

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello test 2": "From FastAPI on Kubernetes"}
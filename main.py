from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello test 3": "From FastAPI on Kubernetes"}
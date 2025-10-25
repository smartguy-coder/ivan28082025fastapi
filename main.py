from fastapi import FastAPI

app = FastAPI(
    debug=True
)


@app.get("/")
def get_info():
    return {"status": "ok"}
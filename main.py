from fastapi import FastAPI

app = FastAPII()


@app.get("/")
async def root():
    return {"message": "Hello World new"}

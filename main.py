from fastapi import FastAPI

app = FastAPI()

# test comment
@app.get("/")
async def root():
    return {"message": "Hello World new"}

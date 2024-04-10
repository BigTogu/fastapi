from fastapi import FastAPI
from operations import router




app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



app.include_router(router, prefix="/operations", tags=["operations"])
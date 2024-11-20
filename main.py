from fastapi import FastAPI
from user_interactions import router as user_router
from recommendation import router as recommendation_router

app = FastAPI()
app.include_router(user_router)
app.include_router(recommendation_router)

@app.get("/")
async def root():
    return {"message": "Welcome to recommendation system"}
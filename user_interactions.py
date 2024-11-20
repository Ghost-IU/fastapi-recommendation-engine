from pydantic import BaseModel, EmailStr
from redis_client import r as client
from fastapi import APIRouter, FastAPI
from tasks import process_tasks

class Interactions(BaseModel):
    # users, products
    user_id: int
    product_id: int
    interaction_type: str

router = APIRouter()

@router.post("/create_log/")
def create_item(interaction: Interactions):
    client.zadd(f"user:{interaction.user_id}:interactions",
                {f"{interaction.product_id}:{interaction.interaction_type}":0})
    # process_tasks.delay(
    #     interaction.user_id,
    #     interaction.product_id,
    #     interaction.interaction_type
    # )
    return {"message" : "User interactions stored!"}

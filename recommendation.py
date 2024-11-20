from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from fastapi import APIRouter

router = APIRouter()

# get dummy values, try to return dummy recommendations 
sample = {
    1: [100, 200, 201],
    2: [300, 211, 111],
    3: [101, 102, 333],
    4: [123, 454, 555],
    5: [1243, 123, 555],
    "other" : [109, 102, 106]
}

@router.get('/recommendations/{user_id}')
def get_recommendation(user_id: int):
    recom = sample.get(user_id, sample['other'])
    return {"user_id": user_id, "recommendations": recom}

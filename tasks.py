from celery_app import celery_app

@celery_app.task
def process_tasks(user_id:int, product_id:int, interaction_type: str):
    print(f"Processing interaction for user: {user_id}")
    print(f"Logged interactions for {user_id}: Product ID {product_id}, Type {interaction_type}")
    return {"log_status": "done", "user_id": user_id, "product_id":product_id}
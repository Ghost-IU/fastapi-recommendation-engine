from celery import Celery

celery_app = Celery('tasks',
             broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/1')

# Optional configuration, see the application user guide.
celery_app.conf.update(
    task_serializer = 'json',
    result_serializer = "json",
    accept_content = ['json'],
    timezone = "UTC",
    enable_utc = True
)

# if __name__ == '__main__':
#     app.start()
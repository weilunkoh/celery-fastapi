import os

from celery import Celery
from fastapi import APIRouter

router = APIRouter()

celery_app = Celery(
    "client",
    broker=os.getenv("CELERY_BROKER_URL", "pyamqp://guest@localhost:5672//"),
    backend=os.getenv(
        "CELERY_RESULT_BACKEND",
        "db+mysql+mysqlconnector://user:password@localhost:3306/celery_db",
    ),
    # broker=os.getenv("CELERY_BROKER_URL", "pyamqp://guest@rabbitmq//"),
    # backend=os.getenv(
    #     "CELERY_RESULT_BACKEND",
    #     "db+mysql+mysqlconnector://user:password@mysql/celery_db",
    # ),
)
celery_app.conf.update(timezone="Asia/Singapore")


@router.post("/send-task/")
def send_task(data: dict):
    print(data)
    task = celery_app.send_task(
        "worker1.process_task1", kwargs={"data": data}, queue="queue1"
    )
    return {"task_id": task.id}

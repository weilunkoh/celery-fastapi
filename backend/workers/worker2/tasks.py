# celery -A tasks worker -n worker2 -Q queue2 --pool=solo
import os
import time

from celery import Celery

celery_app = Celery(
    "worker2",
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


@celery_app.task(name="worker2.process_task2")
def process_task2(data: dict):
    print(f"Worker 2 processing: {data}")

    # Simulate some processing time
    start_time = time.time()
    time.sleep(int(os.getenv("WORKER2_SLEEP_TIME", 3)))
    end_time = time.time()
    print(f"Worker 2 finished processing in {end_time - start_time} seconds")

    return {"status": "Task completed"}

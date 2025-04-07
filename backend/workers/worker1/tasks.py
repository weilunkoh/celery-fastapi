# celery -A tasks worker -n worker1 -Q queue1 --pool=solo

# OR (with multiple worker 1s)

# celery -A tasks worker -n worker1a -Q queue1 --pool=solo
# celery -A tasks worker -n worker1b -Q queue1 --pool=solo

import os
import time

from celery import Celery

celery_app = Celery(
    "worker1",
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


@celery_app.task(name="worker1.process_task1")
def process_task1(data: dict):
    print(f"Worker 1 processing: {data}")

    # Simulate some processing time
    start_time = time.time()
    time.sleep(int(os.getenv("WORKER1_SLEEP_TIME", 30)))
    end_time = time.time()
    print(f"Worker 1 finished processing in {end_time - start_time} seconds")

    celery_app.send_task("worker2.process_task2", kwargs={"data": data}, queue="queue2")
    return {"status": "Task forwarded to Worker 2"}

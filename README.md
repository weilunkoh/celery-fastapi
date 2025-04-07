# Multiple Celery Workers Example

This repository is about a simple application that demonstrates having multiple Celery workers for the following:
- working on similar tasks (i.e. worker1a, worker1b)
- working on different tasks (i.e. worker2)

The tasks are sent by users when they call a FastAPI endpoint. The endpoint sends a RabbitMQ message to Celery Worker1s. In turn, after any Worker1 completes a task, it will send another RabbitMQ message to Worker2 for another task.
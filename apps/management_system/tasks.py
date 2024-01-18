from celery import shared_task

@shared_task(
    bind=True,
    name='Task Example Name',
    autoretry_for=(Exception,),
    max_retries=1
)
def tsk_example():
    return "Task Example Execution"
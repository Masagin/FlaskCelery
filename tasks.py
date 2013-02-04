from celery import Celery

celery = Celery(__name__)

celery.conf.update(
        BROKER_BACKEND = 'sqlalchemy',
        BROKER_HOST = "sqlite:///my.db",
        CELERY_RESULT_BACKEND = "database",
        CELERY_RESULT_DBURI = "sqlite:///my.db",
        CELERY_IMPORTS = ("tasks", ),
)
  
@celery.task(name="tasks.add")
def add(x, y):
    return x + y

if __name__ == "__main__":
    celery.start()
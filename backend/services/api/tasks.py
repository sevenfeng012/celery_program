from celery import Celery
from celery.apps import worker as celery_worker
from celery.utils.log import get_task_logger
from celery.app.task import Task
from logging import Logger

import time
from celery.canvas import chain
# from gevent import monke

# monkey.patch_all()

import json
import requests


app = Celery("tasks", backend="redis://localhost:6379/0",
             broker="redis://localhost:6379/0")

app.conf.update(
    ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['application/json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Shanghai',
)


class AjmdBaseTask(Task):
    """docstring for AjmdBaseTask"""

    abstract = True
    default_retry_delay = 1
    max_retries = 3
    ignore_result = True
    task_time_limit = 15
    acks_late = True

    def on_success(self, retval, task_id, args, kwargs):
        print 'task done: {0}'.format(retval)
        return super(AjmdBaseTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print 'task fail, reason: {0}'.format(exc)
        return super(AjmdBaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)


def calstoreresult(x, y):
    chain = add.s(x, y) | store_result.s()
    chain()


@app.task(base=AjmdBaseTask)
def add(x, y):
    print "add result:"

    ret = x + y
    return ret


@app.task()
def store_result(ret):
    print "result=" + str(ret)
    payload = {"result": str(ret)}
    requests.post(url="http://127.0.0.1:9883/db", data=json.dumps(payload))

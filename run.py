# -*- coding: utf-8 -*-
from datetime import timedelta

from rq import Queue
from redis import Redis
import time

from jobs import count_words_at_url, get_redis_keys

redis_conn = Redis('127.0.0.1', db=0)
q = Queue('default', connection=redis_conn)

job = q.enqueue(count_words_at_url, 'http://nvie.com')
print(job.result)

time.sleep(2)
print(job.result)

q = Queue('queue_1', connection=redis_conn)

job = q.enqueue_in(timedelta(seconds=10), get_redis_keys)
print(job.result)

time.sleep(12)
print(job.result)

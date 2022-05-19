# -*- coding: utf-8 -*-
from datetime import timedelta
import time

from rq_demo import rq_default_queue, rq_queue_1
from jobs import count_words_at_url, get_redis_keys

job = rq_default_queue.enqueue(count_words_at_url, 'http://nvie.com')
print(job.result)

time.sleep(2)
print(job.result)

job = rq_queue_1.enqueue_in(timedelta(seconds=5), get_redis_keys)
print(job.result)

time.sleep(6)
print(job.result)

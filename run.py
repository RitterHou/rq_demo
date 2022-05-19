# -*- coding: utf-8 -*-
from datetime import timedelta
import time

from rq import Retry

from rq_demo import rq_default_queue, rq_queue_1
from jobs import count_words_at_url, get_redis_keys, report_success

rq_default_queue.enqueue(count_words_at_url, 'https://www.jd.com', on_success=report_success,
                         retry=Retry(max=3, interval=[1, 3, 6]))

job1 = rq_default_queue.enqueue(count_words_at_url, 'http://nvie.com')
print(job1.result)
time.sleep(2)
print(job1.result)

job2 = rq_queue_1.enqueue_in(timedelta(seconds=5), get_redis_keys)
print(job2.result)
time.sleep(6)
print(job2.result)

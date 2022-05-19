# -*- coding: utf-8 -*-
from redis import Redis
from rq import Queue

redis_conn = Redis('127.0.0.1', db=0)
rq_default_queue = Queue('default', connection=redis_conn)
rq_queue_1 = Queue('queue_1', connection=redis_conn)

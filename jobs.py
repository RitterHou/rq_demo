# -*- coding: utf-8 -*-
import requests
from redis import Redis

redis_cli = Redis('127.0.0.1', db=0)


def report_success(job, connection, result, *args, **kwargs):
    print(result)


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def get_redis_keys():
    return redis_cli.keys()

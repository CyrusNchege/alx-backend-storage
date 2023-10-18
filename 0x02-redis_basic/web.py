#!/usr/bin/env python3
""" expiring web cache module """

import redis
import requests
from typing import Callable
from functools import wraps

class WebCache:
    def __init__(self):
        self.redis = redis.Redis()

    def count_access(self, url):
        self.redis.incr(f"count:{url}")

    def cache_page(self, url, result):
        self.redis.setex(f"cached:{url}", 10, result)

    def get_page(self, url: str) -> str:
        self.count_access(url)
        cached_response = self.redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        response = requests.get(url)
        result = response.text
        self.cache_page(url, result)
        return result

if __name__ == "__main__":
    web_cache = WebCache()

    @web_cache.get_page
    def get_page(url: str) -> str:
        response = requests.get(url)
        return response.text


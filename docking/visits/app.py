#!/usr/bin/env python3
# python3 + redis test app with docker-compose
# myke 2019-01-27 1.2

from flask import Flask
from redis import Redis

app = Flask (__name__)
redis = Redis (host='redis', port=6379)

@app.route ('/')
def hello ():
    count = redis.incr ('visits')
    return 'Hello my dear friend! Visit #{}.'.format(count)

if __name__ == "__main__":
    app.run (host="0.0.0.0", debug=True)


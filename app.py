from rediscluster import StrictRedisCluster
import time
from flask import Flask


app = Flask(__name__)
startup_nodes = [{"host": "redis-cluster", "port": "6379"}]
cache = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)


def get_hit_count1():
    return cache.incr('hits')

def get_hit_count2():
    return cache.incr('test')

def get_hit_count3():
    return cache.incr('blab')

@app.route('/')
def hit():
    #s = "This is an {example} with {vars}".format(vars="variables", example="example")
    page = "hits: {hits}\ntest: {test}\nblab: {blab}".format(hits=get_hit_count1(), test=get_hit_count2(), blab=get_hit_count3())
    return page


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

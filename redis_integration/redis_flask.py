import time

from flask import Flask, jsonify
# import the flask extension
from flask_cache import Cache
import redis
app = Flask(__name__)

# define the cache config keys, remember that it can be done in a settings file
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_DB'] = 0

# register the cache instance and binds it on to your app
app.cache = Cache(app)

@app.route("/")
@app.cache.cached(timeout=300, key_prefix='date_key')  # cache this view for 300 seconds
def cached_view():
    print('In function')
    return time.ctime()

if __name__ == "__main__":
    app.run(port=5000, debug=True)

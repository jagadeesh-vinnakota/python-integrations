import time
from flask import Flask, jsonify

# import the flask extension
from flask_cache import Cache

app = Flask(__name__)

# define the cache config keys, remember that it can be done in a settings file
app.config['CACHE_TYPE'] = 'simple'

# register the cache instance and binds it on to your app
app.cache = Cache(app)

@app.route("/")
@app.cache.cached(timeout=30)  # cache this view for 30 seconds
def cached_view():
    print('Creating dictionary')
    dicti = {}
    dicti.update({'a':"value1"})
    dicti.update({'b':"value2"})
    return jsonify(dicti), time.ctime()

if __name__ == "__main__":
    app.run(port=5000, debug=True)

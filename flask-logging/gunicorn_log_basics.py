import logging
from flask import Flask, jsonify
import gunicorn
app = Flask(__name__)

gunicorn_logger = logging.getLogger(gunicorn.logger)
app.logger.handlers = gunicorn_logger.handlers
@app.route("/")
def index():
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')

    return jsonify('hello world')

if __name__ == '__main__':
    app.run(debug=True)

#gunicorn --workers=0 --bind=0.0.0.0:8000 --log-level=warning app:app

#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04

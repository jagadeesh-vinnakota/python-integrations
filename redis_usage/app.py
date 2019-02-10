import redis
red = redis.Redis(host='localhost', db=0)
red.set('job','Data Scientist')
print(red.get('job'))

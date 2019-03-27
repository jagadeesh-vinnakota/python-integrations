import redis
'''
    Redis is an in memory key value data store which can used as cache, message broker. 
'''

#setting up the redis data base
red = redis.Redis(host='localhost', db=0)

#storing the key value pair
red.set('job','Data Scientist')
#print(red.get('job'))
print(red.get('date_key'))

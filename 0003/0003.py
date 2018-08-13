__author__ = 'tsingxu'
import redis,uuid

r = redis.StrictRedis(host='localhost',port=6379)
for i in range(10):
    r.set('key_id'+str(i),uuid.uuid1())

for i in range(10):
    print(r.get("key_id"+str(i)))
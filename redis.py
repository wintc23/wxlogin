import redis


class CRedis:
    def __init__(self):
        self.host="localhost"
        self.port=6379
        self.db=0
        self.r=redis.Redis(host=self.host,port=self.port,db=self.db)

    def hset(self,token_id,token_str):
        return self.r.hset('wxlogin',token_id,token_str)

    def hget(self,token_id):
        return self.r.hget("wxlogin",token_id)

    def hdel(self,name,key=None):
        if (key):
            return self.r.hdel(name,key)
        return self.hdel(name)

    def clear(self):
        return self.r.flushdb()

    def hgetall():
        return self.r.hgetall('wxlogin')


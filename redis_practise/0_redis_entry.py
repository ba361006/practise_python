"""
before running this script, please make sure your redis server is running
check README.md for further information
"""
import redis

def single_set(service: redis.client.Redis) -> None:
    print()
    print("### single set ###")
    service.set(name="hello", value="world")
    
    # this will return bytes instead by default
    response = service.get(name="hello")
    print(response, response.__class__)

    # to convert bytes to str
    response = service.get(name="hello").decode("utf-8")
    print(response, response.__class__)
    

def multiple_set(service: redis.client.Redis) -> None:
    print()
    print("### multiple set ###")
    service.mset(mapping={"hello1": "world1", "hello2": "world2"})
    response = service.mget(keys=["hello1", "hello2", "wrong_key"])
    print(response)

if __name__ == "__main__":
    # TCP socket connection and reuse is done behind the scenes after invoking redis.Redis()
    # default port will be 6379
    redis_service = redis.Redis()
    
    single_set(service=redis_service)
    multiple_set(service=redis_service)

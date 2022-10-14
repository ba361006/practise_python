# tutorial
> https://realpython.com/python-redis/

# config
following by the tutorial, config file is located at `/etc/redis/6379.conf`

# command line
- start redis server
    - `redis-server <path_to_your_config_file`
        - following by the tutorial, the command line would be `redis-server /etc/redis/6379.conf`
- shutdown redis server
    - `pkill redis-server` / `redis-cli shutdown`(this one is for MacOS)
- get in server
    - `redis-cli`
        - enter `PING`(case-insensitive), it should response `PONG`
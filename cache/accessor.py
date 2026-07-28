import redis


def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        password=None
    )


# def set_object(key, value):
#     conn = get_redis_connection()
#     return conn.set(key, value)
#
#
# def get_all_objects(key_list):
#     conn = get_redis_connection()
#     return conn.mget(key_list)
#
#
# def get_object(key):
#     conn = get_redis_connection()
#     return conn.get(key)
#
#
# def get_all_keys():
#     conn = get_redis_connection()
#     for key in conn.scan_iter("*"):
#         print(key)
#
#
# # set_object('bike:1', 'welt')
# # set_object('bike:2', 'aspect')
# # set_object('bike:3', 'cube')
# # print(get_object('bike:1'))
# # print(get_object('bike:2'))
# # print(get_object('bike:3'))
# #
# # print(get_all_objects(['bike:1', 'bike:2', 'bike:3']))
#
# get_all_keys()



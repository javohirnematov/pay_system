import redis

# создать подключение к redis
redis_db = redis.from_url('redis://redis_db')               # redis_db берем из docker_compose 29 строчка


# # создать запись в базе данных
# redis_db.set("spam", 10)           # создает запись в базе ввиде словаря{'spam': 10}
#
#
# # получить значение из базы
# data = redis_db.get("spam")
# print(data)
#
# # задать время существования переменной
# redis_db.set("spam2", "Hello", 5)
# data2 = redis_db.get("spam2")
# print(data2)
#

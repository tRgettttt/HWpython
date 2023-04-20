from time import time
def time_decor(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Время выполнения функции {end - start} секунд")
        return result
    return wrapper

@time_decor
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()
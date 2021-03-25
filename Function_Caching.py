from time import sleep
from functools import lru_cache

@lru_cache(maxsize = 3)
def some_work(n):
    sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("done... calling again")
    some_work(3)
    print("called")
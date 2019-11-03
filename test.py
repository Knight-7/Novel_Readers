from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint


def wait(n):
    sleep(n)
    print(f'sleep {n} second')


p = ThreadPoolExecutor(3)
f = []
for i in range(10):
    print(i)
    f.append(p.submit(wait, randint(5, 10)))
    if i == 7:
        for ff in f:
            print(ff.cancel())
        p.shutdown()
        break
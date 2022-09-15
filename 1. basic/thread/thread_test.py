# 일반적으로 오래 걸리는 테스트

import time


def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" % i)


print("Start")

for i in range(5):
    long_task()

print("End")

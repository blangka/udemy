# 동시 별렬 수행 시키는 테스트
import threading
import time


def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" % i)


print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join을 하지 않으면 메인 스레드가 종료되면서 다른 스레드도 종료됨

print("End")

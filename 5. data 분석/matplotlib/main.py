import matplotlib.pyplot as plt

# 선 그래프
# plt.plot(x축, y축)
plt.plot([1, 2, 3, 4])
plt.ylabel("some numbers")
# plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()

import numpy as np

x = np.arange(-4.5, 5, 0.5)  # -4.5 ~ 5 사이의 0.5 간격의 배열
y = 2 * x ** 2  # 수식을 이용해서 배열 x에 대응하는 배열 생성

plt.plot(x, y)
# plt.show()

# 새창에 여러개 그리기
# plt reset
plt.clf()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.figure()
plt.plot([1, 2, 3, 4], [1, 3, 5, 7])
# plt.show()

# 여러창에 그리는것 샘플
# 데이터 생성
plt.clf()
x = np.arange(-5, 5, 0.1)
y1 = x ** 2
y2 = 20 * np.cos(x) ** 2  # 20 * cos(x)^2

plt.figure(1)  # 1번 창 생성
plt.plot(x, y1)

plt.figure(2)  # 2번 창 생성
plt.plot(x, y2)

plt.figure(1)  # 1번 창 선택
plt.plot(x, y2)

plt.figure(2)  # 2번 창 선택
plt.clf()  # 2번 창의 그래프를 지움
plt.plot(x, y1)

# plt.show()

# 하나 창에 여러개 그리는 subplot 샘플
# 데이터 생성
plt.clf()
x = np.arange(0, 10, 0.1)
y1 = 0.3 * (x - 5) ** 2 + 1
y2 = -1.5 * x + 3
y3 = np.sin(x) ** 2
y4 = 10 * np.exp(-x) + 1

plt.subplot(2, 2, 1)  # 2행 2열의 1번째 그래프
plt.plot(x, y1)

plt.subplot(2, 2, 2)  # 2행 2열의 2번째 그래프
plt.plot(x, y2)

plt.subplot(2, 2, 3)  # 2행 2열의 3번째 그래프
plt.plot(x, y3)

plt.subplot(2, 2, 4)  # 2행 2열의 4번째 그래프
plt.plot(x, y4)

# plt.show()

# 그래프의 출력 범위 지정하기 xlim, ylim
plt.clf()

x = np.linspace(-4, 4, 100)  # -4 ~ 4 사이의 100개의 데이터 생성
y1 = x ** 3
y2 = 10 * x ** 2 - 2

plt.plot(x, y1, x, y2)
plt.xlim(-1, 1)  # x축의 범위를 -1 ~ 1로 지정
plt.ylim(-3, 3)  # y축의 범위를 -3 ~ 3로 지정
# plt.show()

# 그래프 꾸미기
plt.clf()
x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

# plt.plot(x, y1, "m", x, y2, "y", x, y3, "k", x, y4, "c")
plt.plot(x, y1, "-", x, y2, "--", x, y3, ":", x, y4, "-.")
plt.title("legend")
plt.legend(["data1", "data2", "data3", "data4"], loc=2)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.text(2, 4, "Hello")
plt.show()

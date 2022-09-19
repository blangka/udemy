# 산점도 2개의 요소로 이루워진 집합 관계
# 키와 몸무계의 관계

import matplotlib.pyplot as plt
from matplotlib import rc

rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

height = [165, 177, 160, 180, 185, 155, 172]
weight = [62, 67, 55, 74, 90, 43, 64]

plt.scatter(height, weight, s=100, c="r", marker="^")
plt.xlabel("height")
plt.ylabel("weight")
plt.title("height & weight")
plt.grid(True)
# plt.show()

plt.clf()

# 막대 그래프
import numpy as np

member_IDs = ["m_01", "m_02", "m_03", "m_04"]  # 회원 아이디
before_ex = [27, 35, 40, 33]  # 운동 전
after_ex = [30, 38, 42, 37]  # 운동 후
colors = ["r", "g", "b", "c"]  # 색상

n_data = len(member_IDs)  # 회원 수
index = np.arange(n_data)  # 0 ~ 회원 수 - 1
plt.bar(
    index, before_ex, color=colors, tick_label=member_IDs, align="center", width=0.6
)
# 세로 막대 그래프는 bar, 가로 막대 그래프는 barh
# plt.show()
plt.clf()

# 2개 비교 그래프
barWidth = 0.4
plt.bar(index, before_ex, color="c", align="edge", width=barWidth, label="before")
plt.bar(
    index + barWidth, after_ex, color="m", align="edge", width=barWidth, label="after"
)

plt.xticks(index + barWidth, member_IDs)
plt.legend()
plt.xlabel("member ID")
plt.ylabel("score")
plt.title("before and after the exercise")
plt.grid(True)
# plt.show()
plt.clf()

# 히스토그램
# 히스토그램은 데이터의 분포를 보여주는 그래프
# 히스토그램은 막대 그래프와 비슷하지만, 막대 그래프는 범주형 데이터를 표현하는데 반해
# 히스토그램은 연속형 데이터를 표현
# plt.hist(데이터, bins=구간 수, range=(최소값, 최대값), color=색상, label=범례)
# bins: 구간 수, range: 최소값과 최대값, color: 색상, label: 범례

# 1. 데이터 생성
math = [76, 82, 84, 83, 90, 86, 85, 91, 76, 79]
plt.hist(math, bins=5, range=(75, 100), color="c", label="math")
# plt.show()
plt.clf()

# 파이 그래프
# 파이 그래프는 원형 그래프로, 전체에서 각 항목이 차지하는 비율을 보여줌
# plt.piex(데이터, labels=항목 이름, autopct=비율 표시 형식, shadow=True, startangle=시작 각도)

# 1. 데이터 생성
fruit = ["사과", "바나나", "딸기", "오렌지", "포도"]
result = [7, 6, 3, 2, 2]

# 2. 파이 그래프 그리기
# plt.pie(result, labels=fruit, autopct="%.1f%%", shadow=True, startangle=90)
explode_value = (0, 0.1, 0, 0, 0)
plt.figure(figsize=(5, 5))
plt.pie(
    result,
    labels=fruit,
    autopct="%.1f%%",
    shadow=True,
    startangle=90,
    explode=explode_value,
    counterclock=False,
)

plt.show()

# 그래프 이미지 파일로 저장
plt.savefig("pie_chart.png")

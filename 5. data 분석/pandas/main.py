# 구조 데이터 생성하기
import numpy as np
import pandas as pd

# serias 생성
# pandas에서 가장 기본적인 데이터 구조(라벨을 갖는 1차원 데이터)
# 세로축을 index라고 하고 시퀀스 데이터를 values라고 한다.
s = pd.Series([1, 3, 5, 7, 9])
print(s)
print(s.values)
print(s.index)

s2 = pd.Series(["a", "b", "c", 1, 2, 3])
print(s2)

s3 = pd.Series([np.NAN, 10, 30])
print(s3)

# index 값을 추가 하여서 사용
s4 = pd.Series([1, 3, 5, 7, 9], index=["a", "b", "c", "d", "e"])
print(s4)

# 날짜 자동 생성 : date_range
# pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None, **kwargs)
# start : 시작 날짜
# end : 종료 날짜
# periods : 생성할 기간의 수
# freq : 날짜 생성 규칙
# tz : 시간대
# normalize : 정규화 여부
# name : 시리즈 이름
# closed : 시작과 종료 날짜를 포함할지 여부
# **kwargs : freq에 대한 추가적인 인자
print(pd.date_range("2021-01-01", "2021-01-10"))

# 2일씩 증가하는 날짜
print(pd.date_range("2021-01-01", periods=5, freq="2D"))
# 요일을 기준으로 일주일씩 증가하는 날짜
print(pd.date_range("2021-01-01", periods=5, freq="W"))
# 업무일 기준 2개월 월말 주기로 12개의 날짜를 생성
print(pd.date_range("2021-01-01", periods=12, freq="2BM"))
# 분기 시작일을 기준으로 4개의 날짜 생성
print(pd.date_range("2021-01-01", periods=4, freq="QS-JAN"))
# 1시간 주기로 10개의 시간 생성
print(pd.date_range("2021-01-01", periods=10, freq="H"))

# DataFrame 생성
# pandas에서 가장 기본적인 데이터 구조(라벨을 갖는 2차원 데이터)
# DataFrame은 행과 열로 구성된다.
# 행은 index, 열은 columns이라고 한다.
# DataFrame은 Series의 집합이다.
# DataFrame은 2차원 배열이다.

# 2차원 배열을 이용하여 생성
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df)
df = pd.DataFrame(np.random.randn(6, 4))
print(df)
df = pd.DataFrame(
    np.random.randn(6, 4),
    index=pd.date_range("2021-01-01", periods=6),
    columns=list("ABCD"),
)
print(df)

# 딕셔너리 타입 데이터 저장
table_data = {
    "연도": [2015, 2016, 2016, 2017, 2017],
    "지사": ["한국", "한국", "미국", "한국", "미국"],
    "고객 수": [200, 250, 450, 300, 500],
}
df = pd.DataFrame(table_data)
print(df)

# 연산
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
print(s1 + s2)


table_data3 = {
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50],
    "C": [100, 200, 300, 400, 500],
    "D": [1000, 2000, 3000, 4000, 5000],
    "E": [10000, 20000, 30000, 40000, 50000],
}
columns_list = ["A", "B", "C", "D", "E"]
index_list = pd.date_range("2021-01-01", periods=5)

df3 = pd.DataFrame(table_data3, index=index_list, columns=columns_list)
print(df3)
print(df3.mean())
print(df3.std())  # 표준편차

# 행별 연산
print(df3.mean(axis=1))

# 연산 한번에 보기
print(df3.describe())

# 2011년 부터 2017년까지 노선별 KTX 이용객 수
KTX_data = {
    "경부선 KTX": [39060, 42060, 45060, 48060, 51060, 54060, 57060],
    "호남선 KTX": [7312, 6939, 3200, 3260, 5360, 3060, 160],
    "경전선 KTX": [390, 420, 453, 48, 51, 540, 573],
    "전라선 KTX": [30, 42, 45, 4, 5, 5, 57033],
    "동해선 KTX": [np.NAN, np.NAN, np.NAN, np.NAN, 323, 42, 43],
}
col_list = {"경부선 KTX", "호남선 KTX", "경전선 KTX", "전라선 KTX", "동해선 KTX"}
index_list = ["2011", "2012", "2013", "2014", "2015", "2016", "2017"]

df_KTX = pd.DataFrame(KTX_data, index=index_list, columns=col_list)
print(df_KTX)
print(df_KTX.index)
print(df_KTX.columns)
print(df_KTX.values)

# 일부만 보이게
print(df_KTX.head(3))
print(df_KTX.tail(3))
print(df_KTX[1:2])
print(df_KTX["경부선 KTX"]["2011":"2013"])
print(df_KTX.loc["2011"])

# 2016년 '호남선KTX' 이용자수
print(df_KTX["호남선 KTX"]["2016"])
print(df_KTX.loc["2016"]["호남선 KTX"])
print(df_KTX.iloc[5][1])
print(df_KTX["호남선 KTX"][5])

# 행과 열을 바꾸는 전치
print(df_KTX.T)

# 데이터 통합하기
# 세로로 통합하기 가로로 통합하기 등 다양한 방법으로 데이터 들을 추가 하는 방법을 확인해 본다.

df1 = pd.DataFrame({"Class1": [95, 92, 98, 100], "Class2": [91, 93, 97, 99]})
df2 = pd.DataFrame({"Class1": [87, 89], "Class2": [85, 90]})

# 세로로 통합하기
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)
df3 = df1.append(df2, ignore_index=True)
print(df3)

df1 = pd.DataFrame({"Class1": [95, 92, 98, 100], "Class2": [91, 93, 97, 99]})
df2 = pd.DataFrame({"Class3": [87, 89, 92, 34]})

# 가로로 통합하기
df4 = pd.concat([df1, df2], axis=1)
print(df4)
df4 = df1.join(df2)
print(df4)

# 특정 열 기준으로 통합하기
df1 = pd.DataFrame(
    {
        "판매월": ["1월", "2월", "3월", "4월"],
        "제품A": [100, 150, 200, 130],
        "제품B": [90, 110, 140, 170],
    }
)
df2 = pd.DataFrame(
    {
        "판매월": ["1월", "2월", "3월", "4월"],
        "제품C": [112, 141, 203, 134],
        "제품D": [90, 110, 140, 170],
    }
)
df5 = pd.merge(df1, df2, on="판매월")
print(df5)
df5 = df1.merge(df2)
print(df5)

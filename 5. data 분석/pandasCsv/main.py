# csv 엑셀 실습
import numpy as np
import pandas as pd

df1 = pd.read_csv("./sea_rain1_from_notepad.csv", encoding="cp949")
print(df1)
df2 = pd.read_csv("./sea_rain1_from_notepad.csv", index_col="연도", encoding="cp949")
print(df2)

# 표 형식의 데이터를 파일로 쓰기
df_WH = pd.DataFrame(
    {"Weight": [68, 83, 112, 44, 99], "Height": [170, 180, 165, 143, 154]},
    index=["ID_1", "ID_2", "ID_3", "ID_4", "ID_5"],
)
df_WH.index.name = "User"
print(df_WH)
# BMI 체질량 지수 = 몸무게 / 키^2
bmi = df_WH["Weight"] / (df_WH["Height"] / 100) ** 2
df_WH["BMI"] = bmi
df_WH.to_csv("./df_WH.csv", encoding="cp949")

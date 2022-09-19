# pandas의 선그래프
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

rc("font", family="AppleGothic")
plt.rcParams["axes.unicode_minus"] = False

s1 = pd.Series([1, 2, 3, 4])
s1.plot(grid=True)
plt.show(block=False)
plt.close()

df_rain = pd.read_csv("sea_rain1_from_notepad.csv", encoding="cp949", index_col="연도")
df_rain.plot(grid=True)
plt.show(block=False)
plt.close()

# pandas 산점도

temperature = [20.1, 19.9, 19.6, 19.5, 19.3, 19.1, 19.0, 18.9, 18.8, 18.7]
Ice_cream_sales = [10, 7, 5, 8, 4, 11, 9, 13, 8, 12]
dict_data = {"temperature": temperature, "Ice_cream_sales": Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data, columns=["temperature", "Ice_cream_sales"])
print(df_ice_cream)
df_ice_cream.plot.scatter(x="temperature", y="Ice_cream_sales", grid=True)
plt.show(block=False)
plt.close()

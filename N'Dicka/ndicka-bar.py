import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

ndicka_data = pd.read_excel('./Ndicka.xlsx', 'NDicka').round(2)
ndicka_data = ndicka_data[ndicka_data['Per 90'].notna()]

akanji_data = pd.read_excel('./Ndicka.xlsx', 'Akanji').round(2)
akanji_data = akanji_data[akanji_data['Per 90'].notna()]

bar_data_1 = ndicka_data[ndicka_data['Statistic'].isin(["Pass Completion %", "% of dribblers tackled", "Successful Pressure %", "% of Aerials Won"])]
bar_data_2 = akanji_data[akanji_data['Statistic'].isin(["Pass Completion %", "% of dribblers tackled", "Successful Pressure %", "% of Aerials Won"])]
# print(ndicka_data)
print(bar_data_1)

x= np.arange(1,5)

f = plt.figure(facecolor="#000")

ax=plt.axes()
ax.set_facecolor("#000")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#888")
ax.spines["bottom"].set_color("#888")

ax.bar(x-0.1, height=bar_data_1["Percentile"], width=0.2, color="#004768")
ax.bar(x+0.1, height=bar_data_2["Percentile"], width=0.2, color="#c68100")

plt.yticks(np.arange(0,110,10), color="#fff")
plt.xticks(np.arange(1,5),bar_data_1["Statistic"],fontsize=8, color="#fff")

for index, value in enumerate(bar_data_1["Percentile"]):
    text = plt.text(index+1,value,str(value),color="#FFF", fontweight="bold", fontsize=5.5)
    text.set_position((index+0.809,value-5))

for index, value in enumerate(bar_data_2["Percentile"]):
    text = plt.text(index+1,value,str(value),color="#fff", fontweight="bold", fontsize=5.5)
    text.set_position((index+1.03,value-5))

# plt.xlabel("Tackles Won p90",color="#fff")
plt.ylabel("Percentile Value",color="#fff")
plt.title("Percentile comparison - N'Dicka and Akanji, 2021/22 season",color="#fff", fontsize=9)

plt.show()
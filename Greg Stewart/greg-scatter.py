import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

assist_comp_data = pd.read_excel("./greg-stewart.xlsx", "comparison-assists")
assist_comp_data = assist_comp_data[assist_comp_data['Player'].notna()]
assist_comp_data = assist_comp_data.reset_index()
assist_comp_data = assist_comp_data.drop(['index'], axis=1)
# print(assist_comp_data)

x = assist_comp_data['Chances Created p90']
y = assist_comp_data['Big Chances Created']

print(len(x))

col=[]
for i in assist_comp_data['Player']:
    if "Greg Stewart" in i:
        col.append('#de6927')
    else:
        col.append('#ccedebb3')

plt.figure(facecolor='#212121')
ax=plt.subplot(111)
ax.set_facecolor('#212121')

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#aaa")
ax.spines["bottom"].set_color("#aaa")

for i in range(len(x)):
    ax.scatter(x[i],y[i], facecolor='none', edgecolor=col[i])
    ax.annotate(assist_comp_data["Player"][i],(x[i],y[i]),color="#aaa")
plt.xticks(np.arange(1.5,4,0.5),color="#888")
plt.yticks(color="#888")
plt.xlabel("Chances Created p90", color="#888")
plt.ylabel("Big Chances Created", color="#888")
# plt.title("Chances Created p90 vs Big Chances Created : ISL 2021-22 Top 10 Assisters.", color="#aaa")
plt.show()
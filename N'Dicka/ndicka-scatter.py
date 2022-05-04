import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

scatter_data = pd.read_excel('../BuLi-general/player-defensive-actions-p90.xlsx').round(2)
# print(scatter_data)
scatter_data = scatter_data.drop(0)


scatter_data = scatter_data[scatter_data["Minutes"]>500]
scatter_data = scatter_data[scatter_data["Position"].isin(["DF", "DF,MF", "MF,DF", "DF,FW", "FW,DF"])]

# keys = np.arange(0,144,1)
# scatter_data["key"] = keys

scatter_data = scatter_data.reset_index()
scatter_data = scatter_data.drop(['index'], axis=1)

# print(scatter_data)

x = scatter_data['Tackles Won']
y = scatter_data['Succ. Tackles']

for i in range(len(x)):
    x[i] = float(x[i])
print(y.max())

# x.keys() = np.arange(0,144,1)

col=[]
for i in scatter_data['Player']:
    if "Dicka" in i:
        col.append('#3EF735')
    elif "Cristian Gamboa" in i or "Danilo Soares" in i:
        col.append('#3ef73557')
    elif "Mavropanos" in i or "Akanji" in i:
        col.append('#35f7e757')
    else:
        col.append('#333')

f = plt.figure(facecolor="#000")
f.set_figwidth(9)
f.set_figheight(6)
ax=plt.axes()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#888")
ax.spines["bottom"].set_color("#888")
ax.set_facecolor("#000")


for i in range(len(x)):
    ax.scatter(x[i],y[i],c=col[i])
    if col[i]!='#333':
        ax.annotate(scatter_data["Player"][i],(x[i],y[i]),color="#fff")
plt.yticks(np.arange(30,100,5),color="#fff")
plt.xticks(color="#fff")
plt.xticks(np.arange(0.4,3.2,0.4))
plt.xlabel("Tackles Won p90",color="#fff")
plt.ylabel("Successful Tackle % p90",color="#fff")
plt.title("Successful tackle % p90 vs Tackles won p90 - Bundesliga defenders, 2021/22 season, min 500 minutes played.",color="#fff")
plt.show()
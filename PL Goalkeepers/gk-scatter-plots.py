#This code won't work out of the box. Comment any two of 1,2,3 to run the uncommented code.

import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

gk_data = pd.read_excel('gk-data.xlsx', 'gk-data')
gk_data = gk_data[gk_data["Minutes"]>=500]
gk_data = gk_data.reset_index()
gk_data = gk_data.drop(["Index"],axis=1)
# print(gk_data)

#1.

y = gk_data['PSxG +/- p90']
x = gk_data['DAOPA p90']

color = []
for i in gk_data["Player"]:
    if i == "David de Gea":
        color.append("#DA291C")
    elif i=="José Sá":
        color.append("#FDB913")
    elif i=="Alisson":
        color.append("#C8102E")
    elif i=="Nick Pope":
        color.append("#6C1D45")
    elif i=="Karl Darlow":
        color.append("#FFFFFF")
    elif i=="Aaron Ramsdale":
        color.append("#DB0007")
    elif i=="Robert Sánchez":
        color.append("#0057B8")
    else:
        color.append("#333")



f = plt.figure(facecolor="#000")
ax = plt.axes()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#888")
ax.spines["bottom"].set_position('zero')
ax.spines["left"].set_color("#888")

ax.set_facecolor("#000")

for i in range(len(x)):
    if gk_data["Player"][i]=="Hugo Lloris":
        continue
    ax.scatter(x[i],y[i],c=color[i])
    if color[i] != "#333":
        ax.annotate(gk_data["Player"][i],(x[i],y[i]),color="#fff")

plt.xticks(color="#fff")
plt.yticks(np.arange(-0.5,0.6,0.1),color="#fff")

plt.show()

#2.

print(x)
print(y.sort_values())

y = gk_data['PSxG +/- p90']
x = gk_data['Crosses Stop %']

color = []
for i in gk_data["Player"]:
    if i == "David de Gea":
        color.append("#DA291C")
    elif i=="José Sá":
        color.append("#FDB913")
    elif i=="Alisson":
        color.append("#C8102E")
    elif i=="Nick Pope":
        color.append("#6C1D45")
    elif i=="Karl Darlow":
        color.append("#FFFFFF")
    elif i=="Aaron Ramsdale":
        color.append("#DB0007")
    elif i=="Robert Sánchez":
        color.append("#0057B8")
    else:
        color.append("#333")



f = plt.figure(facecolor="#000")
ax = plt.axes()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#888")
ax.spines["bottom"].set_position('zero')
ax.spines["left"].set_color("#888")

ax.set_facecolor("#000")

for i in range(len(x)):
    if gk_data["Player"][i]=="Hugo Lloris":
        continue
    ax.scatter(x[i],y[i],c=color[i])
    if color[i] != "#333":
        ax.annotate(gk_data["Player"][i],(x[i],y[i]),color="#fff")

plt.xticks(color="#fff")
plt.yticks(np.arange(-0.5,0.6,0.1),color="#fff")

plt.show()

# 3.

y = gk_data['Launches Cmp %']
x = gk_data['Launch %']

color = []
for i in gk_data["Player"]:
    if i == "David de Gea":
        color.append("#DA291C")
    elif i=="José Sá":
        color.append("#FDB913")
    elif i=="Alisson":
        color.append("#C8102E")
    elif i=="Nick Pope":
        color.append("#6C1D45")
    # elif i=="Karl Darlow":
    #     color.append("#FFFFFF")
    elif i=="Ederson":
        color.append("#6CABDD")
    elif i=="Robert Sánchez":
        color.append("#0057B8")
    else:
        color.append("#333")



f = plt.figure(facecolor="#000")
ax = plt.axes()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_color("#888")
ax.spines["bottom"].set_position('zero')
ax.spines["left"].set_color("#888")

ax.set_facecolor("#000")

for i in range(len(x)):
    if gk_data["Player"][i]=="Hugo Lloris":
        continue
    ax.scatter(x[i],y[i],c=color[i])
    if color[i] != "#333":
        ax.annotate(gk_data["Player"][i],(x[i],y[i]),color="#fff")
    # ax.annotate(gk_data["Player"][i],(x[i],y[i]),color="#fff")

plt.xticks(np.arange(0,110,10),color="#fff")
plt.yticks(np.arange(0,110,10),color="#fff")
plt.xlabel('Launch %',color="#fff")
plt.ylabel('Launch Cmp %',color="#fff")

plt.show()
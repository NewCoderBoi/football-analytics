#This code won't work out of the box. Comment any two of defence, possession and passing to run the uncommented code.

import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

all_data = pd.read_excel("./levitt-garner.xlsx", "Final")
# all_data = all_data[all_data.notna()]
all_data = all_data[5:]
all_data = all_data.reset_index()
all_data = all_data.drop(["index"], axis=1)
all_data.columns = all_data.iloc[0]
all_data = all_data.drop(0)
all_data = all_data[all_data["Attribute"].notna()]
all_data = all_data.reset_index()
all_data = all_data.drop(["index"], axis=1)

for i in range(len(all_data["Dylan Levitt"])):
    if all_data["Dylan Levitt"][i] == "Right":
        continue
    all_data["Dylan Levitt"][i] = round(float(all_data["Dylan Levitt"][i]),2)
    all_data["James Garner"][i] = round(float(all_data["James Garner"][i]),2)

# all_data = all_data[all_data["Dylan Levitt"]].round(2)
# print(all_data)

#Defence

levitt_data = {}
garner_data = {}

for i in range(4,6):
    levitt_data[all_data["Attribute"][i]] = all_data["Dylan Levitt"][i]
    garner_data[all_data["Attribute"][i]] = all_data["James Garner"][i]

for i in range(7,12):
    levitt_data[all_data["Attribute"][i]] = all_data["Dylan Levitt"][i]
    garner_data[all_data["Attribute"][i]] = all_data["James Garner"][i]

radar_dataframe = pd.DataFrame([levitt_data, garner_data], index=["Dylan Levitt", "James Garner"])
# print(radar_dataframe)

Attributes = list(radar_dataframe)
AttNo = len(Attributes)

values_levitt = radar_dataframe.iloc[0].tolist()
values_levitt += values_levitt[:1]
values_garner = radar_dataframe.iloc[1].tolist()
values_garner += values_garner[:1]

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

plt.figure(facecolor="#fff")
ax = plt.subplot(131, polar=True)
# ax.spines['polar'].set_color('#fff')
ax.spines['polar'].set_visible(False)

ax.set_xticks(angles[:-1], Attributes, color="#000",fontsize=7)

ax.plot(angles,values_levitt, color="#004768")
ax.plot(angles,values_garner, color="#c68100")

# ax.fill(angles, values_levitt, '#004768')
# ax.fill(angles, values_garner, '#c68100', alpha=0.5)

# ax.set_title("Levitt", color="#fff", fontsize=9)
# plt.legend()

ax2 = plt.subplot(133)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

x=np.arange(1,3)
bar_data_levitt = []
bar_data_garner = []

bar_data_levitt.append(all_data.iloc[6]["Dylan Levitt"])
bar_data_levitt.append(all_data.iloc[12]["Dylan Levitt"])

bar_data_garner.append(all_data.iloc[6]["James Garner"])
bar_data_garner.append(all_data.iloc[12]["James Garner"])

# print(bar_data_garner)

ax2.bar(x-0.1, height=bar_data_levitt, width=0.2, color="#004768", alpha=0.75)
ax2.bar(x+0.1, height=bar_data_garner, width=0.2, color="#c68100", alpha=0.75)

ax2.set_yticks(np.arange(0,90,10))

plt.show()

# Possession

levitt_data = {}
garner_data = {}

for i in range(13,19):
    levitt_data[all_data["Attribute"][i]] = all_data["Dylan Levitt"][i]
    garner_data[all_data["Attribute"][i]] = all_data["James Garner"][i]

radar_dataframe = pd.DataFrame([levitt_data, garner_data], index=["Dylan Levitt", "James Garner"])
# print(radar_dataframe)

Attributes = list(radar_dataframe)
AttNo = len(Attributes)

values_levitt = radar_dataframe.iloc[0].tolist()
values_levitt += values_levitt[:1]
values_garner = radar_dataframe.iloc[1].tolist()
values_garner += values_garner[:1]

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

plt.figure(facecolor="#fff")
ax = plt.subplot(131, polar=True)
# ax.spines['polar'].set_color('#fff')
ax.spines['polar'].set_visible(False)

ax.set_xticks(angles[:-1], Attributes, color="#000",fontsize=7)

ax.plot(angles,values_levitt, color="#004768")
ax.plot(angles,values_garner, color="#c68100")

# ax.fill(angles, values_levitt, '#004768')
# ax.fill(angles, values_garner, '#c68100', alpha=0.5)

# ax.set_title("Levitt", color="#fff", fontsize=9)
# plt.legend()

ax2 = plt.subplot(133)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

x=np.arange(1,2)
bar_data_levitt = []
bar_data_garner = []

bar_data_levitt.append(all_data.iloc[19]["Dylan Levitt"])
bar_data_garner.append(all_data.iloc[19]["James Garner"])


# print(bar_data_garner)

ax2.bar(x=1.025, height=bar_data_levitt, width=0.05, color="#004768", alpha=0.75)
ax2.bar(x=0.975, height=bar_data_garner, width=0.05, color="#c68100", alpha=0.75)

ax2.set_xticks(np.arange(0.9,1.2,0.1))
ax2.set_yticks(np.arange(0,90,10))

plt.show()

#Passing

levitt_data = {}
garner_data = {}

# for i in range(13,19):
#     levitt_data[all_data["Attribute"][i]] = all_data["Dylan Levitt"][i]
#     garner_data[all_data["Attribute"][i]] = all_data["James Garner"][i]

radar_data = all_data[all_data["Attribute"].isin(["Total Shots p90", "Long Pass Attempted p90", "Long Pass Completed p90", "Key Passes p90"])]
radar_data = radar_data.reset_index()

bar_data = all_data[all_data["Attribute"].isin(["Pass Accuracy %", "Long Pass Success %", "Short Pass Completed p90", "Short Pass Success %"])]
bar_data = bar_data.reset_index()
# print(radar_data)

for i in range(len(radar_data)):
    levitt_data[radar_data["Attribute"][i]] = radar_data["Dylan Levitt"][i]
    garner_data[radar_data["Attribute"][i]] = radar_data["James Garner"][i]

radar_dataframe = pd.DataFrame([levitt_data, garner_data], index=["Dylan Levitt", "James Garner"])
# print(radar_dataframe)

Attributes = list(radar_dataframe)
AttNo = len(Attributes)

values_levitt = radar_dataframe.iloc[0].tolist()
values_levitt += values_levitt[:1]
values_garner = radar_dataframe.iloc[1].tolist()
values_garner += values_garner[:1]

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

plt.figure(facecolor="#fff")
ax = plt.subplot(131, polar=True)
# ax.spines['polar'].set_color('#fff')
ax.spines['polar'].set_visible(False)

ax.set_xticks(angles[:-1], Attributes, color="#000",fontsize=7)

ax.plot(angles,values_levitt, color="#004768")
ax.plot(angles,values_garner, color="#c68100")

# ax.fill(angles, values_levitt, '#004768')
# ax.fill(angles, values_garner, '#c68100', alpha=0.5)

ax2 = plt.subplot(133)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

x=np.arange(1,5)
bar_data_levitt = bar_data["Dylan Levitt"]
bar_data_garner = bar_data["James Garner"]

# print(bar_data_garner)
# print(bar_data_levitt)



# print(bar_data_garner)

ax2.bar(x+0.1, height=bar_data_levitt, width=0.2, color="#004768", alpha=0.75)
ax2.bar(x-0.1, height=bar_data_garner, width=0.2, color="#c68100", alpha=0.75)

# ax2.set_xticks(np.arange(0.9,1.2,0.1))
ax2.set_yticks(np.arange(0,110,10))

plt.show()
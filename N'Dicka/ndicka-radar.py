import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

ndicka_data = pd.read_excel('./Ndicka.xlsx', 'NDicka').round(2)
ndicka_data = ndicka_data[ndicka_data['Per 90'].notna()]
ndicka_data = ndicka_data.drop_duplicates(keep='first')

akanji_data = pd.read_excel('./Ndicka.xlsx', 'Akanji').round(2)
akanji_data = akanji_data[akanji_data['Per 90'].notna()]
akanji_data = akanji_data.drop_duplicates(keep='first')


ndicka_data = ndicka_data[ndicka_data["Statistic"].isin(["Tackles Won", "Dribblers Tackled", "Successful Pressures", "Blocks", "Interceptions"])]
akanji_data = akanji_data[akanji_data["Statistic"].isin(["Tackles Won", "Dribblers Tackled", "Successful Pressures", "Blocks", "Interceptions"])]

ndicka_data = ndicka_data.reset_index()
akanji_data = akanji_data.reset_index()

# print(radar_data_ndicka)
# print(radar_data_akanji)

radar_data_ndicka = {}
radar_data_akanji = {}

for i in range(len(ndicka_data)):
    radar_data_ndicka[ndicka_data["Statistic"][i]] = ndicka_data["Percentile"][i]


for i in range(len(akanji_data)):
    radar_data_akanji[akanji_data["Statistic"][i]] = akanji_data["Percentile"][i]

radar_dataframe = pd.DataFrame([radar_data_ndicka, radar_data_akanji], index=["N'Dicka", "Akanji"])

# print(radar_data_akanji)

Attributes = list(radar_dataframe)
AttNo = len(Attributes)

values_ndicka = radar_dataframe.iloc[0].tolist()
values_ndicka += values_ndicka[:1]
values_akanji = radar_dataframe.iloc[1].tolist()
values_akanji += values_akanji[:1]

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

plt.figure(facecolor="#000")
ax = plt.subplot(111, polar=True, facecolor="#000")
ax.spines['polar'].set_color('#fff')

plt.xticks(angles[:-1], Attributes, color="#fff", fontsize=6)
plt.yticks(color="#fff")

ax.plot(angles,values_ndicka, color="#004768")
ax.plot(angles,values_akanji, color="#c68100")

ax.fill(angles, values_ndicka, '#004768', alpha=0.5)
ax.fill(angles, values_akanji, '#c68100', alpha=0.5)

ax.set_title("Percentile comparison- N'Dicka vs Akanji, Defensive Attributes", color="#fff", fontsize=9)
# plt.legend()

plt.show()
    


# Attributes_ndicka = list(radar_data_ndicka)
# print(Attributes_ndicka)
import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

vitinha_data = pd.read_excel('./Vitinha.xlsx', 'Vitinha-Concise')
clean1 = vitinha_data[vitinha_data['Unnamed: 1'].notna()]
final_vitinha_data = clean1.iloc[1:]
final_vitinha_data.round(1)

# print(final_vitinha_data.tail(10))

radar_data = {"Tackles":final_vitinha_data.iloc[5,1], "Interceptions":final_vitinha_data.iloc[8,1], "Key Passes %":final_vitinha_data.iloc[28,1], "FoulsDrawn": final_vitinha_data.iloc[16,1], "Succ.Dribbles": final_vitinha_data.iloc[18,1], "FoulsDrawn": final_vitinha_data.iloc[16,1]}
radar_dataframe = pd.DataFrame([radar_data], index=["Vitinha"])
# print(radar_dataframe)

Attributes = list(radar_dataframe)
AttNo = len(Attributes)
# print(Attributes)

values = radar_dataframe.iloc[0].tolist()
values += values[:1]

# print(values)

angles = [n / float(AttNo) * 2 * pi for n in range(AttNo)]
angles += angles [:1]

# angles = np.arange(0,7)
# angles += angles[:1]

# print(angles)
plt.figure(facecolor="#000")
ax = plt.subplot(111, polar=True, facecolor="#000")
ax.spines['polar'].set_visible(False)
# ax.set_rticks(np.arange(0,3,0.4), color="#fff")

#Add the attribute labels to our axes
plt.xticks(angles[:-1],Attributes, color="#fff")
plt.yticks(np.arange(0,3,0.4), color="#fff")

#Plot the line around the outside of the filled area, using the angles and values calculated before
ax.plot(angles,values, color="#0b0")

#Fill in the area plotted in the last line
ax.fill(angles, values, '#0b0', alpha=0.5)

#Give the plot a title and show it
ax.set_title("Vitinha p90 2021/22 All Comps.", color="#fff")
plt.show()


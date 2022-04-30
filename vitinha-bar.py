import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

vitinha_data = pd.read_excel('./Vitinha.xlsx', 'Vitinha-Concise')
clean1 = vitinha_data[vitinha_data['Unnamed: 1'].notna()]
final_vitinha_data = clean1.iloc[1:]
final_vitinha_data.round(1)
# print(final_vitinha_data)
# print(final_vitinha_data.iloc[19,1]*100)

# hist_data = {"Tackle Success %":final_vitinha_data.iloc[6,1]*100, "Aerial Duel Success %":final_vitinha_data.iloc[12,1]*100, "Dribble Success %":final_vitinha_data.iloc[19,1]*100, "Pass Accuracy":final_vitinha_data.iloc[21,1]*100}

# hist_dataframe = pd.DataFrame([hist_data], index=["Vitinha"])
# x_axis = list(hist_dataframe)
# x_axis_count = [0,1,2,3,4]
# # print(hist_dataframe) 

# plt.hist(hist_dataframe)
# plt.xticks(x_axis_count[:-1], x_axis)
# plt.show()

bar_data = final_vitinha_data[final_vitinha_data["Legend"].isin(["Tackle success %", "Aerial success %", "Dribble Success %", "Pass Accuracy"])]
bar_data_final = bar_data["Unnamed: 1"].apply(lambda x: x*100)
bar_data.drop("Unnamed: 1", axis=1, inplace=True)
bar_data["Values"] = bar_data_final
bar_data.round({"Values":1})
# print(bar_data)



f = plt.figure(facecolor="#000")
f.set_figwidth(5)
f.set_figheight(3)

# plt.bar(x= np.arange(1,5), height=bar_data["Values"], width=0.3)
# plt.yticks(np.arange(0,100,10))
# plt.xticks(np.arange(1,5),bar_data["Legend"],fontsize=8)

ax=plt.axes()
ax.set_facecolor("#000")
ax.bar(x= np.arange(1,5), height=bar_data["Values"], width=0.4, color="#0B0")
plt.yticks(np.arange(0,100,10), color="#fff")
plt.xticks(np.arange(1,5),bar_data["Legend"],fontsize=8, color="#fff")

# plt.xlim((0,4))
# plt.xticks(bar_data["Legend"])
# plt.xticks(np.arange(1,4))
# plt.ylim((0,10))
# plt.yticks(np.arange(0,100))

for index, value in enumerate(bar_data["Values"]):
    text = plt.text(index+1,value,str(value)+"%",color="#fff", fontweight="bold", fontsize=8)
    text.set_position((index+0.805,value-5))

# plt.bar_label(bar_data["Values"])

plt.show()
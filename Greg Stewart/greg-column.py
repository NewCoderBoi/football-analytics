import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

assist_comp_data = pd.read_excel("./greg-stewart.xlsx", "comparison-assists")
assist_comp_data = assist_comp_data[assist_comp_data['Player'].notna()]
assist_comp_data = assist_comp_data.sort_values('xA')
assist_comp_data = assist_comp_data.reset_index()
assist_comp_data = assist_comp_data.drop(['index'], axis=1)
# print(assist_comp_data)

plt.figure(facecolor='#212121')
ax = plt.subplot(111)
ax.set_facecolor('#212121')

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

column_chart = plt.barh(y=np.arange(0,len(assist_comp_data['Player'])), width=assist_comp_data['xA'], height=0.5, align='center', color='#01572c')
column_chart[len(assist_comp_data['Player'])-2].set_color('#6aaa96')
plt.yticks(assist_comp_data.index)
ax.set_yticklabels(assist_comp_data.Player, fontsize=8, fontweight=600, color='#aaa')
plt.xticks(np.arange(0,6.5,0.5), color='#aaa')
plt.title('Expected Assists : ISL 2021-22 Top 10 Assisters.', color='#aaa', fontsize=15)
plt.show()


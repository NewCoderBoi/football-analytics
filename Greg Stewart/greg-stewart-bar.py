import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns

goal_comp_data = pd.read_excel("./greg-stewart.xlsx", "comparison-goals")
goal_comp_data = goal_comp_data[goal_comp_data['Player'].notna()]
# print(goal_comp_data.head())

# print(goal_comp_data['xG'][1])

new_column = []
for i in range(1,len(goal_comp_data['Player'])+1):
    new_column.append(round((goal_comp_data['xGOT'][i]-goal_comp_data['xG'][i]),2))

# print(new_column)
# new_column = sorted(new_column, key=float, reverse=True)
# print(new_column)

goal_comp_data['xGOT-xG'] = new_column
# print(goal_comp_data['xGOT-xG'])

goal_comp_data = goal_comp_data.sort_values('xGOT-xG', ascending=False)
goal_comp_data = goal_comp_data.reset_index()
goal_comp_data = goal_comp_data.drop(['index'],axis=1)
# print(goal_comp_data)

plt.figure(figsize=(4,4), facecolor='#212121')

ax=plt.subplot(111)
ax.set_facecolor('#212121')

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)


bar_chart = plt.bar(x=np.arange(0,len(goal_comp_data['Player'])), height=goal_comp_data['xGOT-xG'], width=0.5, color='#01572c')
bar_chart[0].set_color('#6aaa96')
plt.xticks(goal_comp_data.index)
ax.set_xticklabels(goal_comp_data.Player, fontsize=8, rotation=20, fontweight=600, color='#aaa')
plt.yticks(np.arange(0,5,0.5), color='#aaa')
plt.title('Expected Goals on Target minus Expected Goals : ISL 2021-22 Top 10 Goalscorers.', color='#aaa', fontsize=15)

plt.show()

import numpy as np
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import PyPizza, FontManager

hendo_data = pd.read_excel('./data.xlsx', 'hendo')
sanchez_data = pd.read_excel('./data.xlsx', 'sanchez')


# all_data.columns = all_data.iloc[0]
# all_data = all_data.drop(0)

# all_data = all_data.reset_index()
# all_data = all_data.drop(["index"], axis=1)
# all_data.columns = all_data.iloc[0]
# all_data = all_data.drop(0)

hendo_data = hendo_data[hendo_data['Per 90'].notna()]
hendo_data.round(1)
hendo_data = hendo_data.reset_index()
hendo_data = hendo_data.drop(["index"], axis=1)

sanchez_data = sanchez_data[sanchez_data['Per 90'].notna()]
sanchez_data.round(1)
sanchez_data = sanchez_data.reset_index()
sanchez_data = sanchez_data.drop(["index"], axis=1)

# print(hendo_data)
# print(sanchez_data.head(25))

# print(final_vitinha_data.tail(10))

font_normal = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Regular.ttf?raw=true"))
font_italic = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Italic.ttf?raw=true"))
font_bold = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                         "Roboto-Medium.ttf?raw=true"))

#Parameters in graph
params = [
    "PSxG-GA", "Comp. Passes(Launch)", "Pass Comp.%(Launch)", "Att.Passes ",
    "Avg Pass Length", "Avg.GoalKickLength", "Crosses Faced", "Cross Stop %",
    "Def.Act.Out.Pen.Area", "Avg. Dist. Def. Actions"
]


indices = [21,22,24,25,28,31,32,34,35,36]
final_hendo_data = []
final_sanchez_data = []

for i in indices:
    final_hendo_data.append(hendo_data["Per 90"][i])
    final_sanchez_data.append(sanchez_data["Per 90"][i])

# print(final_hendo_data)
# print(final_sanchez_data)

min_range = [0,   0,  0,   0,  0,  0,  0,  0,  0, 0]
max_range = [0.5, 10, 100, 50, 80, 80, 10, 30, 1, 15]

params_offset = [
    False, False, True, False, False,
    False, True, True, False, True
]

# instantiate PyPizza class
baker = PyPizza(
    params=params,
    min_range=min_range,        # min range values
    max_range=max_range,        # max range values
    background_color="#222222", straight_line_color="#000000",
    last_circle_color="#000000", last_circle_lw=2.5, other_circle_lw=0,
    other_circle_color="#000000", straight_line_lw=1
)

# plot pizza
fig, ax = baker.make_pizza(
    final_hendo_data,                     # list of values
    compare_values=final_sanchez_data,    # passing comparison values
    figsize=(8, 8),             # adjust figsize according to your need
    color_blank_space="same",   # use same color to fill blank space
    blank_alpha=0.4,            # alpha for blank-space colors
    param_location=110,         # where the parameters will be added
    kwargs_slices=dict(
        facecolor="#ff4d4d", edgecolor="#000000",
        zorder=1, linewidth=1
    ),                          # values to be used when plotting slices
    kwargs_compare=dict(
        facecolor="#4d79ff", edgecolor="#222222", zorder=3, linewidth=1,
    ),                          # values to be used when plotting comparison slices
    kwargs_params=dict(
        color="#F2F2F2", fontsize=12, zorder=5,
        fontproperties=font_normal.prop, va="center"
    ),                          # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#ff4d4d",
            boxstyle="round,pad=0.2", lw=1
        )
    ),                           # values to be used when adding parameter-values
    kwargs_compare_values=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#4d79ff",
            boxstyle="round,pad=0.2", lw=1
        )
    )                            # values to be used when adding comparison-values
)

# adjust the texts
# to adjust text for comparison-values-text pass adj_comp_values=True
baker.adjust_texts(params_offset, offset=-0.25)

# add title
# fig.text(
#     0.515, 0.99, "<Alexia Putellas> vs <League Average>",
#     size=16,
#     highlight_textprops=[{"color": '#1A78CF'}, {"color": '#FF9300'}],
#     ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
# )

# add subtitle
# fig.text(
#     0.515, 0.942,
#     "Hendo Season 19/20 | Sanchez Season 21/22",
#     size=15,
#     ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
# )

# add credits
CREDIT_1 = "data: statsbomb viz fbref"
CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"
CREDIT_3 = "Made by - Debatra Chatterjee, @dbchatterjee"

fig.text(
    0.70, 0.005, f"{CREDIT_3}\n{CREDIT_1}\n{CREDIT_2}", size=9,
    fontproperties=font_italic.prop, color="#F2F2F2",
    ha="right"
)

plt.show()
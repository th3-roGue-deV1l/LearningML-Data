import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('data.csv')

# 2
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']]

    # 6
    df_cat = df_cat.melt(id_vars='cardio', var_name='variable', value_name='value')

    # 7
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=6, aspect=1.2, palette='muted')
    fig.set_axis_labels('variable', 'total')
    fig.set_titles('cardio = {col_name}')
    fig._legend.set_title('value')

    # 8
    # plt.show()    

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # print(df_heat.head(5))

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14

    # 15
    plt.figure(figsize=(10, 8))
    fig = sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5, annot_kws={"size": 10})

    # plt.show()


    # 16
    plt.savefig('heatmap.png')
    return fig

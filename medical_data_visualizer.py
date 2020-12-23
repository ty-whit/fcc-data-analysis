import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height']/100)**2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat_groups = df_cat.groupby(['cardio','variable','value']).size().to_frame(name='total')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat,kind='count',x='variable',hue='value',col='cardio',)
    fig.axes[0,0].set_ylabel('total')
    fig.axes[0,1].set_ylabel('total')

    # Do not modify the next two lines
    #print('saving plot')
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # remove bad blood pressure readings
    cond1 = df['ap_lo']<=df['ap_hi']
    # Only keep height between 2.5% - 97.5%
    cond2 = df['height'] >= df['height'].quantile(0.025)
    cond3 = df['height'] <= df['height'].quantile(0.975)
    # Only keep weight between 2.5% - 97.5%
    cond4 = df['weight'] >= df['weight'].quantile(0.025)
    cond5 = df['weight'] <= df['weight'].quantile(0.975)
    cond  = cond1 & cond2 & cond3 & cond4 & cond5
    
    df_heat = df[cond]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    cond = np.triu(np.ones([14,14]))
    cond = (cond == 1)
    mask = corr.mask(cond)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))
 
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(mask, annot=True, fmt='.1f', square=True, linewidth=1, linecolor='white')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

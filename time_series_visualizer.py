import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig2 = plt.subplots(1)
    fig2 = sns.lineplot(data=df)
    fig2.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig2.set_xlabel('Date')
    fig2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig2.figure.savefig('line_plot.png')
    return fig2


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = data.plot('Year', 'CSIRO Adjusted Sea Level', kind='scatter')

    # Create first line of best fit
    best_fit1 = linregress(data[['Year', 'CSIRO Adjusted Sea Level']])
    plt.plot(range(data['Year'].min(), 2050), best_fit1.intercept + best_fit1.slope*range(data['Year'].min(), 2050), label='Best fit line from 1880', color='red')

    # Create second line of best fit
    best_fit2 = linregress((data.loc[data['Year']>=2000])[['Year', 'CSIRO Adjusted Sea Level']])
    plt.plot(range(2000, 2050), best_fit2.intercept + best_fit2.slope*range(2000, 2050), label='Best fit line from 2000', color='black')

    # Add labels and title
    fig.set_xlim(1850, 2075)
    fig.set_ylim(-2, 20)
    fig.legend(loc='upper left')
    fig.set_title('Rise in Sea Level')
    fig.set_xlabel('Year')
    fig.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

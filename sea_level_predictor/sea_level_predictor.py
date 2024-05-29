import pandas as pd
import matplotlib.pyplot as plt
import math, copy
import numpy as np
from scipy.stats import linregress

def f(w, x, b):
    return w * x + b

def draw_plot():
    # Read data from file
    df = pd.read_csv('data.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label = 'Scatter Plot of the given data')

    # Create first line of best fit
    w_init = 0
    b_init = 0

    iterations = 10000
    tmp_alpha = 0.00000001

    # Perform linear regression
    w, b, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x = np.linspace(1880, 2050, 1000)
    y = f(w, x, b)
    plt.plot(x, y, color='green', label = 'Best Fit Line')

    plt.legend()

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    w1, b1, r, p, st = linregress (df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x = np.linspace(2000, 2050, 1000)
    y = f(w1, x, b1)
    plt.plot(x, y, color = 'red', label = 'Best Fit Line since 2000')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    # plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

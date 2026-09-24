import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    first_fit = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    first_years = pd.Series(range(1880, 2051))
    first_line = first_fit.slope * first_years + first_fit.intercept
    plt.plot(first_years, first_line)


    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    second_fit = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    second_years = pd.Series(range(2000, 2051))
    second_line = second_fit.slope * second_years + second_fit.intercept
    plt.plot(second_years, second_line)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
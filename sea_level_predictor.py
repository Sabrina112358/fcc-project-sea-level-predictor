import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Draw scatter plot
    colors = np.random.uniform(15, 80, len(x))
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x, y, c=colors, vmin=0, vmax=100)

    # Create first line of best fit
    lin = linregress(x, y)
  
    ax = plt.plot(np.arange(1880, 2051), lin.intercept + lin.slope*np.arange(1880, 2051), 'g', label= 'First line of best fit')
     
    # Create second line of best fit from year 2000-2050
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    lin_2 = linregress(x_2000, y_2000)    
  
    ax=plt.plot(np.arange(2000,2051), lin_2.slope*np.arange(2000,2051) + lin_2.intercept, label= 'Second line of best fit')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
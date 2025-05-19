import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
df = df[df['value']>=df['value'].quantile(0.025)]
df = df[df['value']<=df['value'].quantile(0.975)]
df['date'] = pd.to_datetime(df['date'])

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(12, 5)) 
    fig = sns.lineplot(data=df, x='date', y='value',palette='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')



    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    df_bar['Years'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar['Months'] = df_bar['date'].dt.strftime('%B')

    monthly_avg = df_bar.groupby(['Years', 'Months'])['value'].mean().reset_index()
    # Draw bar plot


    print(monthly_avg)
    plt.clf()
    plt.figure(figsize=(7, 5)) 
    fig = sns.barplot(data=monthly_avg,x='Years',y='value',hue='Months',palette='rainbow',hue_order=['January','February','March','April','May','June','July','August','September','October','November','December'])
    plt.ylabel('Average Page Views')
    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
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

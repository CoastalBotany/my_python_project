import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#Loading raw data
df_original = pd.read_csv('vehicles_us.csv')

# Summarized data (already in your app.py)
data = {
    'condition': ['excellent', 'fair', 'good', 'like new', 'new', 'salvage'],
    'mean_price': [12806.669842, 3386.502178, 10877.439067, 16677.445593, 26050.380699, 4242.295552],
    'mean_days_listed': [39.611714, 39.118223, 39.631323, 39.166807, 37.111888, 39.008696],
    'std_price': [571.617451, 4308.814660, 9533.312223, 12154.650272, 21028.831965, 4666.620046],
    'std_days_listed': [28.260449, 27.428377, 28.239384, 28.350925, 26.339138, 28.801576],
    'median_price': [10495.0, 2500.0, 7900.0, 13995.0, 21999.0, 2500.0],
    'median_days_listed': [36.0, 39.0, 39.0, 38.0, 35.0, 33.0]
}

stats_df = pd.DataFrame(data)

#Creating the Streamlit dashboard
st.header("Vehicle Price and Listing Duration Dashboard")

#Adding a checkbox to toggle between mean and median values
use_median = st.checkbox("Use Median Values Instead of Mean", value=False)

#Creating the scatter plot
if use_median:
    #Plotting using median values
    fig = px.scatter(
        stats_df,
        x='median_days_listed',
        y='median_price',
        color='condition',
        size='std_price',
        hover_data=['condition', 'mean_price', 'mean_days_listed', 'std_price', 'std_days_listed', 'median_price', 'median_days_listed'],
        title='Median Price vs Median Days Listed by Condition (Size by Std of Price)',
        labels={'median_days_listed': 'Median Days Listed', 'median_price': 'Median Price'}
    )
else:
    #Plotting using mean values
    fig = px.scatter(
        stats_df,
        x='mean_days_listed',
        y='mean_price',
        color='condition',
        size='std_price',
        hover_data=['condition', 'mean_price', 'mean_days_listed', 'std_price', 'std_days_listed', 'median_price', 'median_days_listed'],
        title='Mean Price vs Mean Days Listed by Condition (Size by Std of Price)',
        labels={'mean_days_listed': 'Mean Days Listed', 'mean_price': 'Mean Price'}
    )

#Displaying scatter plot
st.plotly_chart(fig)

#Adding histogram of vehicle prices by condition
st.header("Distribution of Vehicle Prices by Condition")
if use_median:
    fig_hist_price = px.histogram(
        stats_df,
        x='median_price',
        color='condition',
        title='Histogram of Median Prices by Condition',
        labels={'median_price': 'Median Price', 'condition': 'Condition'},
        nbins=10
    )
else:
    fig_hist_price = px.histogram(
        stats_df,
        x='mean_price',
        color='condition',
        title='Histogram of Mean Prices by Condition',
        labels={'mean_price': 'Mean Price', 'condition': 'Condition'},
        nbins=10
    )

#Displaying the price histogram
st.plotly_chart(fig_hist_price)

# Adding histogram of odometer readings with mean and median lines
st.header("Distribution of Odometer Readings")
fig_hist_odometer = px.histogram(
    df_original,
    x='odometer',
    title='Distribution of Odometer Readings',
    nbins=30,
    opacity=0.7
)

# Calculate mean and median odometer values
mean_odometer = df_original['odometer'].mean()
median_odometer = df_original['odometer'].median()

# Add vertical lines for mean and median
fig_hist_odometer.add_vline(
    x=mean_odometer,
    line_dash="dash",
    line_color="red",
    annotation_text="Mean",
    annotation_position="top left"
)
fig_hist_odometer.add_vline(
    x=median_odometer,
    line_dash="dash",
    line_color="green",
    annotation_text="Median",
    annotation_position="top left"
)

# Display the odometer histogram
st.plotly_chart(fig_hist_odometer)
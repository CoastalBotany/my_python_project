import streamlit as st
import pandas as pd
import plotly.express as px

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

#Adding a header
st.header("Vehicle Price and Listing Duration Dashboard")

#Adding a checkbox to toggle between mean and median values.
use_median = st.checkbox("Use Median Values Instead of Mean", value=False)

#Creating Scatter Plot.
if use_median:
    #Ploting using median values.
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
    #Ploting using mean values.
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

#Displaying the scatter plot.
st.plotly_chart(fig)
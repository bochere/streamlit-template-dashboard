import streamlit as st
import plotly.express as px
import pandas as pd

# Sample World Cup data (you can replace this with your CSV)
data = pd.DataFrame({
    'Team': ['Brazil', 'Germany', 'Argentina', 'France', 'Spain'],
    'Goals': [12, 9, 7, 8, 6]
})

# Custom colors for each team
colors = ['#FFD700', '#FF5733', '#33FF57', '#3357FF', '#FF33A8']

# Create pie chart
fig = px.pie(
    data, 
    names='Team', 
    values='Goals', 
    title='World Cup Goals by Team',
    color='Team',
    color_discrete_sequence=colors
)

# Add some styling
fig.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05, 0, 0, 0, 0])

# Display in Streamlit
st.plotly_chart(fig)


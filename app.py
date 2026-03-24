import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = pd.DataFrame({
    'Team': ['Brazil', 'Germany', 'Argentina', 'France', 'Spain'],
    'Goals': [12, 9, 7, 8, 6],
    'Matches': [5, 4, 5, 4, 4]
})

# Page configuration
st.set_page_config(page_title="World Cup Dashboard", layout="wide")

# --- Banner ---
st.markdown(
    """
    <div style="background-color:#4B8BBE; padding: 20px; border-radius:10px">
        <h1 style="color:white; text-align:center;">⚽ World Cup Dashboard</h1>
    </div>
    """, unsafe_allow_html=True
)

# Sidebar filter
teams = st.sidebar.multiselect("Select Teams", options=data['Team'], default=data['Team'])
filtered_data = data[data['Team'].isin(teams)]

# --- KPIs in card style ---
total_goals = filtered_data['Goals'].sum()
total_matches = filtered_data['Matches'].sum()
avg_goals_per_match = round(total_goals / total_matches, 2) if total_matches > 0 else 0

st.markdown("<br>", unsafe_allow_html=True)  # spacing

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.markdown(
        f"""
        <div style="background-color:#FFD700; padding:20px; border-radius:10px; text-align:center">
            <h3>Total Goals</h3>
            <h2>{total_goals}</h2>
        </div>
        """, unsafe_allow_html=True
    )

with kpi_col2:
    st.markdown(
        f"""
        <div style="background-color:#FF5733; padding:20px; border-radius:10px; text-align:center">
            <h3>Total Matches</h3>
            <h2>{total_matches}</h2>
        </div>
        """, unsafe_allow_html=True
    )

with kpi_col3:
    st.markdown(
        f"""
        <div style="background-color:#33FF57; padding:20px; border-radius:10px; text-align:center">
            <h3>Avg Goals/Match</h3>
            <h2>{avg_goals_per_match}</h2>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)  # spacing

# Colors for charts
colors = ['#FFD700', '#FF5733', '#33FF57', '#3357FF', '#FF33A8']

# --- Charts Layout ---
chart_col1, chart_col2 = st.columns([1, 1])

with chart_col1:
    st.markdown(
        '<div style="background-color:#E8F6F3; padding:10px; border-radius:10px">',
        unsafe_allow_html=True
    )
    st.subheader("Goals Distribution")
    pie_fig = px.pie(
        filtered_data,
        names='Team',
        values='Goals',
        color='Team',
        color_discrete_sequence=colors,
        title='Goals by Team'
    )
    pie_fig.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05]*len(filtered_data))
    st.plotly_chart(pie_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with chart_col2:
    st.markdown(
        '<div style="background-color:#E8F6F3; padding:10px; border-radius:10px">',
        unsafe_allow_html=True
    )
    st.subheader("Matches Played")
    bar_fig = px.bar(
        filtered_data,
        x='Team',
        y='Matches',
        color='Team',
        color_discrete_sequence=colors,
        title='Matches Played by Team'
    )
    bar_fig.update_layout(yaxis_title="Matches", xaxis_title="Team")
    st.plotly_chart(bar_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Table in colored section ---
st.markdown(
    '<div style="background-color:#F5F5F5; padding:15px; border-radius:10px">',
    unsafe_allow_html=True
)
st.subheader("Team Stats Table")
st.dataframe(filtered_data.style.background_gradient(cmap='YlGnBu'))
st.markdown('</div>', unsafe_allow_html=True)

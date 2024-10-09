import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title('Interactive Data Visualization Dashboard')

# Description
st.write("Use the interactive controls below to explore the data.")

# Generate some example data
df = pd.DataFrame({
    'x': range(10),
    'y': [x**2 for x in range(10)],
    'z': [x**3 for x in range(10)]
})

# Add an interactive slider to control the range of x values
x_range = st.slider('Select X-axis Range', min_value=0, max_value=9, value=(0, 9))

# Filter data based on the selected x_range
filtered_df = df[(df['x'] >= x_range[0]) & (df['x'] <= x_range[1])]

# Add a selectbox to choose between different plots
plot_type = st.selectbox('Choose plot type', ['Line Plot', 'Bar Plot', 'Scatter Plot'])

# Display the selected plot
if plot_type == 'Line Plot':
    st.line_chart(filtered_df[['x', 'y']])
elif plot_type == 'Bar Plot':
    st.bar_chart(filtered_df[['x', 'y']])
else:
    st.write("Scatter Plot:")
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['x'], filtered_df['y'], color='r', label='y = x^2')
    ax.scatter(filtered_df['x'], filtered_df['z'], color='b', label='z = x^3')
    ax.set_xlabel('x')
    ax.set_ylabel('y / z')
    ax.legend()
    st.pyplot(fig)

# Add interactivity: Checkbox to show data table
if st.checkbox('Show Data Table'):
    st.write(filtered_df)

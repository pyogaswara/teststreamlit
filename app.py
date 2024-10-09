import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load some example data
df = pd.DataFrame({
    'x': range(10),
    'y': [x ** 2 for x in range(10)]
})

# Streamlit title and description
st.title('Simple Data Visualization')
st.write('This is an example dashboard using Streamlit.')

# Interactive chart
st.line_chart(df)

# Custom plot with Matplotlib
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'], label='y = x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Display the Matplotlib chart
st.pyplot(fig)

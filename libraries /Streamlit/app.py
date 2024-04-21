import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.title('Simple Streamlit App')

# Add a slider widget
x = st.slider('Select a value', 0.0, 10.0, 5.0)

# Generate some data based on the slider value
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values * x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plot of sin(x * selected_value)')
st.pyplot(fig)

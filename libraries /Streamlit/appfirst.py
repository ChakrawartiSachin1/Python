import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt

# Set page title
st.title('Text Analysis App')

# Add a text input widget
text_input = st.text_area('Enter some text:', height=200)

# Perform word count analysis
if text_input:
    # Tokenize the input text
    words = text_input.split()
    
    # Calculate word frequency
    word_freq = Counter(words)
    
    # Display word frequency table
    st.write('### Word Frequency:')
    st.write(word_freq)
    
    # Plot word frequency distribution
    st.write('### Word Frequency Distribution:')
    plt.figure(figsize=(10, 6))
    plt.bar(word_freq.keys(), word_freq.values())
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    st.pyplot(plt)

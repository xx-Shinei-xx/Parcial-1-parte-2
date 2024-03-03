import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import binom

def plot_binomial_distribution(n, p):
    # Generate the values of k for the x-axis
    k_values = range(n+1)
    
    # Calculate the probabilities for each k
    probabilities = binom.pmf(k_values, n, p)
    
    # Plot the binomial distribution
    fig, ax = plt.subplots()
    ax.bar(k_values, probabilities, color='skyblue', label='Binomial Distribution')
    
    # Overlay a line plot for better visualization
    ax.plot(k_values, probabilities, color='red', linestyle='-', linewidth=2, marker='o', label='Line Marking Blocks')
    
    ax.set_title('Binomial Distribution with Line Marking Blocks')
    ax.set_xlabel('Number of Successes (k)')
    ax.set_ylabel('Probability')
    ax.set_xticks(k_values)
    ax.grid(True)
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title('Binomial Distribution Plot')

    # Sidebar for user input
    with st.sidebar:
        st.header('User Input')
        n = st.slider('Value of n (less than 100)', 1, 100, 1)
        p = st.slider('Value of p (between 0 and 1)', 0.0, 1.0, 0.5)

    plot_binomial_distribution(n, p)

if __name__ == "__main__":
    main()

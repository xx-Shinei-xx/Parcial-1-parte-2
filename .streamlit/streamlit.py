import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
 
# Function to calculate binomial distribution and plot
def plot_binomial_distribution(n, p):
    # Generate values for x-axis (number of successes)
    x = np.arange(0, n+1)
    # Calculate binomial distribution
    y = np.array([np.math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in x])
    # Plot the binomial distribution
    plt.bar(x, y)
    plt.title('Binomial Distribution')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    st.pyplot()

# Streamlit interface
def main():
    st.title('Binomial Distribution Plotter')
    st.write("This application allows you to plot the binomial distribution based on the parameters n and p.")

    # User input for n and p
    n = st.number_input("Enter the value of n (number of trials)", min_value=1, max_value=100, value=1, step=1)
    p = st.number_input("Enter the value of p (probability of success)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Plot Distribution"):
        if p > 1:
            st.error("Error: The probability p cannot be greater than 1.")
        else:
            plot_binomial_distribution(int(n), p)

if __name__ == "__main__":
    main()

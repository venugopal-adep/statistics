import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.weightstats import ztest

def generate_data(n, mean, std):
    return np.random.normal(mean, std, n)

def perform_t_test(sample1, sample2):
    statistic, pvalue = stats.ttest_ind(sample1, sample2)
    return statistic, pvalue

def perform_z_test(sample1, sample2):
    statistic, pvalue = ztest(sample1, sample2)
    return statistic, pvalue

def plot_data(sample1, sample2):
    plt.figure(figsize=(10, 5))
    plt.hist(sample1, bins=30, alpha=0.5, label='Sample 1')
    plt.hist(sample2, bins=30, alpha=0.5, label='Sample 2')
    plt.legend(loc='upper right')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of Samples')
    plt.grid(True)
    return plt

def main():
    st.title('Hypothesis Testing Playground')

    with st.sidebar:
        st.header('Generate Data')
        n = st.number_input('Sample Size', min_value=10, value=100, step=10)
        mean1 = st.number_input('Mean for Sample 1', value=0.0)
        std1 = st.number_input('Standard Deviation for Sample 1', value=1.0, step=0.1)
        mean2 = st.number_input('Mean for Sample 2', value=0.5)
        std2 = st.number_input('Standard Deviation for Sample 2', value=1.0, step=0.1)
        if st.button('Generate Samples'):
            sample1 = generate_data(n, mean1, std1)
            sample2 = generate_data(n, mean2, std2)
            st.session_state.sample1 = sample1
            st.session_state.sample2 = sample2
    
    if 'sample1' in st.session_state and 'sample2' in st.session_state:
        st.subheader('Visualize Data Distribution')
        fig = plot_data(st.session_state.sample1, st.session_state.sample2)
        st.pyplot(fig)

        st.subheader('Perform Hypothesis Test')
        test_type = st.selectbox('Select Test Type', ['t-test', 'z-test'])
        if test_type == 't-test':
            statistic, pvalue = perform_t_test(st.session_state.sample1, st.session_state.sample2)
            st.write(f"T-statistic: {statistic:.2f}")
            st.write(f"P-value: {pvalue:.4f}")
        elif test_type == 'z-test':
            statistic, pvalue = perform_z_test(st.session_state.sample1, st.session_state.sample2)
            st.write(f"Z-statistic: {statistic:.2f}")
            st.write(f"P-value: {pvalue:.4f}")

        if pvalue < 0.05:
            st.success("Reject the null hypothesis (p < 0.05)")
        else:
            st.error("Fail to reject the null hypothesis (p >= 0.05)")

if __name__ == '__main__':
    main()

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.preprocessing import StandardScaler
from scipy.stats import gaussian_kde

def generate_data():
    np.random.seed(None)  # Set the seed to None for different data each time
    x = np.random.randint(0, 100, 100)
    y = np.random.randint(0, 100, 100)
    return pd.DataFrame({'x': x, 'y': y})

def normalize_data(data):
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=['x', 'y'])

def plot_data(original_data, normalized_data):
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Original Data", "Original Distribution",
                                                        "Normalized Data", "Normalized Distribution"),
                        column_widths=[0.7, 0.3])

    fig.add_trace(go.Scatter(x=original_data['x'], y=original_data['y'], mode='markers'), row=1, col=1)

    x_kde = gaussian_kde(original_data['x'])
    x_range = np.linspace(original_data['x'].min(), original_data['x'].max(), 200)
    y_kde = gaussian_kde(original_data['y'])
    y_range = np.linspace(original_data['y'].min(), original_data['y'].max(), 200)

    fig.add_trace(go.Scatter(x=x_range, y=x_kde(x_range), mode='lines', name='X', line=dict(color='#1f77b4')), row=1, col=2)
    fig.add_trace(go.Scatter(x=y_range, y=y_kde(y_range), mode='lines', name='Y', line=dict(color='#ff7f0e')), row=1, col=2)

    fig.update_xaxes(title_text="Value", row=1, col=2)
    fig.update_yaxes(title_text="Density", range=[0, 1], row=1, col=2)

    fig.add_annotation(x=1.05, y=0.95, xref='paper', yref='paper', showarrow=False, align='left', xanchor='left',
                       text=f"X Mean: {original_data['x'].mean():.2f}<br>X Std: {original_data['x'].std():.2f}<br>Y Mean: {original_data['y'].mean():.2f}<br>Y Std: {original_data['y'].std():.2f}",
                       row=1, col=2)

    fig.add_trace(go.Scatter(x=normalized_data['x'], y=normalized_data['y'], mode='markers'), row=2, col=1)

    x_kde_norm = gaussian_kde(normalized_data['x'])
    x_range_norm = np.linspace(normalized_data['x'].min(), normalized_data['x'].max(), 200)
    y_kde_norm = gaussian_kde(normalized_data['y'])
    y_range_norm = np.linspace(normalized_data['y'].min(), normalized_data['y'].max(), 200)

    fig.add_trace(go.Scatter(x=x_range_norm, y=x_kde_norm(x_range_norm), mode='lines', name='X', line=dict(color='#1f77b4')), row=2, col=2)
    fig.add_trace(go.Scatter(x=y_range_norm, y=y_kde_norm(y_range_norm), mode='lines', name='Y', line=dict(color='#ff7f0e')), row=2, col=2)

    fig.update_xaxes(title_text="Normalized Value", row=2, col=2)
    fig.update_yaxes(title_text="Density", row=2, col=2)

    fig.add_annotation(x=1.05, y=0.95, xref='paper', yref='paper', showarrow=False, align='left', xanchor='left',
                       text=f"X Mean: {normalized_data['x'].mean():.2f}<br>X Std: {normalized_data['x'].std():.2f}<br>Y Mean: {normalized_data['y'].mean():.2f}<br>Y Std: {normalized_data['y'].std():.2f}",
                       row=2, col=2)

    fig.update_layout(height=800, width=800, title_text="Data Visualization")
    st.plotly_chart(fig)

def main():
    st.title('Standard Normalization Demo')
    st.write('This app demonstrates the concept of standard normalization in machine learning.')
    st.write('Standard Normalization Formula:')
    st.latex(r'z = \frac{x - \mu}{\sigma}')
    st.write('where:')
    st.write('- z is the normalized value')
    st.write('- x is the original value')
    st.write('- μ is the mean of the feature')
    st.write('- σ is the standard deviation of the feature')

    data = generate_data()

    if st.checkbox('Show original data'):
        st.write(data)

    normalized_data = normalize_data(data)

    if st.checkbox('Show normalized data'):
        st.write(normalized_data)

    if st.button('Visualize Data'):
        plot_data(data, normalized_data)

    st.write('Standard normalization is a technique used to standardize the features of a dataset. It transforms the data to have a mean of 0 and a standard deviation of 1. This helps in scaling the features to a similar range, which is beneficial for many machine learning algorithms.')

    st.write('In this demo, we generate a random dataset with two features (x and y) and apply standard normalization to it. The original data points are plotted on the first scatter plot, and the normalized data points are plotted on the second scatter plot. The distribution of each feature is shown on the right side of the corresponding scatter plot using Kernel Density Estimation (KDE).')

    st.write('Observe how the normalized data points are centered around 0 and have a similar scale on both axes. This is the effect of standard normalization, which helps in treating all features with equal importance and can improve the performance of certain machine learning algorithms.')

if __name__ == '__main__':
    main()
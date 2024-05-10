import streamlit as st
import plotly.graph_objects as go
import numpy as np

def calculate_distance(p1, p2, metric):
    if metric == 'Euclidean':
        return np.linalg.norm(p1 - p2), "√((x2 - x1)² + (y2 - y1)²)", "Commonly used in geometry, physics, and machine learning (e.g., k-NN)."
    elif metric == 'Manhattan':
        return np.sum(np.abs(p1 - p2)), "|x2 - x1| + |y2 - y1|", "Often used in urban planning, chess (king's moves), and taxicab geometry."
    elif metric == 'Chebyshev':
        return np.max(np.abs(p1 - p2)), "max(|x2 - x1|, |y2 - y1|)", "Used in chess (queen's moves), warehouse logistics, and infinite norm applications."

def main():
    st.sidebar.title("Settings")
    x1 = st.sidebar.slider("X coordinate of Point 1", -10, 10, 0)
    y1 = st.sidebar.slider("Y coordinate of Point 1", -10, 10, 0)
    x2 = st.sidebar.slider("X coordinate of Point 2", -10, 10, 5)
    y2 = st.sidebar.slider("Y coordinate of Point 2", -10, 10, 5)
    metric = st.sidebar.selectbox("Select Distance Metric", ['Euclidean', 'Manhattan', 'Chebyshev'])

    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    distance, formula, application = calculate_distance(p1, p2, metric)

    st.title("Distance Metrics Visualization")
    st.write(f"The **{metric} Distance** between points is: **{distance:.2f}**")
    st.write(f"**Formula:** {formula}")
    st.write(f"**Applications:** {application}")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[x1, x2], y=[y1, y2], mode='markers', name='Points',
                             marker=dict(color=['red', 'blue'], size=12)))
    fig.add_trace(go.Scatter(x=[x1, x2], y=[y1, y2], mode='lines', name='Line'))

    fig.update_layout(title=f"{metric} Distance: {distance:.2f}",
                      xaxis_title="X Coordinate",
                      yaxis_title="Y Coordinate",
                      showlegend=False)
    
    fig.update_xaxes(showgrid=True, zeroline=True, gridwidth=1, gridcolor='LightPink')
    fig.update_yaxes(showgrid=True, zeroline=True, gridwidth=1, gridcolor='LightBlue')

    if metric == 'Manhattan':
        fig.add_shape(type="line", x0=x1, y0=y1, x1=x1, y1=y2, line=dict(color="green", width=2, dash="dashdot"))
        fig.add_shape(type="line", x0=x1, y0=y2, x1=x2, y1=y2, line=dict(color="green", width=2, dash="dashdot"))

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

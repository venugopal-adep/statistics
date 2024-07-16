import streamlit as st
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from sklearn.datasets import make_blobs

# Set page config
st.set_page_config(layout="wide", page_title="Interactive Distance Metrics Explorer", page_icon="🌠")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 42px !important;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px #cccccc;
    }
    .tab-subheader {
        font-size: 28px !important;
        font-weight: bold;
        color: #8A2BE2;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .content-text {
        font-size: 18px !important;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #9370DB;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #8A2BE2;
        transform: scale(1.05);
    }
    .highlight {
        background-color: #E6E6FA;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-header'>🌠 Interactive Distance Metrics Explorer 🌠</h1>", unsafe_allow_html=True)

# Function to calculate distance
def calculate_distance(p1, p2, metric):
    if metric == 'Euclidean':
        return np.linalg.norm(p1 - p2), "√(Σ(x_i - y_i)²)"
    elif metric == 'Manhattan':
        return np.sum(np.abs(p1 - p2)), "Σ|x_i - y_i|"
    elif metric == 'Chebyshev':
        return np.max(np.abs(p1 - p2)), "max(|x_i - y_i|)"

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎨 3D Visualization", "🔢 Interactive Calculator", "🌐 Real-world Examples", "🧠 Quiz"])

with tab1:
    st.markdown("<h2 class='tab-subheader'>3D Distance Metrics Visualization</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("<p class='content-text'>Explore distances in 3D space!</p>", unsafe_allow_html=True)
        
        x1 = st.slider("Point 1 - X Coordinate", -5.0, 5.0, 0.0, 0.1)
        y1 = st.slider("Point 1 - Y Coordinate", -5.0, 5.0, 0.0, 0.1)
        z1 = st.slider("Point 1 - Z Coordinate", -5.0, 5.0, 0.0, 0.1)
        
        x2 = st.slider("Point 2 - X Coordinate", -5.0, 5.0, 3.0, 0.1)
        y2 = st.slider("Point 2 - Y Coordinate", -5.0, 5.0, 4.0, 0.1)
        z2 = st.slider("Point 2 - Z Coordinate", -5.0, 5.0, 0.0, 0.1)
        
        metric = st.selectbox("Select Distance Metric", ['Euclidean', 'Manhattan', 'Chebyshev'], key='3d_metric')
        
        p1 = np.array([x1, y1, z1])
        p2 = np.array([x2, y2, z2])
        distance, formula = calculate_distance(p1, p2, metric)
        
        st.markdown("<div class='highlight'>", unsafe_allow_html=True)
        st.write(f"The **{metric} Distance** between points is: **{distance:.2f}**")
        st.write(f"**Formula:** {formula}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<p class='content-text'><b>Layman's Explanation:</b></p>", unsafe_allow_html=True)
        if metric == 'Euclidean':
            st.write("Imagine a straight line connecting two points in space. That's Euclidean distance!")
            st.write("Example: The direct flight path between two cities.")
        elif metric == 'Manhattan':
            st.write("Picture walking along city blocks, where you can only move along straight lines. That's Manhattan distance!")
            st.write("Example: The distance a taxi travels in a grid-like city.")
        else:
            st.write("Think of the longest step you need to take in any direction. That's Chebyshev distance!")
            st.write("Example: The number of moves a king needs in chess to reach another square.")
        
    with col2:
        fig = go.Figure(data=[
            go.Scatter3d(x=[x1, x2], y=[y1, y2], z=[z1, z2], mode='markers+lines',
                         marker=dict(size=5, color=['red', 'blue']),
                         line=dict(color='green', width=2))
        ])
        
        if metric == 'Manhattan':
            fig.add_trace(go.Scatter3d(x=[x1, x1, x2], y=[y1, y2, y2], z=[z1, z1, z2], mode='lines',
                                       line=dict(color='orange', width=2, dash='dash')))
        
        fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                          title=f"3D {metric} Distance Visualization")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("<h2 class='tab-subheader'>Interactive Distance Calculator</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<p class='content-text'>Calculate distances between custom points in 2D or 3D space.</p>", unsafe_allow_html=True)
        
        dimension = st.radio("Select dimension", ["2D", "3D"])
        
        if dimension == "2D":
            x1 = st.number_input("X1", value=0.0, step=0.1)
            y1 = st.number_input("Y1", value=0.0, step=0.1)
            x2 = st.number_input("X2", value=3.0, step=0.1)
            y2 = st.number_input("Y2", value=4.0, step=0.1)
            p1 = np.array([x1, y1])
            p2 = np.array([x2, y2])
        else:
            x1 = st.number_input("X1", value=0.0, step=0.1)
            y1 = st.number_input("Y1", value=0.0, step=0.1)
            z1 = st.number_input("Z1", value=0.0, step=0.1)
            x2 = st.number_input("X2", value=3.0, step=0.1)
            y2 = st.number_input("Y2", value=4.0, step=0.1)
            z2 = st.number_input("Z2", value=5.0, step=0.1)
            p1 = np.array([x1, y1, z1])
            p2 = np.array([x2, y2, z2])

        if st.button("Calculate Distances"):
            metrics = ['Euclidean', 'Manhattan', 'Chebyshev']
            results = []
            for metric in metrics:
                distance, formula = calculate_distance(p1, p2, metric)
                results.append({"Metric": metric, "Distance": distance, "Formula": formula})
            
            st.markdown("<div class='highlight'>", unsafe_allow_html=True)
            st.markdown("<h3 class='content-text'>Results:</h3>", unsafe_allow_html=True)
            for result in results:
                st.write(f"**{result['Metric']}:** {result['Distance']:.2f} ({result['Formula']})")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<p class='content-text'>Visual comparison of different distance metrics:</p>", unsafe_allow_html=True)
        if 'results' in locals():
            fig = go.Figure([go.Bar(x=[r['Metric'] for r in results], y=[r['Distance'] for r in results],
                                    text=[f"{r['Distance']:.2f}" for r in results],
                                    textposition='auto',
                                    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1'])])
            fig.update_layout(title="Distance Comparison", xaxis_title="Metric", yaxis_title="Distance")
            st.plotly_chart(fig)

with tab3:
    st.markdown("<h2 class='tab-subheader'>Real-world Examples of Distance Metrics</h2>", unsafe_allow_html=True)
    
    st.markdown("<p class='content-text'>Explore how different distance metrics apply to real-world scenarios.</p>", unsafe_allow_html=True)
    
    scenario = st.selectbox("Select a scenario", ["City Navigation", "Image Similarity", "Chess Moves"])
    
    if scenario == "City Navigation":
        st.markdown("<div class='highlight'>", unsafe_allow_html=True)
        st.write("Imagine you're in New York City, trying to get from Times Square to Central Park.")
        st.write("- **Euclidean Distance:** The length of a straight line between the two points (as the crow flies).")
        st.write("- **Manhattan Distance:** The distance you'd actually walk along the city blocks.")
        st.write("- **Chebyshev Distance:** Not very relevant in this scenario, but could represent the number of blocks in the longer direction.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Simple city grid visualization
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[0, 5], y=[0, 5], mode='markers', name='Points',
                                 marker=dict(size=10, color=['red', 'blue'])))
        fig.add_trace(go.Scatter(x=[0, 5], y=[0, 5], mode='lines', name='Euclidean', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=[0, 0, 5], y=[0, 5, 5], mode='lines', name='Manhattan', line=dict(color='orange')))
        fig.update_layout(title="City Navigation Example", xaxis_title="X", yaxis_title="Y")
        st.plotly_chart(fig)
        
    elif scenario == "Image Similarity":
        st.markdown("<div class='highlight'>", unsafe_allow_html=True)
        st.write("When comparing images in machine learning:")
        st.write("- **Euclidean Distance:** Often used to measure similarity between image features.")
        st.write("- **Manhattan Distance:** Can be used when dealing with color differences in RGB space.")
        st.write("- **Chebyshev Distance:** Might be used to find the maximum difference in any color channel.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Generate sample image data
        img1 = np.random.rand(10, 10, 3)
        img2 = np.random.rand(10, 10, 3)
        
        fig = go.Figure(data=[
            go.Heatmap(z=img1[:,:,0], colorscale='Reds', showscale=False),
            go.Heatmap(z=img2[:,:,0], colorscale='Blues', showscale=False, xaxis='x2', yaxis='y2')
        ])
        fig.update_layout(title="Image Similarity Example",
                          grid= {'rows': 1, 'columns': 2, 'pattern': "independent"})
        st.plotly_chart(fig)
        
    else:  # Chess Moves
        st.markdown("<div class='highlight'>", unsafe_allow_html=True)
        st.write("In the game of chess:")
        st.write("- **Euclidean Distance:** Not typically used in chess.")
        st.write("- **Manhattan Distance:** The number of moves a rook would take to reach a square.")
        st.write("- **Chebyshev Distance:** The number of moves a king would take to reach a square.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Simple chess board visualization
        board = np.zeros((8, 8))
        board[::2, ::2] = 1
        board[1::2, 1::2] = 1
        fig = px.imshow(board, color_continuous_scale='gray')
        fig.update_layout(title="Chess Board")
        st.plotly_chart(fig)

with tab4:
    st.markdown("<h2 class='tab-subheader'>Test Your Knowledge</h2>", unsafe_allow_html=True)
    
    questions = [
        {
            "question": "Which distance metric would be most appropriate for calculating the shortest path for a drone to fly between two points?",
            "options": ["Euclidean", "Manhattan", "Chebyshev"],
            "correct": 0,
            "explanation": "Euclidean distance represents the straight-line distance between two points, which is the shortest path a drone could fly."
        },
        {
            "question": "In a grid-based game where characters can only move up, down, left, or right (not diagonally), which distance metric best represents the number of moves needed?",
            "options": ["Euclidean", "Manhattan", "Chebyshev"],
            "correct": 1,
            "explanation": "Manhattan distance represents the total number of vertical and horizontal moves, which matches the movement in a grid-based game without diagonal moves."
        },
        {
            "question": "If you're measuring the similarity between two colors based on their RGB values, which distance metric might be most appropriate?",
            "options": ["Euclidean", "Manhattan", "Chebyshev"],
            "correct": 2,
            "explanation": "Chebyshev distance considers the maximum difference along any dimension, which can be useful for color comparisons where the largest difference in any RGB channel might be most important."
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"<p class='content-text'><strong>Question {i+1}:</strong> {q['question']}</p>", unsafe_allow_html=True)
        user_answer = st.radio("Select your answer:", q['options'], key=f"q{i}")
        
        if st.button("Check Answer", key=f"check{i}"):
            if q['options'].index(user_answer) == q['correct']:
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error("Incorrect. Try again! 🤔")
            st.info(q['explanation'])
        st.markdown("---")

    if st.button("Show Final Score"):
        st.markdown(f"<p class='tab-subheader'>Your score: {score}/{len(questions)}</p>", unsafe_allow_html=True)
        if score == len(questions):
            st.balloons()

# Conclusion
st.markdown("<h2 class='tab-subheader'>Congratulations! 🎊</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='content-text'>
You've explored the fascinating world of distance metrics! Remember:

1. Euclidean distance is like measuring with a ruler - it's the straight-line distance between points.
2. Manhattan distance is like navigating city blocks - you can only move along grid lines.
3. Chebyshev distance considers the maximum difference in any dimension - think of a king's moves in chess.
4. The choice of distance metric can greatly impact the results in various applications, from navigation to machine learning.
5. Visualizing distances helps us understand their properties and choose the right metric for each task.

Keep exploring and applying these distance metrics in your data analysis and problem-solving adventures!
</p>
""", unsafe_allow_html=True)

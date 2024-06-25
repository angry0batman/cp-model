import streamlit as st
import numpy as np
import joblib

# Load the model
loaded_model = joblib.load('CP.joblib')

# Function to predict CP score
def predict_cp_score(codechef, codeforces, leetcode):
    new_data = np.array([[codechef, codeforces, leetcode]])
    prediction = loaded_model.predict(new_data)
    return prediction[0]

# Page setup
st.set_page_config(page_title="CP Score Predictor", page_icon=":bar_chart:")

# HTML and CSS for styling
html_temp = """
<style>
.navbar {
    overflow: hidden;
    background-color: #333;
    display: flex;
    justify-content: center;
}

.navbar a {
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;
    color: black;
}

.navbar a.active {
    background-color: #0f4a73;
    color: white;
}
</style>

<div class="navbar">
  <a class="active" href="https://ctc-sure.vercel.app/">Home</a>
  <a href="#contact">Contact Us</a>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

# Main content based on navigation choice
st.write('<div id="predict"></div>', unsafe_allow_html=True)
st.write("## Predict CP Score")
st.write("Enter scores from CODECHEF, CODEFORCES, and LEETCODE to predict CP Score:")

# Input fields for user to enter scores
codechef_score = st.number_input("Enter CODECHEF Score", min_value=0)
codeforces_score = st.number_input("Enter CODEFORCES Score", min_value=0)
leetcode_score = st.number_input("Enter LEETCODE Score", min_value=0)

# Predict button
if st.button("Predict"):
    prediction = predict_cp_score(codechef_score, codeforces_score, leetcode_score)
    st.success(f"Predicted CP Score is: {prediction}")

# Contact Us section
st.write('<div id="contact"></div>', unsafe_allow_html=True)
st.write("## Contact Us")
st.write("""
For any queries or support, please contact us at example@email.com.
""")

# Footer
footer_html = """
<div style="background-color:#0f4a73; color: white; text-align: center; padding: 10px; position: relative; bottom: 0; width: 100%; margin-top: 20px;">
    <p>© 2024 CP Score Predictor. All rights reserved.</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PrognosisHub",
    layout="wide",
    page_icon="🧑‍⚕️",
    initial_sidebar_state="expanded",
)

# Set background color
st.markdown(
    """
    <style>
        body {
            background-color: #f0f5f5;
        }
        .navbar {
            background-color: #006400; /* Dark Green */
            padding: 10px;
        }
        .navbar a {
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            font-size: 18px;
        }
        .navbar a:hover {
            background-color: #008000; /* Green */
            border-radius: 5px;
        }
    </style>
    """
    , unsafe_allow_html=True
)

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
#diabetes_model = pickle.load(open(f'{working_dir}/Saved Models/diabetes_model.sav', 'rb'))
#heart_disease_model = pickle.load(open(f'{working_dir}/Saved Models/heart_disease_model.sav', 'rb'))
#parkinsons_model = pickle.load(open(f'{working_dir}/Saved Models/parkinsons_model.sav', 'rb'))
#breast_cancer_model=pickle.load(open(f'{working_dir}/Saved Models/breast_cancer_model.sav','rb'))
import pickle
import requests
from io import BytesIO

# GitHub repository URL
github_repo_url = "https://github.com/your_username/your_repository/raw/main/"

# Load the diabetes model
diabetes_model_url = github_repo_url + "diabetes_model.sav"
response = requests.get(diabetes_model_url)
if response.status_code == 200:
    diabetes_model = pickle.load(BytesIO(response.content))
else:
    st.error("Failed to load the diabetes model")

# Load the heart disease model
heart_disease_model_url = github_repo_url + "heart_disease_model.sav"
response = requests.get(heart_disease_model_url)
if response.status_code == 200:
    heart_disease_model = pickle.load(BytesIO(response.content))
else:
    st.error("Failed to load the heart disease model")

# Load the Parkinson's model
parkinsons_model_url = github_repo_url + "parkinsons_model.sav"
response = requests.get(parkinsons_model_url)
if response.status_code == 200:
    parkinsons_model = pickle.load(BytesIO(response.content))
else:
    st.error("Failed to load the Parkinson's model")

# Load the breast cancer model
breast_cancer_model_url = github_repo_url + "breast_cancer_model.sav"
response = requests.get(breast_cancer_model_url)
if response.status_code == 200:
    breast_cancer_model = pickle.load(BytesIO(response.content))
else:
    st.error("Failed to load the breast cancer model")


# Navbar
st.markdown(
    """
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#diabetes">Diabetes</a>
        <a href="#heart_disease">Heart Disease</a>
        <a href="#parkinsons">Parkinson's</a>
        <a href="#breast_cancer">Breast Cancer</a>
    </div>
    """, unsafe_allow_html=True
)

# Home Page
st.markdown("<h1 id='home'>Welcome to Health Assistant</h1>", unsafe_allow_html=True)
st.write("Welcome to the PrognosisHub a Multiple Disease Prediction System, created by Kanchan Rai.")
st.write("This application allows you to predict the likelihood of having different diseases: Diabetes, Heart Disease, Parkinson's Disease, and Breast Cancer.")
st.write("Use the navigation bar to jump to specific prediction pages.")

# GitHub icons and link on the left
st.sidebar.subheader('Connect with the Creator:')
st.sidebar.write("[Kanchan Rai]()")

# Diabetes Prediction Page
st.markdown("<h2 id='diabetes'>Diabetes Prediction using ML</h2>", unsafe_allow_html=True)
# Rest of the code for Diabetes Prediction page remains the same...

# Heart Disease Prediction Page
st.markdown("<h2 id='heart_disease'>Heart Disease Prediction using ML</h2>", unsafe_allow_html=True)
# Rest of the code for Heart Disease Prediction page remains the same...

# Parkinson's Prediction Page
st.markdown("<h2 id='parkinsons'>Parkinson's Disease Prediction using ML</h2>", unsafe_allow_html=True)
# Rest of the code for Parkinson's Prediction page remains the same...

# Breast Cancer Prediction Page
st.markdown("<h2 id='breast_cancer'>Breast Cancer Prediction using ML</h2>", unsafe_allow_html=True)
# Rest of the code for Breast Cancer Prediction page remains the same...

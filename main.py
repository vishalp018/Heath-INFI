
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your dataset
@st.cache
def load_data():
    data = pd.read_csv("your_dataset.csv")  # Replace "your_dataset.csv" with your dataset path
    return data

# Sidebar for user input
def sidebar_inputs():
    st.sidebar.header("User Input")
    age = st.sidebar.slider("Age", 1, 100, 25)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    # Add more inputs as needed
    return age, gender

# Preprocess data
def preprocess_data(data):
    # Perform preprocessing steps like handling missing values, encoding categorical variables, etc.
    # For simplicity, let's assume that the dataset is already preprocessed
    return data

# Train model
def train_model(data):
    X = data.drop("Disease", axis=1)  # Assuming "Disease" is the target column
    y = data["Disease"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Main function
def main():
    st.title("Medical Disease Analyzer")

    # Load data
    data = load_data()

    # Sidebar inputs
    age, gender = sidebar_inputs()

    # Filter data based on user inputs
    filtered_data = data[(data['Age'] == age) & (data['Gender'] == gender)]

    # Preprocess data
    preprocessed_data = preprocess_data(filtered_data)

    # Train model
    model, X_test, y_test = train_model(preprocessed_data)

    # Make predictions
    predictions = model.predict(X_test)

    # Display results
    st.subheader("Prediction Results")
    st.write("Accuracy:", accuracy_score(y_test, predictions))

if __name__ == "__main__":
    main()

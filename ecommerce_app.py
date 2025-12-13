import streamlit as st
import pickle
import pandas as pd


@st.cache_resource
def load_model():
    with open('ecommerce_model_pipeline.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


lm = load_model()


st.title('E-commerce Spending Predictor')
st.markdown('Use the sliders below to predict the Yearly Amount Spent based on customer metrics.')


avg_session_length = st.slider('1. Avg. Session Length', 
                               min_value=30.0, max_value=40.0, value=33.0, step=0.1)
time_on_app = st.slider('2. Time on App (minutes)', 
                        min_value=10.0, max_value=15.0, value=12.0, step=0.1)
time_on_website = st.slider('3. Time on Website (minutes)', 
                            min_value=35.0, max_value=41.0, value=37.0, step=0.1)
length_of_membership = st.slider('4. Length of Membership (years)', 
                                 min_value=0.0, max_value=6.0, value=3.0, step=0.1)


if st.button('Predict Yearly Amount Spent'):
    features = pd.DataFrame({
        'Avg. Session Length': [avg_session_length],
        'Time on App': [time_on_app],
        'Time on Website': [time_on_website],
        'Length of Membership': [length_of_membership]
    })
    
    prediction = lm.predict(features)[0]
    
    st.success(f'Predicted Yearly Amount Spent: ${prediction:,.2f}')


st.caption('Model is a simple Linear Regression trained on the provided Ecommerce data by Benjamin O.')
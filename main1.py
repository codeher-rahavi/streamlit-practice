import streamlit as st
import pandas as pd

st.title("Streamlit form demo")

with st.form(key="sample_form"):

    #Text inputs
    st.subheader("text inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")

    #Date and time inputs
    st.subheader("Date and time inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")

    #selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option",['Option 1' ,'Option 2', 'Option 3'])
    gender = st.selectbox("Select your gender",['Male','Female','Other'])
    slider_value = st.select_slider("Select a range", options=[1,2,3,4,5])

    #toggle and checkboxes
    st.subheader("Toggle and checkboxes")
    notifications = st.checkbox("Receive notifications")
    toggle_value = st.checkbox("enable dark mode?",value=False)

    #submit button for the form 
    submit_button = st.form_submit_button(label="Submit")



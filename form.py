import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

st.title("User information form")

form_values={
    "name":None,
    "age":None,
    "height":None,
    "gender":None,
    "dob":None
}

min_date=datetime(1990,1,1)
max_date = datetime.now()
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter you name:")
    form_values["age"] = st.number_input("Enter your age:")
    form_values["height"]=st.number_input("Enter your height:")
    form_values["gender"]=st.radio("Select your gender:",options=["Male","Female","Others"])
    form_values["dob"]=st.date_input("Enter your date of birth:",max_value=max_date,min_value=min_date)

   
    st.form_submit_button(label="Submit")
    if not all(form_values.values()):
        st.warning("Please fill all the fields before submitting the form")
    else:
        st.balloons()
        st.write("### Info")
        for (key,value) in form_values.items():
            st.write(f"{key}:{value}")
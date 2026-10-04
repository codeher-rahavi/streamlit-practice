import streamlit as st
from datetime import datetime

min_date=datetime(1990,1,1)
max_date = datetime.now()

st.title("User Information form")
with st.form(key="user_information_form"):
    name = st.text_input("Enter your name:")
    dob=st.date_input("Enter your date of birth:", min_value=min_date, max_value=max_date)

    if dob:
        age = max_date.year - dob.year
        if dob.month > max_date.month or(dob.month == max_date.month and dob.day > max_date.day):
            age-=1
        st.write(f"Your calculated age is {age} years")

    submit_button=st.form_submit_button(label="Submit")
    if submit_button:
        if not name or not dob:
            st.warning("please fill all the required fields")
        else:
            st.success(f"Thank you {name}. Your age is {age}.")
            st.balloons()

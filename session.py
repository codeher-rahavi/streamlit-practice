import streamlit as st

# # a simple counter variable withour session state
# counter =0
# st.write(f"counter value: {counter}",)

# #button to increment the counter

# if st.button("Increment counter:"):
#     counter+=1
#     st.write(f"Counter incremented to {counter}")
# else:
#     st.write(f"Counter stays at {counter}")

# st.write(f"counter value: {st.session_state.counter}")


#st.session_state

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment counter"):
    st.session_state.counter+=1
    st.write(f"Counter imcrement to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"counter did not reset")

st.write(f"counter value: {st.session_state.counter}")
import streamlit as st

st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elemetns like sliders,buttons,and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

#Tabs layout
tab1,tab2,tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.write("You are in tab 1")
with tab2:
    st.write("You are in tab 2")
with tab3:
    st.write("You are in tab 3")


#column layout 
col1,col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")

#container example
with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of container as a grouping for elements")
    st.write("Containers help manage sections of the age")


#empty placeholders
placeholder = st.empty()
placeholder.write("this is an emoty placecholder useful for dynamic content")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated")

#expander
with st.expander("expand for more details"):
    st.write("This is additional information that is hidden by default")
    st.write("You can use expanders to keep your interface cleaner")


#popover
st.write("Hover over this button for a tooltip")
st.button("Button with tooltip",help="this is a tooltip ot popover on hover")

#sidebar input handling
if sidebar_input:
    st.write(f"you entered in the sidebar:{sidebar_input}")
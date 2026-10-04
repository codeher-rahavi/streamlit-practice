import streamlit as st
import os
import pandas as pd

pressed = st.button("press me")
print("First:",pressed)

submitted = st.button("Submit")
print("Second:",submitted)
st.divider()

st.title("Super Simple Title")
st.subheader("subheader")
st.markdown("this is _Markdown_")
st.caption("small text")
code_example="""
def greet(name):
    print("Hello",name)
"""
st.code(code_example,language="python")
st.divider()

st.image(os.path.join(os.getcwd(),"static","BG.webp"))

st.subheader("Dataframe")

df = pd.DataFrame({
    'Name':['John','Alice','Bob'],
    'Age':[25,30,22],   
    'Occupation':['Engineer','Doctor','Artist']
})
st.dataframe(df)


#data editor section (Editable dataframe)

st.subheader("Data Editor")
editable_df = st.data_editor(df)

#static table section
st.subheader("Static table")
st.table(df)

#metrics section 
st.subheader("Metrics")
st.metric(label="Total Rows",value=len(df))
st.metric(label="Average Age",value=round(df['Age'].mean(),1))

#JSON and Dict section
st.subheader("JSON and Dictionaries")
sample_dict = {
    "Name":"Alice",
    "Age":25,
    "Skills":["Python","Data Analysis","Machine Learning"]
}
st.json(sample_dict)

st.write("Dictionary view:",sample_dict)


import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Charts Demo")

#generage sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

#Area chart selection
st.subheader("Area chart")
st.area_chart(chart_data)

#Bar chart section
st.subheader("Bar chart")
st.bar_chart(chart_data)

#line chart
st.subheader("Line chart")
st.line_chart(chart_data)

#scatter chart section
st.subheader("Scatter chart")
scatter_data = pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100)
})

st.scatter_chart(scatter_data)

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] +[13.08, 80.27],columns=['lat', 'lon'] #coordinats around SF
)

st.map(map_data)

st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'],label='A')
ax.plot(chart_data['B'],label='B')
ax.plot(chart_data['C'],label='C')
ax.set_title("Pyplot line chart")
ax.legend()
st.pyplot(fig)

#forms



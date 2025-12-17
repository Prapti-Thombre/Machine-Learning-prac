#Streamlit is an open source app framework for machine learning and data science projects . it allows you to create beautiful web applications for your machin elearning and data science projects with simple python scripts



import streamlit as st
import pandas as pd
import numpy as np

##title of the application
st.title("hello Streamlit")


#display a simple text 
st.write("this is a  simple text")

##create a simple dataframe

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

##Display the DataFrame
st.write("here is the dataframe")
st.write(df)

#create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']

)

st.line_chart(chart_data)

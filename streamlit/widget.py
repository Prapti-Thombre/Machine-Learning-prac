import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("ENter your name:")




age = st.slider("select your age",0,100,25)

st.write(f"Your age is {age}")


options = ["Python","Java", "C++", "javascript"]
choice = st.selectbox("choose your favourite language",options)
st.write(f"You selected{choice}")


if name:
    st.write(f"hello, {name}")



data = {
    "name":["john","jane","jake","jill"],
    "Age":[28,24,35,40],
    "city":["new york","los angeles","chicago","houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file = st.file_uploader("choose a csv file", type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
                        
import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.jpg")

with col2:
    st.title("Twinkle")
    content = """ 
    Hi, I am Twinkle! I am a Python programmer. I am pursuing my graduation in
     Bachelors of technology Computer Science and Engineering from Punjab Technical University in Jalandhar.
     I love to get new experiences and learn from my surroundings.
     """
    st.info(content)

content2 = """
Below you can find some of the apps I have Built in python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col,  col4 = st.columns([2.0, 0.5, 2.0])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
import streamlit as st

def app():
    st.title("Home page.")

    text_input = st.text_input("Enter anything you want")
    if st.button("Submit"):
        st.write(f"You typed: {text_input}")
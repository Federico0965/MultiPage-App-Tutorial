import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/924ecd9e-1512-4e6f-b21a-f696571d381b/pU6OJ1olFh.json")
json_data_project = Image.open("images/json_data.png")
gui_python_project = Image.open("images/gui_python.png")

def app():
    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Hi, I am Coding Boy :wave:")
        st.title("A Python Coder and YouTuber")
        st.write("I am passionate about finding ways to use Python and RealPython to be more efficient and effective in business settings.")
        st.write("[Learn more >](https://realpython.com/)")
    
    # --- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                On my Python YouTube channel, I am making videos for people who:
                - want to learn the Python Basics
                - who want to learn the Intermediate OOP Programming in Python with classes
                - who want to make Python projects
                - who want to master Python

                If this sounds interesting to you, consider subscribing and turning on notifications so you don't miss on any new videos.
                """
            )
            st.write("[Subscribe here >](https://www.youtube.com/@BruvCode?sub_confirmation=1/)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
    
    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("My Projects")
        image_column, text_column = st.columns(2)
        with image_column:
            st.image(json_data_project)
        with text_column:
            st.subheader("Work with JSON in Python")
            st.write(
                """
                Want to know how to work with JSON (JavaScript-Object Notation) with Python? This project
                is right for you! 
                We'll be using `json` module in Python to read and use JSON Data in Python like dictionaries

                In this project, I'll show you exactly how to do it!
                """
            )
            st.markdown("[Find tutorial...](https://realpython.com/python-json/)")
        with image_column:
            st.image(gui_python_project)
        with text_column:
            st.write("##")
            st.subheader("Create your own GUIs in Python")
            st.write(
                """
                Want to know how to make your own GUI Apps using Python? This project is
                right for you!
                We'll be using `tkinter` module in Python to create the window, and we'll style it up.

                In this project, I'll show you exactly how to do it
                """
            )
            st.markdown("[Find tutorial...](https://realpython.com/quizzes/python-gui-programming-with-tkinter/)")
    
    # ---- CONNECT ----
    with st.container():
        st.write("---")
        st.header("Connect with me!!")
        st.write("Email Address - example@gmail.com")
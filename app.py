import streamlit as st
from streamlit_option_menu import option_menu

import homepage, about, contact

st.set_page_config(
    page_title="Multi-Page App Tutorial",
    page_icon=":tada:",
    layout="wide"
)

def MultiApp():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "About", "Contact"],
            icons=["house", "info-circle", "envelope"],
            menu_icon="cast"
        )
    if selected == "Home":
        homepage.app()
    if selected == "About":
        about.app()
    if selected == "Contact":
        contact.app()

if __name__ == "__main__":
    MultiApp()
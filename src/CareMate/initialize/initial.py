import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from streamlit_navigation_bar import st_navbar

class initialize:
    def css_loader(file_path):
        with open(file_path) as f:
            st.markdown(
                f'<style>{f.read()}<style>',
                unsafe_allow_html = True
            )
    def load_nav_bar():
        pages = ["Home", "Try CareMate", "GitHub"]
        urls = {"GitHub": "https://github.com/34RTHY/PrettifiedCareMate"}
        styles = {
            "nav": {
                "background-color": "royalblue",
                "height": "60px",
                "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                "z-index":"1"
            },
            "img": {
                "padding-right": "14px",
            },
            "span": {
                "color": "white",
                "padding": "14px",
                "border-radius": "30px",
            },
            "active": {
                "color": "royalblue",
                "background-color": "white",
                "font-weight": "bold",
                "padding": "14px",
                "border": "0px solid #101a2c",
            }
        }
        options = {
            "show_menu": False,
            "show_sidebar": False,
        }

        page = st_navbar(
            pages,
            urls=urls,
            styles=styles,
            options=options,
        )
        if page == 'Home':       
            pass
        if page=='Try CareMate':
            page='Home'
            switch_page('CareMate')
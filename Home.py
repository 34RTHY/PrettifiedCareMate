import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from streamlit_navigation_bar import st_navbar
import os
from src import CareMate
import src.CareMate as caremate
path_to_css = './style/Homestyle.css'

class Home:
    def __init__(self):
        st.set_page_config(initial_sidebar_state="collapsed")
        if 'selboxdisabled' not in st.session_state:
            st.session_state.selboxdisabled = False
        caremate.initialize.css_loader(path_to_css)
        caremate.initialize.load_nav_bar()

    def app(self):
        st.title(":blue[CareMate], AI Symptoms analyzer",anchor=False)
        st.caption("Your AI medical assistant, predicts diseases based on your symptoms.")
        title1, title2 = st.columns(2,gap = 'medium')
        with title1:
            st.markdown("- Displays medical coding for each suggested disease.")
            st.markdown("- Reveals potential diseases using medical evidence")
            st.markdown("- Recommends personalized treatments for symptoms")
            st.markdown("- Provides actionable plans for patients and doctors")
            if st.button('Start Analyzing ⇨', type="primary"):
                switch_page('CareMate')
        with title2:
            st.image("docmed.png")

        st.markdown("<h1 style='text-align: center;'>Features</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3,gap = 'medium')
        with col1:
            with st.container():
                st.subheader("Medical Coding",anchor=False)
                st.markdown("Precise medical coding tools for documentation and billing in healthcare.")
        
        with col2:
            with st.container():
                st.subheader("Patient Mode",anchor=False)
                st.markdown("Assists in assessing symptom severity for patients.")

        with col3:
            with st.container():
                st.subheader("Doctor Mode",anchor=False)
                st.markdown("Suggests potential diseases based on patient history and lab results.")

        st.header("About :blue[CareMate]",anchor=False)
        st.markdown(":blue[CareMate] is more than just a predictive tool, it's a gateway to informed healthcare decisions. Our advanced AI technology leverages symptom analysis to forecast potential diseases accurately. By bridging the gap between medical expertise and everyday life, CareMate is revolutionizing healthcare accessibility for both professionals and the public.")
        st.markdown("Our mission is to democratize AI technology, making it readily available and easily understandable. With CareMate, you're not just predicting diseases; you're empowering individuals with the knowledge to take control of their health.")

Home_instance = Home()
Home_instance.app()


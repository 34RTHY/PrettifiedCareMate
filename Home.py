import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import streamlit.components.v1 as components
import os
import src.CareMate as caremate
path_to_css = './style/Homestyle.css'

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


class Home:
    def __init__(self):
        st.set_page_config(initial_sidebar_state="collapsed")
        if 'selboxdisabled' not in st.session_state:
            st.session_state.selboxdisabled = False
        caremate.initialize.css_loader(path_to_css)
        caremate.initialize.load_nav_bar()

    def app(self):
        st.title(":blue[CareMate], AI Symptoms analyzer",anchor=False)
        # st.markdown("<h1 class='fade-in' style='text-align: center;'>CareMate, AI Symptoms analyzer</h1>", unsafe_allow_html=True)
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

        st.markdown("<h1 target='' style='text-align: center; opacity: 0;'>Features</h1>", unsafe_allow_html=True)
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
        st.markdown("<p target='' class='paragraph'><blue>CareMate</blue> is more than just a predictive tool, it's a gateway to informed healthcare decisions. Our advanced AI technology leverages symptom analysis to forecast potential diseases accurately. By bridging the gap between medical expertise and everyday life, CareMate is revolutionizing healthcare accessibility for both professionals and the public.</p>", unsafe_allow_html=True)
        st.markdown("<p target='' class='paragraph'>Our mission is to democratize AI technology, making it readily available and easily understandable. With CareMate, you're not just predicting diseases; you're empowering individuals with the knowledge to take control of their health.</p>", unsafe_allow_html=True)

Home_instance = Home()
Home_instance.app()


components.html(
    """<script>
const streamlitDoc = window.parent.document;

let options = {
    rootMargin: '0px',
    threshold: 1.0
};

function handleIntersect(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.tagName == 'H2' || entry.target.tagName == 'H1') {
                handleIntersectHeader(entry);
            } else if (entry.target.tagName == 'IMG') {
                handleIntersectImage(entry);
            } else if (entry.target.tagName == 'P' || entry.target.tagName == 'LI') {
                handleIntersectMarkdown(entry);
            }
        }
    });
}

function handleIntersectHeader(entry) {
    if (entry.intersectionRatio > 0.9) {
        entry.target.style.animation = `animateHeader 0.5s forwards ease-out`
    } else {
        entry.target.style.animation = 'none';
        entry.target.style.opacity = 0;
    }
}

function handleIntersectMarkdown(entry) {
    if (entry.intersectionRatio > 0.9) {
        entry.target.style.animation = `animateMarkdown 1s forwards ease-out`
    } else {
        entry.target.style.animation = 'none';
        entry.target.style.opacity = 0;
    }
}

function handleIntersectImage(entry) {
    if (entry.intersectionRatio > 0.9) {
        entry.target.style.animation = `animateImage 5s forwards ease-out`
    } else {
        entry.target.style.animation = 'none';
        entry.target.style.opacity = 0;
    }
}
 
let observer = new IntersectionObserver(handleIntersect, options);
let targetHeaders = Array.from(streamlitDoc.querySelectorAll('.main h2, h1[target]'));
let targetMarkdown = Array.from(streamlitDoc.querySelectorAll('.main .stMarkdown p[target], li'));
let targetImages = Array.from(streamlitDoc.querySelectorAll('.main img'));


let targetElements = [].concat.apply([], [targetHeaders, targetMarkdown, targetImages]) 
targetElements.forEach((targetElement) => {
    observer.observe(targetElement);
});

</script>""",
    height=0,
)
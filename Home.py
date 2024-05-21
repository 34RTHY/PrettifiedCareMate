import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import streamlit.components.v1 as components
import src.CareMate as caremate
path_to_css = './style/Landingpage.css'

class Home:
    def set_bg_hack(self, main_bg):
        '''
        A function to unpack an image from root folder and set as bg.
    
        Returns
        -------
        The background.
        '''
        # set bg name
        main_bg_ext = "png"

        st.markdown(
             f"""
             <style>
             .stApp {{
                 background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )


    def __init__(self):
        st.set_page_config(initial_sidebar_state="collapsed")
        if 'selboxdisabled' not in st.session_state:
            st.session_state.selboxdisabled = False
        caremate.initialize.css_loader(path_to_css)
        caremate.initialize.load_nav_bar()



    def app(self):
        # st.markdown("<html data-theme='cupcake'></html>", unsafe_allow_html=True)
        st.title(":blue[CareMate], AI Symptoms analyzer",anchor=False)
        # st.markdown("<h1 class='fade-in' style='text-align: center;'>CareMate, AI Symptoms analyzer</h1>", unsafe_allow_html=True)
        # st.markdown(theme_swap, unsafe_allow_html=True)
        st.caption("Your AI medical assistant, predicts diseases based on your symptoms.")
        title1, title2 = st.columns(2,gap = 'medium')
        with title1:
            st.markdown("""
                            <li style='font-size: 16px' class='listText hidden '>Displays medical coding for each suggested disease.</li>
                            <li style='font-size: 16px' class='listText hidden '>Reveals potential diseases using medical evidence</li>
                            <li style='font-size: 16px' class='listText hidden '>Recommends personalized treatments for symptoms</li>
                            <li style='font-size: 16px' class='listText hidden '>Provides actionable plans for patients and doctors</li>
                        """, unsafe_allow_html=True)

            st.markdown("<div style='padding-top:3rem'></div>", unsafe_allow_html=True)
            if st.button('Start Analyzing ⇨', type="primary"):
                switch_page('CareMate')
        with title2:
            st.image("src\\media\\docmed.png")

        st.markdown("<h1 class='hidden' style='text-align: center;'>Features</h1>", unsafe_allow_html=True)
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
        st.markdown("<p class='paragraph hidden'><blue>CareMate</blue> is more than just a predictive tool, it's a gateway to informed healthcare decisions. Our advanced AI technology leverages symptom analysis to forecast potential diseases accurately. By bridging the gap between medical expertise and everyday life, CareMate is revolutionizing healthcare accessibility for both professionals and the public.</p>", unsafe_allow_html=True)
        st.markdown("<p class='paragraph hidden'>Our mission is to democratize AI technology, making it readily available and easily understandable. With CareMate, you're not just predicting diseases; you're empowering individuals with the knowledge to take control of their health.</p>", unsafe_allow_html=True)

Home_instance = Home()
# Home_instance.set_bg_hack('src\\media\\BG-Gradient.png')
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
                        if(entry.target.classList.contains("st-emotion-cache-tcjedx")) {
                            handleIntersectColumn(entry);
                        }
                        else {
                            handleIntersectUniversal(entry);
                        }
                    }
                });
            }

            function handleIntersectUniversal(entry) {
                console.log(entry)
                entry.target.classList.add('show');
            }

            function handleIntersectColumn(entry) {
                console.log(entry + " Column")
                entry.target.classList.add('displayScale');
            }
            
            let observer = new IntersectionObserver(handleIntersect, options);
            let targetHeaders = Array.from(streamlitDoc.querySelectorAll('.main h2, h1.hidden'));
            let targetMarkdown = Array.from(streamlitDoc.querySelectorAll('.main .stMarkdown p, li'));
            let targetImages = Array.from(streamlitDoc.querySelectorAll('.main img'));
            let targetColumn = Array.from(streamlitDoc.querySelectorAll('.st-emotion-cache-tcjedx'));
            targetColumn.forEach(entry => {
                entry.classList.add('animateScale');
            });
            /* console.log(targetColumn); */


            let targetElements = [].concat.apply([], [targetHeaders, targetMarkdown, targetImages, targetColumn]) 
            targetElements.forEach((targetElement) => {
                observer.observe(targetElement);
            });

            let navBar = streamlitDoc.querySelectorAll('nav.data-v-96be9aef');
            console.log(navBar);

            </script>""",
    height=0,
)
import streamlit as st

def main():
    # Set up the page configuration
    st.set_page_config(page_title="Resnal", page_icon="🌟", layout="centered")

    # Display the animated heading and apply styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        .css-164nlkn {
            background-color: white !important; /* Main header area */
        }
        .css-1d391kg {
            background-color: white !important; /* Main content area */
        }
        .css-18e3th9 {
            background-color: white !important; /* Sidebar */
        }
        .eczjsme18 .eczjsme11 {
            background-color: #03864d;
            color: white;
        }
        .eczjsme15 {
            color: white;
            font-size: 1.3rem;
        }
        .stApp {
            background-color: #B4E380 !important;
            background-image: url('https://cdn.dribbble.com/users/20368/screenshots/4012238/data_scene.gif');
            # background-size: cover;
            background-size:contain;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        @keyframes scaleAndGrayscale {
            0% {
                background-size: 30% 30%;
                filter: grayscale(100%);
            }
            50% {
                background-size: 45% 45%;
                filter: grayscale(0%);
            }
            100% {
                background-size: 30% 30%;
                filter: grayscale(100%);
            }
        }
        .ea3mdgi8{
        position:relative;
        }

        body {
            display:flex;
            justify-content:end;
            background-color: #B4E380 !important;
            background-image: url('https://png.pngtree.com/background/20220725/original/pngtree-advertising-poster-data-analysis-cartoon-flat-picture-image_1774648.jpg');
        }

        # .ea3mdgi8 {
        #     background-image: url('https://png.pngtree.com/background/20220725/original/pngtree-advertising-poster-data-analysis-cartoon-flat-picture-image_1774648.jpg');
        #     background-repeat: no-repeat;
        #     background-attachment: fixed;
        #     background-size: 400px 600px;
        #     background-position: center;
        #     animation: scaleAndGrayscale 10s infinite ease-out;
        # }

        @keyframes slideIn {
            0% {
                opacity: 0;
                transform: translateY(-40px) translateX(20px);
            }
            50% {
                opacity: 1;
                transform: translateY(0) translateX(20px);
                
                color: green;
            }
            100% {
                opacity: 1;
                transform: translateY(0) translateX(60px); /* Ensure heading stays at the top */
                color: red;
            }
        }

        .animated-heading {
            position:absolute;
            right:0px;
            margin-left:100px;
            background-color:#03864d;
            border:1px solid black;
            border-radius:40px 40px ;  
            color:white;
            font-size: 3em;
            font-weight: bold;
            animation: slideIn 2s ease-out; /* Shorter duration for faster appearance */
            position: absolute; /* Absolute positioning */
            top: 0; /* Align to the top */
            left: 50%; /* Center horizontally */
            transform: translateX(-50%); /* Center horizontally */
            text-align: center; /* Center text alignment */
            margin: 0;
            padding-top: 20px; /* Add padding from the top */
        }
        .block-container{
            transform:translateX(21rem);
        }
        .bottom-text {
            font-size: 1.5em;
            margin-top: 50px;
            text-align: center;
        }

        .sidebar {
            width: 70%;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8); /* Slightly transparent white background */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: absolute;
            margin-right:-12rem;
            right:40px;
            top: 10px;
            bottom: 10px;
            color: black;
            overflow: auto; /* Ensure content does not overflow */
        }
        </style>
        """, unsafe_allow_html=True
    )

    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Navigation logic
    if st.session_state.page == "home":
        st.markdown('<div class="animated-heading"><div>Resnal <br> Result and Evaluation<div></div>', unsafe_allow_html=True)
        st.markdown('<div class="bottom-text"></div>', unsafe_allow_html=True)
       # st.markdown('<div class="sidebar"><p>Welcome to Resnal, your go-to platform for managing and evaluating student results. Here, you can view detailed results, analyze data, and make informed decisions based on comprehensive evaluations.</p></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

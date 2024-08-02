import streamlit as st

def main():
    # Set up the page configuration
    st.set_page_config(page_title="Resnal", page_icon="🌟", layout="centered")

    # Display the animated heading and apply styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white !important;
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
        .eczjsme18{
            #  background: rgb(238,174,202);
            background: radial-gradient(circle, rgba(118,174,202,0.4) 40%, rgba(148,187,233,0.1) 70%);;
            color:black;
        }
        .eczjsme13{
        color:white;
        }
        .eczjsme14{
       color:white;
        }
#         .eczjsme18 .eczjsme11 {
#         font-family: "Lucida Console", "Courier New", monospace;
# #            background: rgb(238,174,202);
# # background: radial-gradient(circle, rgba(238,174,202,0.8) 0%, rgba(148,187,233,0.6) 90%);
# #             color: black !important;
# #  background: rgba(0, 128, 0, 0.5);
# # background: #B71375;
# # opacity:50;
# #              background: rgb(238,174,202);
# # background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);

# background-color: #36BA98;

# background-image: linear-gradient(38deg, #4158D0 4%, #C850C0 26%, #36BA98 20%);

#         }
.eczjsme18 .eczjsme11 {
            font-family: "Lucida Console", "Courier New", monospace;
            background: rgba(238,174,202,0.7);/* Green with transparency */
            background-image: linear-gradient(38deg, rgba(35, 28, 118, 0.7) 37%, rgba(200, 80, 192, 0.5) 26%, rgba(41, 86, 162, 0.6) 20%);
        }
        .eczjsme15 {
            color: black;
            font-size: 1.3rem;
        }
        .eczjsme14{
        color:black;
        }
        
        .stApp {
            # background-color: #59D5E0 !important;
            background-image: url('https://media.licdn.com/dms/image/D4D12AQEDzlOGfiudRg/article-cover_image-shrink_600_2000/0/1692353679370?e=2147483647&v=beta&t=02i3ENOOcT5iFray7urZUm8EidUhH5jCXLb0HnDBlQ4');
            # background-size: cover;
            background-size:contain;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: "Lucida Console", "Courier New", monospace;
            
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
            background-color: #59D5E0 !important;
            background-image: url('https://media.licdn.com/dms/image/C4D12AQEeKAn9dPLbhw/article-cover_image-shrink_600_2000/0/1616667695311?e=2147483647&v=beta&t=KTbbDeJ4Wwf6KFCPZ0Q1Et1jbaD7d81SHbTx-NVs3QA');
        }

        # .ea3mdgi8 {
        #     background-image: url('https://media.licdn.com/dms/image/C4D12AQEeKAn9dPLbhw/article-cover_image-shrink_600_2000/0/1616667695311?e=2147483647&v=beta&t=KTbbDeJ4Wwf6KFCPZ0Q1Et1jbaD7d81SHbTx-NVs3QA');
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
            # background-color:#03864d;
            background-color:rgba(35, 28, 118, 0.7);
            border:1px solid black;
            border-radius:40px 40px ;  
            color:white;
            font-family: "Lucida Console", "Courier New", monospace;
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
            width: 90%;
            padding: 20px;
            background: #59D5E0; /* Slightly transparent white background */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: fixed;
            margin-right:-12rem;
            right:40px;
            top: 10px;
            bottom: 10px;
            color: black !important;
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

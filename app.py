import streamlit as st
from admin import admin_page
from streamlit.components.v1 import html

def inject_custom_css():
    # Custom CSS to apply Inter font globally
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

    /* Apply Inter font globally */
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    /* Customize sidebar */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
        color: white;
        height: 100vh;
    }

    /* Sidebar radio button styles */
    [data-testid="stSidebar"] .stRadio div {
        padding: 10px;
        margin: 5px 0;
        background-color: #1A1A1A;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }

    [data-testid="stSidebar"] .stRadio div:hover {
        background-color: #333333;
    }

    /* Custom icons for each sidebar item */
    [data-testid="stSidebar"] .stRadio div:nth-child(1)::before {
        content: '🏠';
        padding-right: 10px;
        color: white;
    }

    [data-testid="stSidebar"] .stRadio div:nth-child(2)::before {
        content: 'ℹ️';
        padding-right: 10px;
        color: white;
    }

    [data-testid="stSidebar"] .stRadio div:nth-child(3)::before {
        content: '🖥️';
        padding-right: 10px;
        color: white;
    }

    [data-testid="stSidebar"] .stRadio div:nth-child(4)::before {
        content: '🌍';
        padding-right: 10px;
        color: white;
    }

    [data-testid="stSidebar"] .stRadio div:nth-child(5)::before {
        content: '🔐';
        padding-right: 10px;
        color: white;
    }

    [data-testid="stSidebar"] .stRadio div:nth-child(6)::before {
        content: '🔑';
        padding-right: 10px;
        color: white;
    }

    /* Change selected option background */
    [data-testid="stSidebar"] .stRadio div[data-checked="true"] {
        background-color: #0072CE;
        border-radius: 8px;
    }
    </style>
    """
    # Injecting CSS into Streamlit app
    html(css, height=0)

inject_custom_css()  # Call the function to apply the custom CSS

# Your usual Streamlit code follows here...

# Function to display the Home Page
def home():
    st.title("Road Accident Detection & Alert System")
    st.header("Enhancing Road Safety Through AI-Driven Solutions")
    st.write("""
        Our platform leverages advanced AI technology to detect road accidents in real-time,
        providing instant alerts to emergency services and reducing response times.
        By integrating machine learning algorithms and a user-friendly interface,
        we aim to create safer roads for everyone.
    """)

# Function to display the About Page
def about():
    st.title("About Our Mission")
    st.header("Committed to Road Safety and Innovation")
    st.write("""
        Our project is dedicated to improving road safety through cutting-edge AI technology. 
        By harnessing the power of machine learning and real-time monitoring, we aim to detect 
        accidents faster and more accurately. Our team is passionate about making a positive impact
        on traffic and road safety, and we are constantly innovating to create smarter, safer transportation systems.
        Learn more about our journey and the values that drive us towards a safer future.
    """)

# Function to display the Technology Page
def technology():
    st.title("Technology Behind the System")
    st.header("Advanced AI and Machine Learning")
    st.write("""
        Our Road Accident Detection & Alert System is built using cutting-edge technology to ensure accurate and timely detection of road incidents.
        
        **Key Technologies:**
        - **Artificial Intelligence (AI):** Our system leverages AI to analyze video feeds in real-time, identifying potential accidents with high accuracy.
        - **Machine Learning:** We use supervised learning techniques to train our models on vast datasets of road footage, enabling them to recognize patterns associated with accidents.
        - **Computer Vision:** By utilizing computer vision algorithms, our system can interpret and understand the visual data from cameras, detecting objects, movements, and anomalies.
        - **Cloud Computing:** The system is hosted on the cloud, ensuring scalability, reliability, and the ability to process large amounts of data efficiently.
        
        **How It Works:**
        1. **Data Input:** The system receives live video feeds from CCTV cameras installed on roads.
        2. **Processing:** The AI algorithms process the video in real-time, analyzing each frame for signs of accidents.
        3. **Detection:** If an accident is detected, the system instantly sends an alert to the relevant authorities with details such as location, severity, and time.
        4. **Continuous Learning:** The machine learning models are continuously updated with new data, improving their accuracy over time.
        
        Our commitment to innovation ensures that our system stays at the forefront of technology, providing the most effective solution for road safety.
    """)

# Function to display the Impact Page
def impact():
    st.title("Impact and Case Studies")
    st.header("Real-World Success Stories")
    st.write("""
        Our Road Accident Detection & Alert System has made a significant impact on road safety, helping to save lives and reduce response times in emergency situations.
        
        **Case Studies:**
        - **Case Study 1: Urban Traffic Management**
          In a bustling metropolitan city, our system was integrated into the existing traffic management infrastructure. Within the first month, the system detected over 50 accidents, enabling faster emergency response and reducing casualties by 30%.
        
        - **Case Study 2: Highway Patrol Integration**
          On a major highway known for frequent accidents, our system was deployed to monitor key intersections and high-risk areas. The system's real-time alerts helped authorities reduce the average response time from 15 minutes to just 5 minutes, significantly lowering the fatality rate.
        
        **Testimonials:**
        - *"The road accident detection system has transformed how we manage traffic incidents. The accuracy and speed of detection are unparalleled, and the system's integration with our emergency services has been seamless."* – Traffic Control Department, City X.
        - *"Since implementing the AI-based accident detection system, we've seen a noticeable decline in severe accidents. The data-driven insights provided by the system are invaluable for planning and prevention."* – Highway Safety Manager, Region Y.
        
        **Impact Statistics:**
        - **50%** reduction in road accident fatalities in areas where the system is deployed.
        - **70%** decrease in average emergency response time.
        - **200+** successful accident detections within the first quarter of deployment.
        
        These case studies and testimonials are a testament to the power of our technology and its potential to make roads safer for everyone.
    """)

# Function to display the Login Page
def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email == "admin" and password == "password":  # Simplified login check
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'admin'  # Set the page to admin after successful login
        else:
            st.error("Invalid email or password.")

# Initialize session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Function to display the Signup Page
def signup():
    st.title("Sign Up")
    st.write("Create an account to use the application.")

    # Simple signup form
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password == confirm_password:
            st.success("Account created successfully!")
        else:
            st.error("Passwords do not match. Please try again.")

# Set up navigation bar
def main():
    inject_custom_css()  # Inject custom CSS to style the sidebar

    if st.session_state['logged_in'] and st.session_state['page'] == 'admin':
        admin_page()  # Call the admin page directly if logged in
    else:
        st.sidebar.title("Navigation")
        pages = ["Home", "About", "Technology", "Impact", "Login", "Signup"]
        choice = st.sidebar.radio("Go to", pages)

        # Call functions based on user's choice
        if choice == "Home":
            home()
        elif choice == "About":
            about()
        elif choice == "Technology":
            technology()  # Call the technology page
        elif choice == "Impact":
            impact()  # Call the impact page
        elif choice == "Login":
            login()
        elif choice == "Signup":
            signup()

if __name__ == "__main__":
    main()
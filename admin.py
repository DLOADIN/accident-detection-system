import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import random
import time

# Customizing the dark mode theme for graphs
plt.style.use('dark_background')

# Function to check if user is logged in
def check_login():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.warning("You need to log in to access the Admin page.")
        st.stop()

# Function to simulate accident notifications
def get_random_accident():
    locations = ["Intersection A", "Highway 1", "Downtown", "Bridge 2", "Tunnel 3"]
    severities = ["Low", "Medium", "High"]

    return {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Location": random.choice(locations),
        "Severity": random.choice(severities),
        "Status": "New"
    }

# Function for Notifications page
def notifications():
    st.title("Real-Time Accident Notifications")

    # Initialize notifications list in session state
    if "notifications" not in st.session_state:
        st.session_state["notifications"] = []

    # Button to simulate receiving a new accident notification
    if st.button("Simulate New Accident"):
        new_notification = get_random_accident()
        st.session_state["notifications"].append(new_notification)
        st.toast(f"New accident detected at {new_notification['Location']}")

    # Simulate real-time notifications
    if st.button("Start Real-Time Monitoring"):
        with st.spinner("Monitoring for accidents..."):
            for _ in range(5):  # Simulate 5 new notifications
                time.sleep(3)  # Wait 3 seconds between notifications
                new_notification = get_random_accident()
                st.session_state["notifications"].append(new_notification)
                st.toast(f"New accident detected at {new_notification['Location']}")

    # Create a dataframe from the notifications
    notifications_df = pd.DataFrame(st.session_state["notifications"])

    # Display the notifications in a table with adjusted width
    if not notifications_df.empty:
        st.write("Latest Accident Notifications:")
        st.dataframe(notifications_df, width=1200, height=400)  # Adjust the width and height
    else:
        st.write("No accident notifications yet.")

def admin_statistics():
    st.title("Statistics")

    # Create sample data for the graphs
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    accidents_by_month = np.random.randint(10, 100, size=12)
    accidents_by_day = np.random.randint(5, 20, size=7)
    severity_levels = ["Low", "Medium", "High"]
    accident_severity_time = [random.choice(severity_levels) for _ in range(12)]
    areas = ["Area 1", "Area 2", "Area 3", "Area 4", "Area 5"]
    accidents_by_area = np.random.randint(5, 50, size=len(areas))

    # Filters for exploration
    selected_month = st.selectbox("Select Month", months)
    selected_area = st.multiselect("Select Area(s)", areas, default=areas)

    # Filtered data for graphs
    filtered_accidents_by_area = [accidents_by_area[i] for i, area in enumerate(areas) if area in selected_area]

    # Create two equal-width columns for side-by-side graphs
    col1, col2 = st.columns(2)

    # First graph: Accidents by Month
    with col1:
        st.subheader(f"Accidents Detected in {selected_month}")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(months, accidents_by_month, label="Accidents Detected", color="cyan", marker='o')
        ax.set_xlabel("Months")
        ax.set_ylabel("Number of Accidents")
        ax.set_title(f"Accidents Detected by Month in {selected_month}")
        st.pyplot(fig)

    # Second graph: Accidents by Area
    with col2:
        st.subheader("Number of Accidents by Area")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.bar(selected_area, filtered_accidents_by_area, color="lightblue")
        ax2.set_xlabel("Areas")
        ax2.set_ylabel("Number of Accidents")
        ax2.set_title("Accidents Detected by Area")
        st.pyplot(fig2)

    # Third graph: Accidents by Day of the Week
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Accidents by Day of the Week")
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        ax3.bar(days_of_week, accidents_by_day, color="orange")
        ax3.set_xlabel("Day of the Week")
        ax3.set_ylabel("Number of Accidents")
        ax3.set_title("Accidents Detected by Day of the Week")
        st.pyplot(fig3)

    # Fourth graph: Severity of Accidents Over Time
    with col4:
        st.subheader("Severity of Accidents Over Time")
        fig4, ax4 = plt.subplots(figsize=(8, 4))
        ax4.plot(months, accident_severity_time, color="red", marker='o')
        ax4.set_xlabel("Months")
        ax4.set_ylabel("Severity Level")
        ax4.set_title("Severity of Accidents Over Time")
        st.pyplot(fig4)

# Function for Upload Footage page
def upload_footage():
    st.title("Upload Footage")
    st.write("This page will allow admins to upload footage for accident detection.")

    # File uploader for video files
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # For demo purposes, display the video
        st.video(uploaded_file)
        st.write("Video uploaded successfully. Processing for accident detection...")

# Function for Live Footage page
def live_footage():
    st.title("Live Footage")
    st.write("This page will display live footage for accident detection in real-time.")

    # Use Streamlit's camera_input to access live camera feed
    live_camera = st.camera_input("Live Camera")

    if live_camera is not None:
        # Display the live camera input for demo purposes
        st.image(live_camera)
        st.write("Live footage received. Processing for accident detection...")

# Function for the Profile page
def profile():
    st.title("Admin Profile")
    st.write("Update your profile information.")

    # Set up default values for profile fields
    if 'name' not in st.session_state:
        st.session_state['name'] = 'John Doe'
    if 'email' not in st.session_state:
        st.session_state['email'] = 'admin@example.com'
    if 'password' not in st.session_state:
        st.session_state['password'] = 'password123'

    # Create the profile form
    with st.form("profile_form"):
        name = st.text_input("Full Name", value=st.session_state['name'])
        email = st.text_input("Email", value=st.session_state['email'])
        password = st.text_input("Password", type="password", value=st.session_state['password'])

        # Submit button for form
        submitted = st.form_submit_button("Save Changes")

        if submitted:
            # Update session state with new values
            st.session_state['name'] = name
            st.session_state['email'] = email
            st.session_state['password'] = password
            st.success("Profile information updated successfully!")

# Function for Logout
def logout():
    st.session_state['logged_in'] = False
    st.success("Logged out successfully!")
    st.rerun(scope="app") 
    # st.experimental_rerun()
    # Reload the page after logout

# Main function for the admin page
def admin_page():
    check_login()

    st.sidebar.title("Admin Navigation")
    admin_pages = ["Statistics", "Upload Footage", "Live Footage", "Notifications", "Profile", "Logout"]
    admin_choice = st.sidebar.radio("Admin Menu", admin_pages)

    if admin_choice == "Statistics":
        admin_statistics()
    elif admin_choice == "Upload Footage":
        upload_footage()
    elif admin_choice == "Live Footage":
        live_footage()
    elif admin_choice == "Profile":
        profile()
    elif admin_choice == "Notifications":
        notifications()  # Call the notifications function
    elif admin_choice == "Logout":
        logout()

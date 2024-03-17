import streamlit as st
from send_email_via_web import sendemailViaWeb


st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email Address")
    # Define some sample data
    options = ['Job Enquiries', 'Project Proposals', 'Other']

    # Create a dropdown
    selected_option = st.selectbox('Select an option:', options)
    text_input = st.text_area("Enter some text:")

    # Display the selected option
    # st.write('You selected:', selected_option)
    button = st.form_submit_button()

    if button:
        sendemailViaWeb(user_email, selected_option+"--"+text_input)
        st.info("Your email was sent successfully.....")

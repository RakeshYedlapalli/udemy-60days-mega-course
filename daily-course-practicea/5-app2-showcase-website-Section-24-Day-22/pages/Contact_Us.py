import streamlit as st
from send_email_via_web import sendemailViaWeb


st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email Address")
    message = st.text_area("Your message here")
    button = st.form_submit_button()

    if button:
        sendemailViaWeb(user_email, message)
        st.info("Your email was sent successfully.....")

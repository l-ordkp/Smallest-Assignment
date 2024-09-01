import streamlit as st

def handle_message():
    st.write("You have selected to Leave a Message.")
    user_message = st.text_input("Please type your message below:")
    if st.button("Send Message"):
        if user_message:
            st.success(f"Message sent: {user_message} to Dr. Adrin, he will revert to you shortly")
        else:
            st.warning("Please enter a message before sending.")
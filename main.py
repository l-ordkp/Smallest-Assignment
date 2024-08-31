import streamlit as st

st.title("AI Receptionist")
st.write("Please choose an option:")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_message_input' not in st.session_state:
    st.session_state.show_message_input = False

if st.button("Emergency"):
    st.write("You have selected Emergency. Please describe the emergency.")
    # Here you can add further steps to collect details about the emergency

if st.button("Leave a Message"):
    st.session_state.show_message_input = True

if st.session_state.show_message_input:
    st.write("You have selected to Leave a Message.")
    
    # Text input for the message
    user_message = st.text_input("Please type your message below:")

    # Send button to submit the message
    if st.button("Send Message"):
        if user_message:
            
            st.success(f"Message sent: {user_message} to Dr. Adrin, he will revert to you shortly")
            # Clear the input field by forcing a rerun
            
        else:
            st.warning("Please enter a message before sending.")


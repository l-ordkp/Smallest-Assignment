# import streamlit as st
# from db import load_faiss_components
# from emergency_handler import handle_emergency
# from message_handler import handle_message
# import asyncio

# # Initialize session state
# if 'show_message_input' not in st.session_state:
#     st.session_state.show_message_input = False
# if 'show_emergency_input' not in st.session_state:
#     st.session_state.show_emergency_input = False

# # Load FAISS components
# scenarios, responses, index, model = load_faiss_components()

# st.title("AI Receptionist")
# st.write("Please choose an option:")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Emergency"):
#         st.session_state.show_emergency_input = True
#         st.session_state.show_message_input = False

# with col2:
#     if st.button("Leave a Message"):
#         st.session_state.show_message_input = True
#         st.session_state.show_emergency_input = False


# if st.session_state.show_emergency_input:
#     asyncio.run(handle_emergency(scenarios, responses, index, model))    

# if st.session_state.show_message_input:
#     handle_message()

# if st.button("Return to Main Menu"):
#     st.session_state.show_emergency_input = False
#     st.session_state.show_message_input = False
#     for key in ['emergency_description', 'emergency_submitted', 'emergency_response', 'location', 'start_time']:
#         if key in st.session_state:
#             del st.session_state[key]
#     st.rerun()

import streamlit as st
from db import load_faiss_components
from emergency_handler import handle_emergency
from message_handler import handle_message
import asyncio

# Initialize session state
if 'show_message_input' not in st.session_state:
    st.session_state.show_message_input = False
if 'show_emergency_input' not in st.session_state:
    st.session_state.show_emergency_input = False

# Load FAISS components
scenarios, responses, index, model = load_faiss_components()

st.title("AI Receptionist")
st.write("Please choose an option:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Emergency"):
        st.session_state.show_emergency_input = True
        st.session_state.show_message_input = False

with col2:
    if st.button("Leave a Message"):
        st.session_state.show_message_input = True
        st.session_state.show_emergency_input = False


if st.session_state.show_emergency_input:
    asyncio.run(handle_emergency(scenarios, responses, index, model))    

if st.session_state.show_message_input:
    handle_message()

if st.button("Return to Main Menu"):
    st.session_state.show_emergency_input = False
    st.session_state.show_message_input = False
    for key in ['emergency_description', 'emergency_submitted', 'emergency_response', 'location', 'start_time']:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

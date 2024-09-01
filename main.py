import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the FAISS index, scenarios, responses, and the transformer model
def load_faiss_components():
    with open('scenarios.pkl', 'rb') as f:
        scenarios = pickle.load(f)
    with open('responses.pkl', 'rb') as f:
        responses = pickle.load(f)
    index = faiss.read_index('emergency_index.faiss')
    model = SentenceTransformer('sentence_transformer_model')
    return scenarios, responses, index, model

# Function to find the most similar scenario and its response
def find_similar_scenario(query, index, model, scenarios, responses):
    query_vector = model.encode([query])
    k = 1  # 
    D, I = index.search(query_vector, k)
    return scenarios[I[0][0]], responses[I[0][0]]

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_message_input' not in st.session_state:
    st.session_state.show_message_input = False
if 'show_emergency_input' not in st.session_state:
    st.session_state.show_emergency_input = False

# Load FAISS components
scenarios, responses, index, model = load_faiss_components()

st.title("AI Receptionist")
st.write("Please choose an option:")

if st.button("Emergency"):
    st.session_state.show_emergency_input = True
    st.session_state.show_message_input = False

if st.button("Leave a Message"):
    st.session_state.show_message_input = True
    st.session_state.show_emergency_input = False

if st.session_state.show_emergency_input:
    st.write("You have selected Emergency. Please describe the situation:")
    emergency_input = st.text_input("Emergency description:")
    if st.button("Get Response"):
        if emergency_input:
            similar_scenario, response = find_similar_scenario(emergency_input, index, model, scenarios, responses)
            st.write(f"Most similar scenario: {similar_scenario}")
            st.write(f"Recommended response: {response}")
        else:
            st.warning("Please enter a description of the emergency.")

if st.session_state.show_message_input:
    st.write("You have selected to Leave a Message.")
    user_message = st.text_input("Please type your message below:")
    if st.button("Send Message"):
        if user_message:
            st.success(f"Message sent: {user_message} to Dr. Adrin, he will revert to you shortly")
        else:
            st.warning("Please enter a message before sending.")
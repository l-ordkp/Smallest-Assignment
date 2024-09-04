import streamlit as st
import time
import random
import concurrent.futures
import asyncio
from utils import fetch_db_response

async def handle_emergency(scenarios, responses, index, model):
    # Initialize session state variables
    if 'emergency_description' not in st.session_state:
        st.session_state.emergency_description = None
    if 'db_task_started' not in st.session_state:
        st.session_state.db_task_started = False
    if 'location' not in st.session_state:
        st.session_state.location = None
    if 'eta_given' not in st.session_state:
        st.session_state.eta_given = False
    if 'showing_response' not in st.session_state:
        st.session_state.showing_response = False
    if 'db_response' not in st.session_state:
        st.session_state.db_response = None
    if 'similar_scenario' not in st.session_state:
        st.session_state.similar_scenario = None
    if 'eta' not in st.session_state:
        st.session_state.eta = None
    if 'db_future' not in st.session_state:
        st.session_state.db_future = None

    # Step 1: Ask for emergency details and start the database call
    if not st.session_state.emergency_description:
        st.session_state.emergency_description = st.text_input("Please describe the emergency:")
        if st.session_state.emergency_description:
            st.session_state.start_time = time.time()
            st.session_state.db_task_started = True

            # Start the async call to the database in a different thread
            with concurrent.futures.ThreadPoolExecutor() as executor:
                st.session_state.db_future = executor.submit(fetch_db_response,
                                                             st.session_state.emergency_description, index, model, scenarios, responses)
            st.write("Emergency description received. Processing your request...")
            st.rerun()

    # Step 2: Ask for location while waiting for the database call to complete
    if st.session_state.db_task_started and not st.session_state.location:
        st.session_state.location = st.text_input("I am checking what you should do immediately, meanwhile, can you tell me which area are you located right now")
        if st.session_state.location:
            st.write("Location received. Calculating estimated arrival time...")
            st.session_state.eta = random.randint(5, 20)
            st.session_state.eta_given = True
            st.rerun()

    # Step 3: Show the ETA and provide user with two button options
    if st.session_state.eta_given and not st.session_state.showing_response:
        st.write(f"Dr. Adrin will arrive in approximately {st.session_state.eta} minutes.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Arrival is too late"):
                st.session_state.showing_response = "too_late"
                st.rerun()
        with col2:
            if st.button("Yes, it's good"):
                st.session_state.showing_response = "good"
                st.rerun()

    # Step 4: Handle the user's choice and show appropriate response
    if st.session_state.showing_response:
        # Wait for the database response if not ready
        if st.session_state.db_future and not st.session_state.db_future.done():
            elapsed_time = time.time() - st.session_state.start_time
            if elapsed_time < 15:
                remaining_time = 15 - elapsed_time
                st.write("Processing your emergency... Please hold just a sec...")
                await asyncio.sleep(remaining_time)  # Wait for the remaining time
                st.rerun()

        # Process the result from the database
        if st.session_state.db_future and st.session_state.db_future.done():
            st.session_state.similar_scenario, st.session_state.db_response = st.session_state.db_future.result()

        if st.session_state.db_response:
            if st.session_state.showing_response == "too_late":
                st.write("I understand that you are worried that Dr. Adrin will arrive too late.")
                st.write(f"Meanwhile, we would suggest that you {st.session_state.db_response}")
            elif st.session_state.showing_response == "good":
                st.write(f"Don't worry, please follow these steps: {st.session_state.db_response}, Dr. Adrin will be with you shortly.")
        else:
            st.write("Unable to retrieve emergency instructions. Please follow default emergency procedures.")

    # Reset button
    if st.button("Start Over"):
        for key in ['emergency_description', 'location', 'eta_given', 'db_response', 'showing_response', 'db_task_started', 'eta', 'db_future']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()



# import streamlit as st
# import asyncio
# import time
# import numpy as np
# from utils import simulated_db_call

# async def handle_emergency(scenarios, responses, index, model):
#     st.write("You have selected Emergency.")
    
#     # Step 1: Get emergency description
#     if 'emergency_description' not in st.session_state:
#         emergency_input = st.text_input("Please describe the emergency situation:")
#         if st.button("Submit Emergency"):
#             st.session_state.emergency_description = emergency_input
#             st.session_state.start_time = time.time()
#             st.rerun()

#     if 'emergency_description' in st.session_state:
#         # Start the database call
#         db_call_task = asyncio.create_task(simulated_db_call(
#             st.session_state.emergency_description, index, model, scenarios, responses))
        
#         # Step 2: While waiting for the database, ask for location
#         if 'location' not in st.session_state:
#             st.write("I am checking what you should do immediately. Meanwhile, can you tell me which area are you located right now?")
#             location_input = st.text_input("Your location:")
#             if st.button("Submit Location"):
#                 st.session_state.location = location_input
#                 st.rerun()

#         # Step 3: Once location is provided, give ETA
#         if 'location' in st.session_state and 'eta_given' not in st.session_state:
#             estimated_time = np.random.randint(5, 30)
#             st.write(f"Dr. Adrin will be coming to your location at {st.session_state.location} immediately.")
#             st.write(f"Estimated time of arrival: {estimated_time} minutes")
#             st.session_state.eta_given = True
#             st.session_state.estimated_time = estimated_time

#         # Step 4: Handle if arrival time is too late
#         if 'eta_given' in st.session_state:
#             is_time_ok = st.radio("Is this arrival time acceptable?", ("Yes", "No, it's too late"))
#             if is_time_ok == "No, it's too late":
#                 if 'db_response' in st.session_state:
#                     st.write(f"I understand that you are worried that Dr. Adrin will arrive too late. "
#                              f"Meanwhile, we would suggest that you {st.session_state.db_response}")
#                     st.write("Please follow these steps while the doctor comes so that the patient gets better.")
#                 else:
#                     st.write("Please hold just a sec while I fetch the appropriate instructions for you.")

#         # Ensure we've waited at least 15 seconds since the emergency was submitted
#         elapsed_time = time.time() - st.session_state.start_time
#         if elapsed_time < 15:
#             remaining_time = 15 - elapsed_time
#             st.write(f"Processing your emergency... Please wait {remaining_time:.1f} seconds.")
#             await asyncio.sleep(remaining_time)

#         # Get the database response
#         if 'db_response' not in st.session_state:
#             similar_scenario, response = await db_call_task
#             st.session_state.db_response = response
#             st.write(f"Based on your emergency: {similar_scenario}")
#             st.write(f"Immediate steps: {response}")

#     # Reset button
#     if st.button("Start Over"):
#         for key in ['emergency_description', 'location', 'eta_given', 'db_response', 'start_time']:
#             if key in st.session_state:
#                 del st.session_state[key]
#         st.rerun()




# async def handle_emergency(scenarios, responses, index, model):
#     st.write("You have selected Emergency.")
    
#     # Initialize session state variables
#     if 'emergency_description' not in st.session_state:
#         st.session_state.emergency_description = None
#     if 'start_time' not in st.session_state:
#         st.session_state.start_time = None
#     if 'db_task_started' not in st.session_state:
#         st.session_state.db_task_started = False
#     if 'location' not in st.session_state:
#         st.session_state.location = None
#     if 'eta_given' not in st.session_state:
#         st.session_state.eta_given = False
#     if 'estimated_time' not in st.session_state:
#         st.session_state.estimated_time = None
#     if 'db_response' not in st.session_state:
#         st.session_state.db_response = None
#     if 'similar_scenario' not in st.session_state:
#         st.session_state.similar_scenario = None
#     if 'showing_response' not in st.session_state:
#         st.session_state.showing_response = False

#     # Step 1: Get emergency description
#     if st.session_state.emergency_description is None:
#         emergency_input = st.text_input("Please describe the emergency situation:")
#         if st.button("Submit Emergency"):
#             st.session_state.emergency_description = emergency_input
#             st.session_state.start_time = time.time()
#             st.rerun()

#     if st.session_state.emergency_description is not None:
#         # Start the database call if not already started
#         if not st.session_state.db_task_started:
#             try:
#                 st.session_state.db_call_task = asyncio.create_task(simulated_db_call(
#                     st.session_state.emergency_description, index, model, scenarios, responses))
#                 st.session_state.db_task_started = True
#             except asyncio.CancelledError:
#                 st.write("The operation was cancelled. Please try again.")
#                 st.session_state.db_task_started = False
#                 st.rerun()
        
#         # Step 2: Ask for location while waiting for the database
#         if st.session_state.location is None:
#             st.write("I am checking what you should do immediately. Meanwhile, can you tell me which area are you located right now?")
#             location_input = st.text_input("Your location:")
#             if st.button("Submit Location"):
#                 st.session_state.location = location_input
#                 st.rerun()
        
#         # Step 3: Once location is provided, give ETA
#         if st.session_state.location is not None and not st.session_state.eta_given:
#             estimated_time = np.random.randint(5, 30)
#             st.write(f"Dr. Adrin will be coming to your location at {st.session_state.location} immediately.")
#             st.write(f"Estimated time of arrival: {estimated_time} minutes")
#             st.session_state.eta_given = True
#             st.session_state.estimated_time = estimated_time
#             st.rerun()
        
#         # Display the ETA persistently
#         if st.session_state.estimated_time is not None:
#             st.write(f"Estimated time of arrival: {st.session_state.estimated_time} minutes")

#         # Step 4: Handle if arrival time is too late
#         if st.session_state.eta_given:
#             st.write("ETA has been provided. Proceeding with the next step...")
#             if st.button("No, its too late"):
#                 elapsed_time = time.time() - st.session_state.start_time
#                 if elapsed_time >= 15 and st.session_state.db_response:
#                     st.write(f"I understand that you are worried that Dr. Adrin will arrive too late. "
#                              f"Meanwhile, we would suggest that you {st.session_state.db_response}")
#                 elif elapsed_time < 15:
#                     remaining_time = 15 - elapsed_time
#                     st.write(f"Processing your emergency... Please hold just a sec, it will take {remaining_time:.1f} seconds.")
#                     try:
#                         await asyncio.sleep(remaining_time)
#                     except asyncio.CancelledError:
#                         st.write("The operation was interrupted. Please wait a moment.")
#                     st.rerun()
#                 else:
#                     st.write("Please hold just a sec while I fetch the appropriate instructions for you.")
#                 st.session_state.showing_response = True
#                 st.rerun()
            
#             if st.button("Yes, this arrival time is acceptable"):
#                 st.write("Thank you for confirming the ETA. Please wait while we process your request.")
#                 st.session_state.showing_response = True
#                 st.rerun()
        
#         # Step 5: Ensure delay completion and get the database response
#         if st.session_state.eta_given and st.session_state.db_response is None:
#             try:
#                 similar_scenario, response = await st.session_state.db_call_task
#                 st.session_state.db_response = response
#                 st.session_state.similar_scenario = similar_scenario
#                 st.write(f"Based on your emergency: {similar_scenario}")
#                 st.write(f"Immediate steps: {response}")
#             except asyncio.CancelledError:
#                 st.write("The operation was cancelled. Please try again.")
#             st.rerun()

#     # Reset button
#     if st.button("Start Over"):
#         for key in ['emergency_description', 'location', 'eta_given', 'db_response', 'start_time', 'showing_response', 'db_task_started']:
#             if key in st.session_state:
#                 del st.session_state[key]
#         st.rerun()

import streamlit as st
import asyncio
import time
import random
from db import load_faiss_components, find_similar_scenario_async  # Import from db.py

async def handle_emergency(scenarios, responses, index, model):
    # Initialize session state variables
    if 'emergency_description' not in st.session_state:
        st.session_state.emergency_description = None
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
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

    # Step 1: Ask for emergency details and start the database call
    if not st.session_state.emergency_description:
        st.session_state.emergency_description = st.text_input("Please describe the emergency:")
        if st.session_state.emergency_description:
            st.session_state.start_time = time.time()
            st.session_state.db_task_started = True
            st.write("Emergency description received. Processing your request...")
            st.rerun()

    # Step 2: Ask for location while waiting for the database call to complete
    if st.session_state.db_task_started and not st.session_state.location:
        st.session_state.location = st.text_input("Please provide your current location:")
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
        if st.session_state.start_time is None:
            st.write("Error: Start time not set. Please try again.")
            return

        elapsed_time = time.time() - st.session_state.start_time
        if elapsed_time < 15:
            remaining_time = 15 - elapsed_time
            st.write(f"Processing your emergency... Please hold just a sec")
            await asyncio.sleep(remaining_time)
            st.rerun()
        
        if not st.session_state.db_response:
            st.write("Fetching appropriate instructions from the database...")
            try:
                st.session_state.similar_scenario, st.session_state.db_response = await asyncio.get_event_loop().run_in_executor(
                    None, find_similar_scenario_async, st.session_state.emergency_description, index, model, scenarios, responses)
            except Exception as e:
                st.write(f"An error occurred: {e}")
                st.session_state.db_response = "default emergency instructions"

        if st.session_state.db_response:
            if st.session_state.showing_response == "too_late":
                st.write("I understand that you are worried that Dr. Adrin will arrive too late.")
                st.write(f"Meanwhile, we would suggest that you {st.session_state.db_response}")
            elif st.session_state.showing_response == "good":
                st.write(f"Don't worry, please follow these steps.{st.session_state.db_response}, Dr. Adrin will be with you shortly.")
                
        else:
            st.write("Unable to retrieve emergency instructions. Please follow default emergency procedures.")

    # Reset button
    if st.button("Start Over"):
        for key in ['emergency_description', 'location', 'eta_given', 'db_response', 'start_time', 'showing_response', 'db_task_started', 'eta']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Load FAISS components once at the start
scenarios, responses, index, model = load_faiss_components()



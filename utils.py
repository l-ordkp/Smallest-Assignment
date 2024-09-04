import asyncio
from db_call import load_faiss_components, find_similar_scenario_async  

# Function to be run in a separate thread
def fetch_db_response(emergency_description, index, model, scenarios, responses):
    try:
        return find_similar_scenario_async(emergency_description, index, model, scenarios, responses)
    except Exception as e:
        return None, f"An error occurred: {e}"
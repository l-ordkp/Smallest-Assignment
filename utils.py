import asyncio
from db import find_similar_scenario

async def simulated_db_call(query, index, model, scenarios, responses):
    await asyncio.sleep(15)  # Artificial 15-second delay
    return find_similar_scenario(query, index, model, scenarios, responses)

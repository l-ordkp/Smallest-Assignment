import concurrent.futures
import faiss
import pickle
import replicate
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
load_dotenv()
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')

def load_faiss_components():
    with open('scenarios.pkl', 'rb') as f:
        scenarios = pickle.load(f)
    with open('responses.pkl', 'rb') as f:
        responses = pickle.load(f)
    index = faiss.read_index('emergency_index.faiss')
    model = SentenceTransformer('sentence_transformer_model')
    return scenarios, responses, index, model

def find_similar_scenario(query, index, model, scenarios, responses, threshold=0.5):
    query_vector = model.encode([query])
    k = 1  # Number of nearest neighbors to retrieve
    D, I = index.search(query_vector, k)
    
    similarity_score = 1 - D[0][0]
    
    if similarity_score < threshold:
        scenario = "I don't understand that."
        response = "Please repeat the question/statement."
    else:
        scenario = scenarios[I[0][0]]
        response = responses[I[0][0]]
        
    # Integrating with Replicate's LLM, whether or not the similarity score is high
    prompt = f"The user described the following emergency: {query}. Based on the similar scenario '{scenario}' from my db, and the suggested response is '{response}' from my db (there is a chance that my database wouldn't have a good or appropriate response for the scenario), provide an enhanced response that the AI receptionist can give to the user. If you think that the {query} is very much unrelated to any medical emergency then just return the statement repeat the question."
    
    output = replicate.run(
        "meta/meta-llama-3-70b-instruct",
        input={
            "top_k": 0,
            "top_p": 0.9,
            "prompt": prompt,
            "max_tokens": 512,
            "min_tokens": 0,
            "temperature": 0.6,
            "system_prompt": "You are a helpful AI Receptionist.",
            "length_penalty": 1,
            "stop_sequences": "<|end_of_text|>,<|eot_id|>",
            "presence_penalty": 1.15,
            "log_performance_metrics": False
        }
    )
    
    if isinstance(output, list):
        output = "".join(output)
<<<<<<< HEAD

=======
       
>>>>>>> b6d64ee1c9e275ff3addd2731f61429573caa935
    return scenario, output


def find_similar_scenario_async(query, index, model, scenarios, responses, threshold=0.5):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_similar_scenario, query, index, model, scenarios, responses, threshold)
        return future.result()


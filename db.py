import concurrent.futures
import faiss
import pickle
from sentence_transformers import SentenceTransformer

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
    
    # D contains the distances, closer to 0 is better (cosine similarity)
    # Convert the distance to a similarity score (1 - distance for cosine)
    similarity_score = 1 - D[0][0]
    
    if similarity_score < 0.8:  # If the similarity is below the threshold, consider it unrelated
        return "I don't understand that.", "Please repeat the question/statement."
    else:
        return scenarios[I[0][0]], responses[I[0][0]]

def find_similar_scenario_async(query, index, model, scenarios, responses, threshold=0.5):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_similar_scenario, query, index, model, scenarios, responses, threshold)
        return future.result()

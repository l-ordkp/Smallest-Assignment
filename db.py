# import faiss
# import pickle
# from sentence_transformers import SentenceTransformer

# def load_faiss_components():
#     with open('scenarios.pkl', 'rb') as f:
#         scenarios = pickle.load(f)
#     with open('responses.pkl', 'rb') as f:
#         responses = pickle.load(f)
#     index = faiss.read_index('emergency_index.faiss')
#     model = SentenceTransformer('sentence_transformer_model')
#     return scenarios, responses, index, model

# def find_similar_scenario(query, index, model, scenarios, responses):
#     query_vector = model.encode([query])
#     k = 1  # Number of nearest neighbors to retrieve
#     D, I = index.search(query_vector, k)
#     return scenarios[I[0][0]], responses[I[0][0]]
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

def find_similar_scenario(query, index, model, scenarios, responses):
    query_vector = model.encode([query])
    k = 1  # Number of nearest neighbors to retrieve
    D, I = index.search(query_vector, k)
    return scenarios[I[0][0]], responses[I[0][0]]

def find_similar_scenario_async(query, index, model, scenarios, responses):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_similar_scenario, query, index, model, scenarios, responses)
        return future.result()

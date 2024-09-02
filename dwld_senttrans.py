from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Save the model locally
model_save_path = 'sentence_transformer_model'
if not os.path.exists(model_save_path):
    model.save(model_save_path)
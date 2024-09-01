import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
emergency_dataset = [
    {
        "scenario": "The patient is not breathing",
        "response": "Patient is not breathing. Please start CPR immediately. Push hard and fast in the center of the chest."
    },
    {
        "scenario": "The patient is choking",
        "response": "Patient is choking. Perform the Heimlich maneuver. Place a fist just above the navel and thrust inward and upward."
    },
    {
        "scenario": "The patient has a severe allergic reaction",
        "response": "Patient has a severe allergic reaction. Use an epinephrine auto-injector if available, and call emergency services."
    },
    {
        "scenario": "The patient is having a heart attack",
        "response": "Patient is having a heart attack. Keep the patient calm and call emergency services immediately."
    },
    {
        "scenario": "The patient is unconscious",
        "response": "Patient is unconscious. Check for breathing, and call emergency services immediately."
    },
    {
        "scenario": "The patient is bleeding heavily",
        "response": "Patient is bleeding heavily. Apply pressure to the wound and elevate the injured area. Call emergency services immediately."
    },
    {
        "scenario": "The patient is experiencing a seizure",
        "response": "Patient is experiencing a seizure. Clear the area of any hazards and do not restrain the patient. Time the seizure and call emergency services if it lasts more than 5 minutes."
    },
    {
        "scenario": "The patient has a broken bone",
        "response": "Patient has a broken bone. Immobilize the injured area and apply ice to reduce swelling. Seek medical attention."
    },
    {
        "scenario": "The patient is in shock",
        "response": "Patient is in shock. Lay the patient down and elevate their legs. Keep them warm and calm while waiting for emergency services."
    },
    {
        "scenario": "The patient is having difficulty breathing",
        "response": "Patient is having difficulty breathing. Help them into a comfortable sitting position and encourage slow, deep breaths. Call emergency services."
    },

    {
        "scenario": "The patient is not breathing",
        "response": "Patient is not breathing. **Start CPR immediately.** Push hard and fast in the center of the chest."
    },
    {
        "scenario": "The patient is choking",
        "response": "Patient is choking. **Perform the Heimlich maneuver.** Place a fist just above the navel and thrust inward and upward."
    },
    {
        "scenario": "The patient has a severe allergic reaction",
        "response": "Patient has a severe allergic reaction. **Use an epinephrine auto-injector if available and call emergency services immediately.**"
    },
    {
        "scenario": "The patient is having a heart attack",
        "response": "Patient is having a heart attack. **Keep the patient calm and call emergency services immediately.**"
    },
    {
        "scenario": "The patient is unconscious",
        "response": "Patient is unconscious. **Check for breathing and call emergency services immediately.**"
    },
    {
        "scenario": "The patient is bleeding heavily",
        "response": "Patient is bleeding heavily. **Apply pressure to the wound and elevate the injured area.** Call emergency services immediately."
    },
    {
        "scenario": "The patient is experiencing a seizure",
        "response": "Patient is experiencing a seizure. **Clear the area of any hazards and do not restrain the patient.** Time the seizure and call emergency services if it lasts more than 5 minutes."
    },
    {
        "scenario": "The patient has a broken bone",
        "response": "Patient has a broken bone. **Immobilize the injured area and apply ice to reduce swelling.** Seek medical attention."
    },
    {
        "scenario": "The patient is in shock",
        "response": "Patient is in shock. **Lay the patient down and elevate their legs.** Keep them warm and calm while waiting for emergency services."
    },
    {
        "scenario": "The patient is having difficulty breathing",
        "response": "Patient is having difficulty breathing. **Help them into a comfortable sitting position and encourage slow, deep breaths.** Call emergency services."
    }
]


# Extract scenarios and responses separately
scenarios = [entry["scenario"] for entry in emergency_dataset]
responses = [entry["response"] for entry in emergency_dataset]

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Create embeddings for the emergency scenarios
emergency_embeddings = model.encode(scenarios)

# Set up the FAISS index
index = faiss.IndexFlatL2(emergency_embeddings.shape[1])
index.add(emergency_embeddings)

# Save the index, scenarios, and responses to be used in the main application
faiss.write_index(index, 'emergency_index.faiss')
with open('scenarios.pkl', 'wb') as f:
    pickle.dump(scenarios, f)
with open('responses.pkl', 'wb') as f:
    pickle.dump(responses, f)

print("Vector database created and saved successfully!")

# print("hi")
# import torch
# print(torch.__version__)


import os
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
import ollama

client = chromadb.PersistentClient(path="./chromadb")
collection = client.get_or_create_collection("cat_facts")

# Read the cat facts from the text file
with open('cat-facts.txt', 'r') as file:
    cat_facts = [line.strip() for line in file if line.strip()]

"""
# Normalization
def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm
"""
model = SentenceTransformer('all-MiniLM-L6-v2')
# Initialize the database with cat facts if it's empty
def insert(chunk, batch_size=100):
    for i in range(0, len(chunk), batch_size):
        batch = chunk[i : i + batch_size]
        embeddings = model.encode(batch, normalize_embeddings=True).tolist()
        ids = [f"fact_{j}" for j in range(i, i + len(batch))]
        collection.add(ids=ids, documents=batch, embeddings=embeddings)
        print("Total facts in database:", collection.count())

if collection.count() == 0:
    insert(cat_facts)
# Get the 3 most relevant cat facts based on the query with euclidean distance
def retrieve(query, top_k=3):

    query_embedding = model.encode([query], normalize_embeddings=True).tolist()

    results = collection.query(query_embeddings=query_embedding, n_results=top_k)

    if results["documents"] and results["distances"] and results["documents"][0] and results["distances"][0]:
        for fact, distance in zip(results["documents"][0], results["distances"][0]):
            print(f"Distance: {distance:.4f}, Fact: {fact}")
        return results["documents"][0]
    else:
        print("No results found.")
        return []



# User interaction loop
while True:
    input_query = input("\nAsk me about cats (or type 'exit' to quit): ")

    # Exit condition
    if input_query.lower().strip() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not input_query.strip():
        continue

    top_k = 3

    # Retrieve relevant facts
    retrieved_facts = retrieve(input_query, top_k)

    # Create prompt
    instruction_prompt = f"""
Based on the following cat facts:
{retrieved_facts}

Please provide a detailed response to the query:
'{input_query}'.

Don't make up any information.
If you don't know the answer, say 'I don't know'.
"""

    # Generate response using Ollama
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "system", "content": "You are a helpful assistant. Answer only using the provided context. Do not make up information."},
                  {"role": "user", "content": instruction_prompt}],
        options={"temperature": 0.0},
        stream=True
    )

    # Print streaming response
    print("\nAnswer: ", end="", flush=True)

    for chunk in response:
        print(chunk["message"]["content"], end="", flush=True)

    print("\n")
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_and_split_recipes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    recipes = re.split(r'---', content)
    return [recipe.strip() for recipe in recipes if recipe.strip()]

def create_vector_database(recipes):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(recipes, show_progress_bar=True)
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings.astype('float32'))
    return model, index

def search_similar_recipes(query, model, index, recipes, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding.astype('float32'), top_k)
    return [recipes[i] for i in indices[0]]
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_and_split_recipes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    recipes = re.split(r'---', content)
    return [recipe.strip() for recipe in recipes if recipe.strip()]

def create_vector_database(recipes):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(recipes)
    return vectorizer, tfidf_matrix  # SADECE 2 değer döndür!

def search_similar_recipes(query, vectorizer, tfidf_matrix, recipes, top_k=3):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    indices = similarities.argsort()[-top_k:][::-1]
    return [recipes[i] for i in indices]

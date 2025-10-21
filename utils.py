import re
import numpy as np

# FAISS'i koşullu import et
try:
    import faiss
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False
    print("FAISS not available, using simple search")

# SentenceTransformers yerine alternatives
try:
    from sentence_transformers import SentenceTransformer
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    # Alternatif embedding yöntemi
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("Using TF-IDF instead of SentenceTransformers")

def load_and_split_recipes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    recipes = re.split(r'---', content)
    return [recipe.strip() for recipe in recipes if recipe.strip()]

def create_vector_database(recipes):
    if TRANSFORMERS_AVAILABLE and FAISS_AVAILABLE:
        # Orijinal yöntem
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(recipes)
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings.astype('float32'))
        return model, index, "transformers"
    else:
        # Alternatif TF-IDF yöntemi
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(recipes)
        return vectorizer, tfidf_matrix, "tfidf"

def search_similar_recipes(query, model, index, recipes, top_k=3):
    if isinstance(model, SentenceTransformer):
        # Transformers ile arama
        query_embedding = model.encode([query])
        distances, indices = index.search(query_embedding.astype('float32'), top_k)
        return [recipes[i] for i in indices[0]]
    else:
        # TF-IDF ile arama
        query_vec = model.transform([query])
        from sklearn.metrics.pairwise import cosine_similarity
        similarities = cosine_similarity(query_vec, index).flatten()
        indices = similarities.argsort()[-top_k:][::-1]
        return [recipes[i] for i in indices]

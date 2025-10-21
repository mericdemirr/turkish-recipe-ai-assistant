import streamlit as st
import google.generativeai as genai
from utils import load_and_split_recipes, create_vector_database, search_similar_recipes
import os
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()

# Sayfa ayarı
st.set_page_config(
    page_title="🧑‍🍳 Yemek Tarifi Asistanı",
    page_icon="🍳",
    layout="wide"
)

# Gemini API ayarı
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Veriyi yükle (cache'le daha hızlı çalışsın)
@st.cache_resource
def load_data():
    recipes = load_and_split_recipes("tarifler.txt")
    model, index = create_vector_database(recipes)
    return recipes, model, index

# Arayüz
st.title("🧑‍🍳 Malzemelerinle Yemek Tarifi Bul")
st.write("Elinizdeki malzemeleri yazın, size uygun tarifleri önerelim!")

# Malzeme girişi
user_ingredients = st.text_area(
    "Hangi malzemeler var?",
    placeholder="Örnek: kıyma, soğan, domates, patates, biber...",
    height=100
)

# Buton
if st.button("Tarifleri Bul 🚀") and user_ingredients:
    with st.spinner("En uygun tarifler aranıyor..."):
        try:
            # Veriyi yükle
            recipes, model, index = load_data()
            
            # Benzer tarifleri bul
            similar_recipes = search_similar_recipes(user_ingredients, model, index, recipes)
            
            # Gemini için prompt hazırla
            prompt = f"""
            Kullanıcının elindeki malzemeler: {user_ingredients}
            
            Aşağıdaki tariflerden, bu malzemelerle yapılabilecek en uygun olanı seç ve kullanıcıya göster.
            Sadece verilen tarifler arasından seçim yap.
            
            TARİFLER:
            {similar_recipes}
            
            Lütfen:
            1. En uygun tarifi seç
            2. Tarifin tam metnini olduğu gibi göster
            3. Başka yorum ekleme
            """
            
            # Gemini'ye sor
            model_genai = genai.GenerativeModel("gemini-2.5-flash")
            response = model_genai.generate_content(prompt)
            
            # Sonucu göster
            st.success("İşte size önerilen tarif:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {str(e)}")
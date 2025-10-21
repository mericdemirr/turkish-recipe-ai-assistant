# Yemek Tarifi Asistanı - AI-Powered Recipe Finder

Generative AI 101 Bootcamp için hazırlanmış Türkçe RAG (Retrieval-Augmented Generation) tabanlı yemek tarifi chatbot projesi.

## Proje Hakkında

Bu proje, RAG (Retrieval-Augmented Generation) mimarisi kullanarak geliştirilmiş bir yapay zeka yemek asistanıdır.  
Hugging Face'ten indirilen Türkçe yemek tarifleri veri setini kullanır.  
Kullanıcıların elindeki malzemeleri girerek, bu malzemelerle yapılabilecek en uygun tarifleri akıllı şekilde bulur ve önerir.

## Veri Seti Hakkında

**Kaynak:** [mertbozkurt/turkish-recipe](https://huggingface.co/datasets/mertbozkurt/turkish-recipe/tree/main)  
**Kullanım:** Veri seti indirilerek lokal olarak kullanılmıştır (`tarifler.txt`)  
**İçerik:** 5,000+ Türk mutfağı yemek tarifi  
**Lisans:** Açık kaynak - eğitim ve araştırma amaçlı kullanım  
**Veri Yapısı:**
```
Tarif Adı:
Malzemeler: [malzeme listesi]
Yapılışı: [adım adım tarif]
```

## Kullanılan Teknolojiler

- Scikit-learn: TF-IDF vektörleştirme ve cosine similarity  
- Streamlit: Web arayüzü  
- Google Gemini: Text generation modeli (gemini-2.5-flash)  
- Python-dotenv: Çevre değişkenleri yönetimi  

## Kurulum

### 1. Gerekli Paketleri Yükleyin

```bash
# Sanal ortam oluşturun
python -m venv yemek-env

# Ortamı aktif edin
# macOS / Linux
source yemek-env/bin/activate
# Windows
yemek-env\Scripts\activate

# Paketleri yükleyin
pip install -r requirements.txt
```

### 2. API Anahtarını Ayarlayın

Proje kök dizininde .env dosyası oluşturun ve aşağıdaki satırı ekleyin:

GEMINI_API_KEY=your_google_api_key_here

### 3. Veri Setini Hazırlayın

tarifler.txt dosyasını Hugging Face’ten indirin veya projedeki örnek veri setini kullanın.

### 4. Uygulamayı Çalıştırın

```bash
streamlit run app.py
```
Tarayıcınızda otomatik olarak açılacaktır (genellikle http://localhost:8501).
## Proje Yapısı
```
.
├── app.py              # Ana uygulama dosyası
├── utils.py            # Yardımcı fonksiyonlar
├── requirements.txt    # Python bağımlılıkları
├── tarifler.txt        # Yemek tarifleri veri seti (Hugging Face'ten)
├── .env                # API anahtarı (git'e eklenmez)
└── README.md           # Bu dosya
```
## Nasıl Çalışır?

1. **Veri yükleme:** `tarifler.txt` dosyasındaki yemek tarifleri yüklenir.  
2. **TF-IDF vektörleştirme:** Her tarif TF-IDF ile vektöre dönüştürülür.  
3. **Benzerlik arama:** Cosine similarity ile en benzer tarifler bulunur.  
4. **Yanıt üretimi:** Gemini modeli en uygun tarifi önerir.

## Örnek Kullanımlar

- "kıyma, soğan"
- "tavuk, pirinç"
- "kabak, kıyma"
- "patlıcan, biber"

## RAG Mimarisi
Kullanıcı Sorusu → TF-IDF Vektörleştirme → Cosine Similarity Arama → Benzer Tarifler → Gemini Optimizasyon → Sonuç

## Veri Seti İstatistikleri

- Toplam Tarif: 5,000+
- Kategori Sayısı: 15+ farklı yemek kategorisi
- Ortalama Malzeme Sayısı: 8-12
- Dil: Türkçe

## Sorun Giderme

ModuleNotFoundError hatası alıyorum:
```bash
pip install -r requirements.txt
```

API key hatası alıyorum:
- .env dosyasını kontrol edin
- Google AI Studio'dan yeni API key alın

Veri seti bulunamadı:
- tarifler.txt dosyasının proje klasöründe olduğundan emin olun
- Orijinal veri setini Hugging Face’ten indirebilirsiniz

Lisans
Bu proje eğitim amaçlıdır. Veri seti Hugging Face'ten alınmış olup orijinal lisans koşulları geçerlidir.

Katkıda Bulunma
Sorularınız veya önerileriniz için issue açabilirsiniz.

Canlı Demo
Canlı Uygulama Linki:
https://turkish-recipe-ai-assistant-c4qs8lgwlf492aj6bndfeh.streamlit.app/

Örnek kullanım:
kıyma, soğan
“Tarifleri Bul” butonuna tıklayın ve AI’nın önerisini izleyin.



# Yemek Tarifi Asistanı - AI-Powered Recipe Finder
Generative AI 101 Bootcamp için hazırlanmış Türkçe RAG (Retrieval-Augmented Generation) tabanlı yemek tarifi chatbot projesi.
## Proje Hakkında
Bu proje, RAG (Retrieval-Augmented Generation) mimarisi kullanarak geliştirilmiş bir yapay zeka yemek asistanıdır. Hugging Face'ten indirilerek yerel olarak kaydedilen Türkçe yemek tarifleri veri setini kullanır. Kullanıcıların elindeki malzemeleri girerek, bu malzemelerle yapılabilecek en uygun tarifleri akıllı bir şekilde bulur ve önerir.
## Veri Seti Hakkında
**Kaynak:** [mertbozkurt/turkish-recipe](https://huggingface.co/datasets/mertbozkurt/turkish-recipe/tree/main) - Hugging Face
**Kullanım:** Veri seti indirilerek lokal olarak kullanılmıştır (tarifler.txt)
**İçerik:** 5,000+ Türk mutfağı yemek tarifi
**Lisans:** Açık kaynak - eğitim ve araştırma amaçlı kullanım
**Veri Yapısı:**
Tarif Adı:
Malzemeler: [malzeme listesi]
Yapılışı: [adım adım tarif]
## Kullanılan Teknolojiler
FAISS: Vektör veritabanı
Streamlit: Web arayüzü
Sentence Transformers: Metin embedding modeli (all-MiniLM-L6-v2)
Google Gemini: Text generation modeli (gemini-2.0-flash)
Python-dotenv: Çevre değişkenleri yönetimi
## Kurulum
1.Gerekli Paketleri Yükleyin
# Virtual environment oluşturun
python -m venv yemek-env
source yemek-env/bin/activate  # macOS/Linux
yemek-env\Scripts\activate  # Windows
# Paketleri yükleyin
pip install -r requirements.txt
2.API Anahtarını Ayarlayın
Proje kök dizininde .env dosyası oluşturun:
GEMINI_API_KEY=your_google_api_key_here
3.Veri Setini Hazırlayın
# tarifler.txt dosyasını Hugging Face'ten indirin veya
# Örnek veri seti projeye dahil edilmiştir
4.Uygulamayı Çalıştırın
bash
streamlit run app.py
Tarayıcınızda otomatik olarak açılacaktır (genellikle http://localhost:8501).
## Proje Yapısı
.
├── app.py              # Ana uygulama dosyası
├── utils.py            # Yardımcı fonksiyonlar
├── requirements.txt    # Python bağımlılıkları
├── tarifler.txt        # Yemek tarifleri veri seti (Hugging Face'ten)
├── .env               # API anahtarı (git'e eklenmez)
└── README.md          # Bu dosya
## Nasıl Çalışır?
1.Veri Yükleme: Hugging Face'ten alınan Türkçe yemek tarifleri veri seti yüklenir
2.Belge İşleme: Tarifler "---" ayracı ile parçalara ayrılır
3.Embedding: Her tarif embedding modeli ile vektöre dönüştürülür
4.Vektör Veritabanı: Vektörler FAISS'te saklanır
5.Sorgulama: Kullanıcının malzemeleri embedding'e dönüştürülür ve en ilgili tarifler bulunur
6.Yanıt Üretimi: Gemini modeli, bulunan tariflerden yararlanarak optimize edilmiş tarif önerisi oluşturur
## Örnek Kullanımlar
- "kıyma, soğan, domates, patates"
- "tavuk, pirinç, havuç, bezelye"
- "kabak, kıyma, soğan, domates salçası"
- "patlıcan, biber, domates, sarımsak"
## Önemli Notlar
- İlk çalıştırmada embedding modeli indirilir, bu işlem birkaç dakika sürebilir
- Veri seti Hugging Face'ten alındığı için lisans koşullarına uygun kullanılmalıdır
- FAISS vektör veritabanı bellekte çalışır, büyük veri setleri için dikkatli olun
- Streamlit cache mekanizması sayesinde sonraki çalıştırmalarda hızlı başlar
##  RAG Mimarisi
text
Kullanıcı Sorusu → Embedding → FAISS Arama → Benzer Tarifler → Gemini Optimizasyon → Sonuç
## Veri Seti İstatistikleri
- Toplam Tarif: 5,000+
- Kategori Sayısı: 15+ farklı yemek kategorisi
- Ortalama Malzeme Sayısı: 8-12 malzeme
- Dil: Türkçe
## Sorun Giderme
ModuleNotFoundError hatası alıyorum
bash
pip install -r requirements.txt
API key hatası alıyorum
- .env dosyasını kontrol edin
- Google AI Studio'dan yeni API key alın
Veri seti bulunamadı
- tarifler.txt dosyasının proje klasöründe olduğundan emin olun
- Orijinal veri setini Hugging Face'ten indirebilirsiniz
##  Lisans
Bu proje eğitim amaçlıdır. Veri seti Hugging Face'ten alınmış olup orijinal lisans koşulları geçerlidir.
##  Katkıda Bulunma
Sorularınız veya önerileriniz için issue açabilirsiniz.
## Canlı Demo
bash
pip install -r requirements.txt

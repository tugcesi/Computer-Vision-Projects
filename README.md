# 🎨 Colour Recognition

Bu proje, görüntülerdeki renkleri **HSV (Hue, Saturation, Value)** renk modeli kullanarak tanıyan ve analiz eden bir Python uygulamasıdır.

## 📁 Proje Yapısı

```
Colour-Recognition/
├── app.py                  # Streamlit web uygulaması
├── ColourRecognition.ipynb # Jupyter Notebook analizi
├── colour.jpeg             # Örnek görüntü
├── result.png              # Örnek sonuç görseli
├── requirements.txt        # Python bağımlılıkları
└── README.md               # Proje dokümantasyonu
```

## 🚀 Kurulum

### 1. Repoyu klonlayın
```bash
git clone https://github.com/tugcesi/Colour-Recognition.git
cd Colour-Recognition
```

### 2. Bağımlılıkları yükleyin
```bash
pip install -r requirements.txt
```

## ▶️ Kullanım

### Streamlit Uygulaması
```bash
streamlit run app.py
```
Tarayıcınızda `http://localhost:8501` adresine gidin.

### Jupyter Notebook
```bash
jupyter notebook ColourRecognition.ipynb
```

## 🛠️ Özellikler

- 🖼️ Görüntü yükleme (JPG, PNG, BMP)
- 🎯 Gerçek zamanlı HSV kalibrasyon araçları
- 🎨 Renk maskesi oluşturma ve görselleştirme
- 📊 HSV histogram analizi
- 📋 Kullanıma hazır Python kodu üretme
- 🌈 Desteklenen renkler: Kırmızı, Mavi, Yeşil, Sarı, Pembe, Lacivert

## 📦 Gereksinimler

- Python 3.8+
- OpenCV
- Streamlit
- NumPy
- Pillow
- Matplotlib

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

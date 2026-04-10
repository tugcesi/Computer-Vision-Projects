import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="HSV Kalibrasyonu", layout="wide")
st.title("🎯 HSV Renk Kalibrasyonu Aracı")

st.markdown("""
Bu araç, görüntünüzdeki renklerin **gerçek HSV değerlerini** bulmanıza yardımcı olur.
Renkli bir görüntü yükleyin ve sonra **maskeleri görerek** HSV aralıklarını ayarlayın.
""")

# Sidebar'da ayarlamalar
st.sidebar.header("HSV Aralığı Ayarla")

# Renk seçimi
selected_color = st.sidebar.selectbox(
    "Kalibre etmek istediğiniz rengi seçin:",
    ['Kırmızı', 'Mavi', 'Yeşil', 'Sarı', 'Pembe', 'Lacivert', 'Özel']
)

# HSV slider'ları
st.sidebar.subheader("Hue (Ton)")
hue_lower = st.sidebar.slider("Hue Min", 0, 180, 0, key="hue_min")
hue_upper = st.sidebar.slider("Hue Max", 0, 180, 10, key="hue_max")

st.sidebar.subheader("Saturation (Doygunluk)")
sat_lower = st.sidebar.slider("Saturation Min", 0, 255, 50, key="sat_min")
sat_upper = st.sidebar.slider("Saturation Max", 0, 255, 255, key="sat_max")

st.sidebar.subheader("Value (Parlaklık)")
val_lower = st.sidebar.slider("Value Min", 0, 255, 50, key="val_min")
val_upper = st.sidebar.slider("Value Max", 0, 255, 255, key="val_max")

# Görüntü yükleme
uploaded_file = st.file_uploader("Bir görüntü yükleyin", type=['jpg', 'jpeg', 'png', 'bmp'])

if uploaded_file is not None:
    # Görüntüyü yükle
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    
    # Maske oluştur
    lower_hsv = np.array([hue_lower, sat_lower, val_lower])
    upper_hsv = np.array([hue_upper, sat_upper, val_upper])
    mask = cv2.inRange(image_hsv, lower_hsv, upper_hsv)
    
    # Sonuç görüntüsü
    result = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    
    # Göster
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Orijinal")
        st.image(image, use_container_width=True)
    
    with col2:
        st.subheader("Maske")
        st.image(mask, use_container_width=True, channels="GRAY")
    
    with col3:
        st.subheader("Sonuç")
        st.image(result_rgb, use_container_width=True)
    
    # İstatistikler
    st.subheader("📊 İstatistikler")
    
    # Maskedeki pikselleri say
    masked_pixels = cv2.countNonZero(mask)
    total_pixels = image_bgr.shape[0] * image_bgr.shape[1]
    percentage = (masked_pixels / total_pixels) * 100
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Algılanan Pikseller", f"{masked_pixels:,}")
    with col2:
        st.metric("Toplam Pikseller", f"{total_pixels:,}")
    with col3:
        st.metric("Yüzde", f"{percentage:.2f}%")
    
    # Ayarları kopyala
    st.subheader("📋 Python Kodu")
    code = f"""
lower_{selected_color.lower()} = np.array([{hue_lower}, {sat_lower}, {val_lower}])
upper_{selected_color.lower()} = np.array([{hue_upper}, {sat_upper}, {val_upper}])
"""
    st.code(code, language="python")
    st.info(f"💡 Bu aralığı ana programda kullanabilirsiniz!")
    
    # Histogram
    st.subheader("📈 HSV Histogramı")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 3))
    
    # Hue
    hist_h = cv2.calcHist([image_hsv], [0], mask, [180], [0, 180])
    axes[0].plot(hist_h)
    axes[0].axvline(hue_lower, color='r', linestyle='--', label='Min')
    axes[0].axvline(hue_upper, color='g', linestyle='--', label='Max')
    axes[0].set_title('Hue Histogram')
    axes[0].legend()
    axes[0].grid()
    
    # Saturation
    hist_s = cv2.calcHist([image_hsv], [1], mask, [256], [0, 256])
    axes[1].plot(hist_s)
    axes[1].axvline(sat_lower, color='r', linestyle='--', label='Min')
    axes[1].axvline(sat_upper, color='g', linestyle='--', label='Max')
    axes[1].set_title('Saturation Histogram')
    axes[1].legend()
    axes[1].grid()
    
    # Value
    hist_v = cv2.calcHist([image_hsv], [2], mask, [256], [0, 256])
    axes[2].plot(hist_v)
    axes[2].axvline(val_lower, color='r', linestyle='--', label='Min')
    axes[2].axvline(val_upper, color='g', linestyle='--', label='Max')
    axes[2].set_title('Value Histogram')
    axes[2].legend()
    axes[2].grid()
    
    plt.tight_layout()
    st.pyplot(fig)
    
else:
    st.info("👆 Lütfen yukarıdan bir görüntü yükleyin")
    
    with st.expander("📚 HSV Hakkında Bilgi"):
        st.write("""
        ### HSV Renk Modeli
        - **Hue (Ton)**: 0-180 arasında (Kırmızı=0, Yeşil=60, Mavi=120)
        - **Saturation (Doygunluk)**: 0-255 (0=Gri, 255=Saf renk)
        - **Value (Parlaklık)**: 0-255 (0=Siyah, 255=Parlak)
        
        ### Tipik HSV Aralıkları
        - **Kırmızı**: H=0-10 veya 170-180
        - **Yeşil**: H=35-85
        - **Mavi**: H=90-130
        - **Sarı**: H=15-35
        - **Pembe**: H=130-170
        - **Lacivert**: H=100-120
        """)
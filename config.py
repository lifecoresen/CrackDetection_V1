"""
Özel Konfigürasyon - Parametreleri Ayarlama
Çatlak ve nem tespiti hassasiyetini kontrol et
"""

# Çatlak Tespiti Parametreleri (Adaptive Threshold - İyileştirilmiş Yöntem)
CRACK_DETECTION_CONFIG = {
    # Yöntem seçimi: 'adaptive', 'canny' veya 'orb'
    'method': 'orb',  # 'canny', 'adaptive' veya 'orb'
    
    # Adaptive Threshold yöntemi parametreleri
    'blur_kernel': 3,              # Gaussian blur kernel (düşük = daha fazla detay)
    'adaptive_block': 15,          # Adaptive threshold block size
    'adaptive_constant': 3,        # Adaptive threshold sabit
    'morph_kernel': 3,             # Morfoloji kernel (küçük = ince çatlaklar)
    'morph_iterations': 1,         # Morfoloji işlem sayısı
    'min_contour_area': 50,        # Minimum kontur alanı (px²) - daha düşük
    
    # Şekil filtreleme parametreleri (boruları ayırt etmek için)
    'max_solidity': 0.3,           # Maksimum doluluk (düşük = çatlak, yüksek = boru)
    'max_aspect_ratio': 8.0,       # Maksimum en-boy oranı
    
    # ORB yöntemi parametreleri (yeni - gelişmiş)
    'orb_features': 2500,          # ORB feature sayısı - artırıldı
    'bilateral_d': 3,              # Bilateral filter diameter - düşürüldü
    'bilateral_sigma': 40,         # Bilateral filter sigma - düşürüldü
    'canny_threshold1': 20,        # Canny alt eşik - düşürüldü
    'canny_threshold2': 80,        # Canny üst eşik - düşürüldü
}

# Nem Tespiti Parametreleri
MOISTURE_DETECTION_CONFIG = {
    'dark_threshold': 80,        # Koyu alan eşiği (çok yüksek = sadece çok koyu)
    'min_region_area': 300,      # Minimum nem alanı (piksel²) - sadece büyük bölgeler
    'morphology_kernel': 7,      # Daha büyük kernel = büyük nemi tespit et
    'window_size': 21,           # Kontrast analizi pencere boyutu
}

# Görüntü Ön İşleme Parametreleri
PREPROCESSING_CONFIG = {
    'bilateral_filter_d': 5,      # Daha az filtreleme
    'bilateral_filter_sigma_color': 50,
    'bilateral_filter_sigma_space': 50,
    'clahe_clip_limit': 6.0,      # Maksimum kontrast iyileştirme
    'clahe_tile_size': (2, 2),    # Çok küçük tile = maksimum detay
    'resize_width': 800,
}

# Görselleştirme Parametreleri
VISUALIZATION_CONFIG = {
    'crack_color': (0, 255, 0),      # Yeşil - Çatlaklar
    'moisture_color': (0, 0, 255),   # Kırmızı - Nem
    'text_color': (255, 255, 255),   # Beyaz - Yazı
    'line_thickness': 2,
}

print("Konfigürasyon yüklendi!")

# 1. Gerekli kütüphaneleri yükleme
import pandas as pd
import matplotlib.pyplot as plt

# 2. Veri setini yükleme
df = pd.read_csv(r"D:\Python ile Veri Bilimi\python veri bilimi\heart.csv")

# İlk 5 satırı görüntüleyerek genel yapıyı kontrol et
print("İlk 5 Satır:")
print(df.head())

# Sütun isimlerini yazdıralım bi göz atalım
print("\nSütunlar:")
print(df.columns)

# 3. Eksik veri kontrolü
print("\nEksik Veri Kontrolü:")
print(df.isnull().sum())

# Eğer eksik veri olsaydı:
# df.fillna(df.mean(), inplace=True)  # Tüm sayısal eksikleri ortalama ile doldurur
# veya
# df.dropna(inplace=True)  # Eksik verili satırları siler

# 4. Temel istatistikler
print("\nTemel İstatistikler:")
print(df.describe())

# Ekstra: Hedef sütunundaki hasta ve sağlıklı kişi sayısı
print("\n'target' Sütununda Dağılım (1 = hasta, 0 = sağlıklı):")
print(df['target'].value_counts())

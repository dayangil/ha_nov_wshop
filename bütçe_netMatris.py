# -*- coding: utf-8 -*-

KUR = 55.0
SATIS_FIYATI_NET = 1395.0  # Tüm vergilerden arındırılmış net kişi başı fiyat

# 1. Sabit Giderler
sabit_giderler = {
    "Muhterem Hn. Eğitmen Ücreti": 1300.0,
    "Eduardo Eğitmen Ücreti": 1300.0,
    "Zeynep Organizasyon Ücreti": 800.0,
    "Eduardo Uçak Bileti": 450.0,
    "Workshop Malzemeleri (Toplam)": 300.0,
    "Toplam Vapur Ücreti (TL)": 1500.0 / KUR
}

# 2. Kişi Başı Değişken Giderler
birim_degisken_giderler = {
    "Konaklama": 95.0,
    "Havalimanı Transfer (TL)": 4000.0 / KUR,
    "Topkapı Sarayı (TL)": 2750.0 / KUR,
    "Gala Yemeği (TL)": 2000.0 / KUR,
    "İki Öğle Yemeği": 25.0,
    "Coffee Break": 20.0,
    "Toplu Ulaşım (TL)": 1000.0 / KUR,
    "Toplantı Salonu": 10.0,
    "Resim Heykel Müzesi (TL)": 550.0 / KUR,
    "Sertifika Baskısı (TL)": 100.0 / KUR,
    "Porselen Fayans (TL)": 100.0 / KUR
}

# Hesaplama Motoru
toplam_sabit_gider = sum(sabit_giderler.values())
kisi_basi_degisken_gider = sum(birim_degisken_giderler.values())
kadro_masraf_yuku = kisi_basi_degisken_gider * 3
kesin_sabit_maliyet = toplam_sabit_gider + kadro_masraf_yuku

senaryolar = [10, 12, 15]

# 1. BÖLÜM: MALIYET MATRISI TABLOSU
print("=" * 78)
print(f"{'GÜVENLİ GİDER VE MALİYET MATRİSİ (EURO)':^78}")
print("=" * 78)
print(f" {'Maliyet Kalemi':<35} | {'Euro Karşılığı':<16} | {'Maliyet Türü':<18} ")
print("-" * 78)

# Sabitleri listele
for kalem, deger in sabit_giderler.items():
    print(f" {kalem:<35} | {deger:12.2f} €    | {'Sabit Gider':<18}")

print("-" * 78)

# Değişkenleri listele
for kalem, deger in birim_degisken_giderler.items():
    print(f" {kalem:<35} | {deger:12.2f} €    | {'Değişken (Kişi Başı)':<18}")

print("-" * 78)
print(f" {'3 Kişilik Yönetim Kadrosu Toplam Yükü':<35} | {kadro_masraf_yuku:12.2f} €    | {'Sabit Havuzuna Ek':<18}")
print(f" {'KESİN SABİT MALİYET TOPLAMI':<35} | {kesin_sabit_maliyet:12.2f} €    | {'Kadro Dahil Sabit':<18}")
print(f" {'KİŞİ BAŞI DEĞİŞKEN MALİYET':<35} | {kisi_basi_degisken_gider:12.2f} €    | {'Katılımcı Başı Çarpan':<18}")
print("=" * 78)


# 2. BÖLÜM: NET KAR SENARYOLARI RAPORU
print(f"\n{'NET / VERGİSİZ / KOMİSYONSUZ WORKSHOP NET KÂR SENARYOLARI':^78}")
print("=" * 78)

for k in senaryolar:
    toplam_ciro = SATIS_FIYATI_NET * k
    katilimci_maliyeti = kisi_basi_degisken_gider * k
    toplam_operasyonel_maliyet = kesin_sabit_maliyet + katilimci_maliyeti
    net_kar = toplam_ciro - toplam_operasyonel_maliyet
    
    print(f"\n>>> SENARYO: {k} KATILIMCI <<<")
    print("-" * 50)
    print(f"Toplam Net Ciro                    : {toplam_ciro:10.2f} €")
    print(f"Toplam Katılımcı Değişken Gideri   : {katilimci_maliyeti:10.2f} €")
    print(f"Toplam Organizasyon Maliyeti       : {toplam_operasyonel_maliyet:10.2f} €")
    print("-" * 50)
    print(f"SİZE KALAN NET KÂR (%100)          : {net_kar:10.2f} €")
    print(f"Kişi Başına Düşen Net Kazancınız   : {net_kar/k:10.2f} €")
    print("=" * 78)

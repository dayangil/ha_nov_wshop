# -*- coding: utf-8 -*-

# Sabit Parametreler
KUR = 55.0
SATIS_FIYATI_BRUT = 1395.0  # KDV Dahil Kişi Başı Brüt Fiyat

# 1. Sabit Maliyetler (Katılımcı sayısından bağımsız direkt giderler)
sabit_giderler = {
    "Muhterem Hn. Eğitmen Ücreti": 1300.0,
    "Eduardo Eğitmen Ücreti": 1300.0,
    "Zeynep Organizasyon Ücreti": 800.0,
    "Eduardo Uçak Bileti": 450.0,
    "Workshop Malzemeleri (Toplam)": 300.0,
    "Toplam Vapur Ücreti (TL)": 1500.0 / KUR
}

# 2. Birim Değişken Maliyetler (Kişi başı çarpanlı giderler)
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

# Eğitmen/Yönetim kadrosunun (3 Kişi) organizasyona yüklediği değişken maliyet (Sabit havuzuna eklenir)
kadro_degisken_yuku = kisi_basi_degisken_gider * 3
net_sabit_yukumluluk = toplam_sabit_gider + kadro_degisken_yuku

senaryolar = [10, 12, 15]

print("=" * 75)
print("   İKTİSADİ İŞLETME + %10 DERNEK PAYLI WORKSHOP BÜTÇE RAPORU (EURO)")
print("=" * 75)

for k in senaryolar:
    # Ciro ve KDV Hesaplamaları
    brut_ciro = SATIS_FIYATI_BRUT * k
    kdv_tutari = brut_ciro - (brut_ciro / 1.20)
    net_ciro = brut_ciro - kdv_tutari
    
    # Gider Hesaplamaları
    katilimci_degisken_gideri = kisi_basi_degisken_gider * k
    toplam_gider = net_sabit_yukumluluk + katilimci_degisken_gideri
    
    # Vergilendirme
    vergi_matrahi = net_ciro - toplam_gider
    kurumlar_vergisi = vergi_matrahi * 0.25
    yasal_net_kar = vergi_matrahi - kurumlar_vergisi
    
    # Kâr Paylaşımı
    dernek_kar_payi = yasal_net_kar * 0.10
    kalan_net_kar = yasal_net_kar - dernek_kar_payi
    
    # Terminal Çıktısı
    print(f"\n>>> SENARYO: {k} KATILIMCI <<<")
    print("-" * 40)
    print(f"Toplam Brüt Ciro (KDV Dahil)       : {brut_ciro:10.2f} €")
    print(f"Ödenecek KDV (%20)                 : {kdv_tutari:10.2f} €")
    print(f"KDV Hariç Net Ciro                 : {net_ciro:10.2f} €")
    print("-" * 40)
    print(f"Toplam Sabit Maliyetler            : {net_sabit_yukumluluk:10.2f} € (Kadro Değişken Giderleri Dahil)")
    print(f"Toplam Katılımcı Değişken Maliyeti : {katilimci_degisken_gideri:10.2f} €")
    print(f"Toplam Operasyonel Gider (Maliyet) : {toplam_gider:10.2f} €")
    print("-" * 40)
    print(f"Vergi Matrahı (Dönem Kârı)         : {vergi_matrahi:10.2f} €")
    print(f"Kurumlar Vergisi (%25)             : {kurumlar_vergisi:10.2f} €")
    print(f"Yasal Net Kâr (Vergi Sonrası)       : {yasal_net_kar:10.2f} €")
    print("-" * 40)
    print(f"DERNEK KÂR PAYI (%10)              : {dernek_kar_payi:10.2f} €")
    print(f"SİZE KALAN NET KÂR (%90)           : {kalan_net_kar:10.2f} €")
    print(f"Kişi Başına Düşen Net Kazancınız   : {kalan_net_kar/k:10.2f} €")
    print("=" * 75)

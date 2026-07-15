# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt

# Sayfa Ayarları - Mobil dostu olması için geniş ekranı kapatıyoruz
st.set_page_config(page_title="Workshop Finansal Simülatör", layout="centered", page_icon="📊")

st.title("📊 Workshop Finansal Analiz Paneli")
st.markdown("Hem mobil hem masaüstü cihazlarla %100 uyumlu dinamik bütçe simülatörü.")

# MOBİL DOSTU PARAMETRE ALANI (Ana sayfada açılır kartlar)
with st.expander("⚙️ 1. Genel ve Finansal Ayarlar (Değiştirmek için Tıklayın)", expanded=True):
    KUR = st.number_input("Euro Kuru (1 € = X TL)", min_value=1.0, value=55.0, step=0.5)
    SATIS_FIYATI_BRUT = st.number_input("Kişi Başı Brüt Satış Fiyatı (€) [KDV Dahil]", min_value=100.0, value=1395.0, step=25.0)
    calisma_modu = st.selectbox(
        "Çalışma Modunu Seçiniz:",
        ["Vergisiz & Komisyonsuz (Net Elden)", "İktisadi İşletme (%20 KDV, %25 KV + %10 Dernek Payı)"]
    )

with st.expander("👥 2. Katılımcı Senaryoları Seçimi", expanded=False):
    st.markdown("Hesaplamak istediğiniz katılımcı sayılarını işaretleyin:")
    
    # Mobilde daha rahat seçilmesi için checkbox yerleşimi
    c10 = st.checkbox("10 Katılımcı", value=True)
    c12 = st.checkbox("12 Katılımcı", value=True)
    c15 = st.checkbox("15 Katılımcı", value=True)
    
    senaryo_secenekleri = list()
    if c10: senaryo_secenekleri.append(10)
    if c12: senaryo_secenekleri.append(12)
    if c15: senaryo_secenekleri.append(15)

# Maliyet Tanımlamaları
sabit_giderler = {
    "Muhterem Hn. Eğitmen Ücreti": 1300.0,
    "Eduardo Eğitmen Ücreti": 1300.0,
    "Zeynep Organizasyon Ücreti": 800.0,
    "Eduardo Uçak Bileti": 450.0,
    "Workshop Malzemeleri (Toplam)": 300.0,
    "Toplam Vapur Ücreti (TL)": 1500.0 / KUR
}

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

# Hesaplamalar
toplam_sabit_gider = sum(sabit_giderler.values())
kisi_basi_degisken_gider = sum(birim_degisken_giderler.values())
kadro_masraf_yuku = kisi_basi_degisken_gider * 3
kesin_sabit_maliyet = toplam_sabit_gider + kadro_masraf_yuku

# Ana Panel - Güvenli Gider ve Maliyet Matrisi
st.header("📋 Güvenli Gider ve Maliyet Matrisi")

# Mobilde alt alta düzgün görünmesi için yapılandırıldı
tab_sabit, tab_degisken = st.tabs(["📌 Sabit Giderler", "🔄 Kişi Başı Değişken Giderler"])

with tab_sabit:
    for k, v in sabit_giderler.items():
        st.write(f"• **{k}**: {v:.2f} €")
    st.markdown(f"**Yalın Sabit Toplamı:** {toplam_sabit_gider:.2f} €")

with tab_degisken:
    for k, v in birim_degisken_giderler.items():
        st.write(f"• **{k}**: {v:.2f} €")
    st.markdown(f"**Birim Değişken Toplamı:** {kisi_basi_degisken_gider:.2f} €")

st.info(f"💡 **Yönetim Kadrosu Yükü:** 3 Kişi x {kisi_basi_degisken_gider:.2f} € = **{kadro_masraf_yuku:.2f} €**")
st.success(f"🧮 **Kesin Sabit Maliyet (Kadro Dahil):** {kesin_sabit_maliyet:.2f} €")

# Senaryo Analizleri
st.header(f"📈 Sonuçlar: {calisma_modu}")

tablo_data = []
grafik_katilimci = []
grafik_kar = []

senaryo_secenekleri.sort()

for k in senaryo_secenekleri:
    brut_ciro = SATIS_FIYATI_BRUT * k
    katilimci_maliyeti = kisi_basi_degisken_gider * k
    toplam_gider = kesin_sabit_maliyet + katilimci_maliyeti
    
    if calisma_modu == "Vergisiz & Komisyonsuz (Net Elden)":
        kdv_tutari = 0.0
        kurumlar_vergisi = 0.0
        dernek_payi = 0.0
        net_kar = brut_ciro - toplam_gider
    else:
        kdv_tutari = brut_ciro - (brut_ciro / 1.20)
        net_ciro = brut_ciro - kdv_tutari
        vergi_matrahi = net_ciro - toplam_gider
        kurumlar_vergisi = max(0.0, vergi_matrahi * 0.25)
        yasal_net_kar = max(0.0, vergi_matrahi - kurumlar_vergisi)
        dernek_payi = yasal_net_kar * 0.10
        net_kar = yasal_net_kar - dernek_payi

    grafik_katilimci.append(f"{k} Kişi")
    grafik_kar.append(net_kar)
    
    # Mobilde tablonun taşmaması için sadeleştirilmiş görünüm
    tablo_data.append({
        "Katılımcı": f"{k} Kişi",
        "Brüt Ciro": f"{brut_ciro:,.0f} €",
        "Maliyet": f"{toplam_gider:,.0f} €",
        "NET KÂR": f"{net_kar:,.0f} €",
        "Kişi Başı Kazanç": f"{net_kar/k:,.0f} €"
    })

if tablo_data:
    st.table(tablo_data)

# Canlı Grafik Gösterimi
if grafik_kar:
    st.subheader("📊 Net Kâr Dağılımı")
    fig, ax = plt.subplots(figsize=(6, 3))
    bars = ax.bar(grafik_katilimci, grafik_kar, color=list(['#4CAF50','#2196F3','#FF9800']), edgecolor='gray')
    ax.set_ylabel('Net Kâr (€)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + (max(grafik_kar)*0.02 if max(grafik_kar) > 0 else 10), f'{yval:,.0f} €', 
                va='bottom', ha='center', fontsize=9, fontweight='bold')

    st.pyplot(fig)

# İŞ BİRLİĞİ SÖZLEŞME BUTONU
st.header("📝 Sanat Derneği İş Birliği Protokolü")
if st.button("📄 Resmi Sözleşme Taslağını Üret"):
    st.subheader("WORKSHOP ORGANİZASYON VE İŞ BİRLİĞİ PROTOKOLÜ")
    st.markdown(f"""
    **1. TARAFLAR**  
    İşbu protokol, bir tarafta faaliyetlerini yürüten **Workshop Organizasyon Komitesi** (YÜKLENİCİ) ile diğer tarafta **Sanat Derneği İktisadi İşletmesi** (DERNEK) arasında imzalanmıştır.
    
    **2. PROTOKOLÜN KONUSU**  
    YÜKLENİCİ tarafından organize edilen workshop etkinliğinin, DERNEK İktisadi İşletmesi çatısı altında faturalandırılması ve kâr paylaşım esaslarının belirlenmesidir.
    
    **3. MALİ ŞARTLAR VE VERGİLENDİRME**  
    * 3.1. Katılımcı kayıt bedeli kişi başı brüt **{SATIS_FIYATI_BRUT:.2f} € (KDV Dahil)** olarak belirlenmiştir. Sabit kur **1 Euro = {KUR:.2f} TL**'dir.
    * 3.2. Organizasyona ait tüm operasyonel giderler DERNEK İktisadi İşletmesi adına faturalandırılacaktır.
    """)
    
    if calisma_modu == "İktisadi İşletme (%20 KDV, %25 KV + %10 Dernek Payı)":
        st.markdown("""* 3.3. Tüm operasyonel giderler ve yasal %25 Kurumlar Vergisi düşüldükten sonra kalan Net Kâr üzerinden %10 DERNEK kâr payı kesintisi yapılacak, kalan %90 YÜKLENİCİ'ye aktarılacaktır.""")
    else:
        st.markdown("""* 3.3. İşbu çalışma bağış kapsamında değerlendirildiğinden, DERNEK herhangi bir kâr payı kesintisi yapmaksızın operasyonel giderler sonrası kalan tutarın %100'ünü YÜKLENİCİ'ye aktarır.""")
        
    st.markdown("""
    **4. YÜRÜRLÜK**  
    4 maddeden oluşan işbu protokol taraflarca imzalandığı tarihte yürürlüğe girer.  
    
    *İmza (Yüklenici)* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *İmza (Dernek Yetkilisi)*
    """)

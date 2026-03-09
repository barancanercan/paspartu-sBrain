import asyncio
import edge_tts

async def main():
    text = """
    Türkiye gündeminin özeti, 4 Mart 2026 sabahı. Son yirmi dört saatin en önemli gelişmeleri.

    Birinci konu: ÖZGÜR ÖZEL VE CHP. CHP Genel Başkanı Özgür Özel, partiyi yolsuzluk skandalının aktörleri olarak nitelendirdi ve önemli bir hamle yaptı. Ayrıca Özgür Özel'in marketleri tehdit ettiği iddiaları gündemde.

    İkinci konu: MANSUR YAVAŞ. Ankara Büyükşehir Belediye Başkanı Mansur Yavaş, tehdit karşısında birlik olunması gerektiğini vurguladı.

    Üçüncü konu: EKREM İMAMOĞLU. İstanbul Büyükşehir Belediye Başkanı Ekrem İmamoğlu, katledilen Fatma Nur öğretmen için başsağlığı mesajı paylaştı.

    Dördüncü konu: YSK. Yüksek Seçim Kurulu, 2025 nüfusuna göre vekil sayılarını açıkladı.

    Beşinci konu: SEÇİM HAZIRLIKLARI. Deniz Kuvvetleri 2. Bölgesi'nde erken seçimler için hazırlıklar yapıldığı haberleri geldi. Seçimlerin ulusal festivale dönüştürülmesi planlanıyor.

    Altıncı konu: ENFLASYON. Bloomberght'e göre küresel enflasyon şoku riski artıyor.

    Yedinci konu: KABİNE. AK Parti kurmayları İran'dan göç dalgası beklenmediğini açıkladı.

    Sekizinci konu: ANKARA BELEDİYESİ. Çankaya Belediyesi'nin dijital yüzü Çankapp yayına başladı.

    İşte sabah gündemi. Detaylar veritabanımızda.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/gundem_sabah.wav")

asyncio.run(main())
print("Bitti!")

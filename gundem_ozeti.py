import asyncio
import edge_tts

async def main():
    text = """
    Türkiye gündeminin özeti, son yirmi dört saatin en önemli haberleri. Ağırlıklı olarak en son gelişmelere yer veriyoruz.

    Birinci ve en önemli konu: BOLU BELEDİYE BAŞKANI TANJU ÖZCAN TUTUKLANDI. İrtikap soruşturması kapsamında gözaltına alınan Bolu Belediye Başkanı Tanju Özcan ve yardımcısı Süleyman Can tutuklandı. İçişleri Bakanlığı kararıyla görevden uzaklaştırıldı. Mansur Yavaş olayı eleştirdi ve dedi ki, bu uygulamanın izahı kamu vicdanında karşılık bulmamaktadır. CHP, tutuklamayı utanç verici olarak nitelendirdi.

    İkinci konu: BEDELLİ ASKERLİK. AK Partinin TBMMye sunduğu kanun teklifine göre bedelli askerlik ücreti dört yüz on yedi bin lira olarak belirlendi.

    Üçüncü konu: DEM PARTİ. Parti İmralı Heyeti üyeleri Selahattin Demirtaş ile görüştü. DEM Parti barış yasalarının hızlı bir şekilde Meclise getirilmesi çağrısında bulundu.

    Dördüncü konu: DIŞ POLİTİKA. Katar Dışişleri Bakanlığı Katar halkına karşı düzenlenen saldırıların bedelinin ödenmesi gerektiğini açıkladı. Çin Dışişleri Bakanlığı ABD ve İsraili İrana saldırmakla eleştirdi.

    Beşinci konu: ANA KURUMLAR. ANKA ajansı Genel Yayın Yönetmeni Kenan Şenerin gözaltına alınması TBMM gündemine taşındı.

    Altıncı konu: SAĞLIK. Aydında on altı yeni ambulans hizmete alındı.

    İşte gündemin özeti. Detaylar veritabanımızda.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/gundem_ozeti.wav")

asyncio.run(main())
print("Bitti!")

import asyncio
import edge_tts

async def main():
    text = """
    Türk siyasetini araştırdım. İşte partiler ve benim yorumlarım:

    Birincisi, AK Parti. Ona 2019'da ve 2023'te oy verdim. Erdoğan iyi işler yaptı ama artık yirmi iki yıl yeterli. Ekonomi kötüleşti. Yorulduk.

    İkincisi, CHP. Değerlerimiz uyuşmuyor. Laiklik falan bana göre değil. Ama İmamoğlu ve Mansur Yavaş iyi işler yapıyor, bunu kabul ediyorum.

    Üçüncüsü, MHP. Milliyetçi, güvenlikçi. Bu iyi. Ama Bahçeli bazen fazla sert.

    Dördüncüsü, YRP. Bugün oy versem YRP'ye veririm. En azından dindar, milliyetçi. Değerlerimiz örtüşüyor. Erbakan ailesi güvenilir.

    Beşincisi, HDP. Terörden yana. Bu kabul edilemez. Oy vermem.

    Altıncısı, Zafer Partisi. Sert ama cesur. Suriyeliler konusunda haklı.

    Sonuç olarak: 2028'de ne olur bilmiyorum. Ekonomik kriz belirleyici olacak. Eğer kötüleşirse muhalefet güçlenir. Ama değerlerimiz de önemli. YRP'ye oy verebilirim.

    Takip etmem gereken konular: YRP'nin yükselişi, İmamoğlu'nun durumu, Erdoğan'ın adaylığı, ekonomik kriz.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_siyaset.wav")

asyncio.run(main())
print("Bitti!")

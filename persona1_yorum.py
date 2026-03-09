import asyncio
import edge_tts

async def main():
    text = """
    Barış Terkoğlu'nun videosunu izledim. İran-ABD savaşı hakkındaydı. Türkiye'nin durumu, hedef alınıp alınmadığı konusunda bilgi veriyordu.

    Düşüncelerim şunlar: Güvenlik endişem var. Savaş çıkarsa ekonomi batar. Zaten yeterince kötüydü. Bir de savaş mı? 

    Orduya güveniyorum ama bu işler karışık. İran bize füze attı mı, hedef mi olduk? Bilmiyorum.

    Erdoğan güçlü duruyor, uyarıları yapıyor. ABD ile ilişkiler ne olacak? İran bizim komşumuz. Savaş istemiyoruz ama hazırlıklı olmalıyız.

    Kendi açımdan: İşlerim nasıl etkilenir? Antalya'da turizm ne olur? Zaten ekonomi en büyük sorunumuz. Savaş daha da kötü yapar.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_yorum.wav")

asyncio.run(main())
print("Bitti!")

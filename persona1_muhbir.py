import asyncio
import edge_tts

async def main():
    text = """
    Muhbir hesabının tweetlerini analiz ettim. İşte yorumlarım:

    Birincisi, akran zorbalığı. Yedi yaşında çocuk, kolu kırıldı. Bu çok üzücü. Aileler çocuklarını okula gönderiyor, güveniyor. Sonra böyle şeyler oluyor. Velilere de iş düşüyor.

    İkincisi, İspanyol TV meselesi. Yabancılar bizi yanlış tanıyor. İsteyen istediğini söylüyor. Bizim sesimiz çıkmıyor. 

    Üçüncüsü, HIV hastası. Adam hasta olmuş, tedavi olmaya çalışıyor. Eczacı nasıl böyle davranır? Toplumumuzda bilgi eksikliği var.

    Dördüncüsü, NATO üsleri. İsmail Saymaz doğru söylüyor. Ama savaş istemiyoruz. Komşularımızla kavga etmek istemiyoruz.

    Beşincisi, balistik füze. Nevşin Mengü ciddi bir iddia attı. Kimseye güvenemiyoruz artık. İsrail'e, Rusya'ya, ABD'ye... Hepsi kendi çıkarları için çalışıyor.

    Sonuç olarak: Muhbir iyi hesap. Dikkatli haberler paylaşıyor. Takip edilesi. Ama başka kaynaklardan da doğrulamak lazım.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_muhbir.wav")

asyncio.run(main())
print("Bitti!")

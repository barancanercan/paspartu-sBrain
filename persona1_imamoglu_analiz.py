import asyncio
import edge_tts

async def main():
    text = """
    İmamoğlu'nun tutuklanma sebeplerini detaylıca araştırdım. Şimdi kendi yorumumu yapayım.

    Birincisi, diploma meselesi. Otuz yıllık diploma nasıl iptal edilir? Bu bana çok garip geldi. Tam aday olacakken, tam seçimler öncesi böyle bir şey olması bence tesadüf değil.

    İkincisi, yolsuzluk suçlamaları. Belediyelerde yolsuzluk olur, bu yeni değil. Ama kanıt gerekli. Çok iddia var ama somut ne var bilmiyorum.

    Üçüncüsü, terör suçlaması. Bu çok ağır. Pkk ile işbirliği iddiası. Bu doğru mu bilmiyorum. Daha çok araştırmam lazım.

    Dördüncüsü, ekonomik etki. Dolar fırladı, borsa düştü, faizler yükseldi. Zaten kötü olan ekonomi daha da kötüleşti. Bu beni doğrudan etkiliyor.

    Beşincisi, muhalefet tepkileri. Hepsinin tek lafı: "Darbe" diyorlar. Bu ciddi bir suçlama.

    Altıncısı, uluslararası tepkiler. Avrupa birliği süreci durdu, Almanya silah vermedi. Bu Türkiye'nin aleyhine.

    Sonuç olarak: Kafam karışık. Bir yandan CHP'li, değerlerimle uyuşmuyor. Ama bu kadar ağır suçlamalar, bu kadar timing... Bence garip.

    Ekonomik kriz zaten her şeyi kötüleştiriyor. Bir de bu belirsizlik eklenince işler daha da karışıyor.

    2028'de ne olur bilmiyorum. Ama bu konuyu takip etmem lazım.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_imamoglu_analiz.wav")

asyncio.run(main())
print("Bitti!")

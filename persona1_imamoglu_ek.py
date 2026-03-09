import asyncio
import edge_tts

async def main():
    text = """
    İmamoğlu konusunda daha fazla araştırma yaptım. İşte bulduklarım:

    Birincisi, yolsuzluk kanıtları. Savcılık irtikap, rüşvet, ihaleye fesat, dolandırıcılık, kara para aklama gibi suçlamalar yöneltti. 48 kişi yolsuzluktan tutuklandı. Bu ciddi görünüyor.

    İkincisi, terör suçlaması. Pkk ile işbirliği iddiası vardı. Ama İmamoğlu terör suçlamasından serbest bırakıldı. Bu bana garip geldi. Ya kanıt yetersizdi, ya siyasi hesap vardı.

    Üçüncüsü, 2028 seçimleri. İmamoğlu şu an tutuklu olmasına rağmen CHP'nin cumhurbaşkanı adayı. 15.5 milyon oy aldı ön seçimde. Bu ciddi bir rakam. 2028'de ne olur bilmiyorum ama ekonomik kriz derinleşirse muhalefet güçlenebilir.

    Dördüncüsü, ekonomik etkiler. Dolar fırladı, borsa düştü, faizler yükseldi. Bu benim gibi esnafı directly etkiliyor.

    Sonuç olarak: Araştırmam devam edecek. Yolsuzluk davası ne zaman sonuçlanır? İmamoğlu seçim kazanır mı? Tutuklu seçilirse ne olur? Bunları takip etmem lazım.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_imamoglu_ek_ara.wav")

asyncio.run(main())
print("Bitti!")

import asyncio
import edge_tts

async def main():
    text = """
    Ekrem İmamoğlu'nun Silivri videosunu izledim. İstanbul Belediye Başkanı, hapishanedeki deneyimini anlatıyor.

    Düşüncelerim şunlar:

    Birincisi, adam CHP'li. Benim siyasi görüşümle tamamen ters. Ben muhafazakarım, YRP'ye oy vereceğim demiştim. Ama yine de izledim.

    İkincisi, hapishane kısmı ilginçti. Seçimler iptal edildi, yeniden seçildi, sonra hapse attılar. Bu doğru mu bilmiyorum ama "hapis" denilince insan düşünüyor.

    Üçüncüsü, muhafazakar değerler açısından: İmamoğlu dua ediyor, inançından bahsediyor. Bu beni rahatsız etmiyor. Ama partisi CHP. CHP'nin değerleri benimkilerle uyuşmuyor.

    Dördüncüsü, ekonomi ve belediyecilik: İstanbul'u iyi yönettiğini söylüyorlar. Metro, yollar, temizlik yapılmış. Ama ben Antalya'da yaşıyorum, İstanbul'u çok bilemiyorum.

    Beşincisi, 2028 seçimleri açısından: İmamoğlu aday olursa çok güçlü olur. CHP kazanır mı bilmiyorum. Ben YRP'ye oy vereceğim. Ama ekonomik kriz olursa her şey değişir.

    Sonuç olarak: Video güzel yapılmış, iyi konuşuyor. Ama benim oyum onda değil. Partisi ve değerleri benimkilerle uyuşmuyor.

    Eğer ekonomi daha da kötüleşirse, "en azından İmamoğlu ekonomiyi düzeltir" diyenler olabilir. O zaman durum değişebilir.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/persona1_imamoglu_yorum.wav")

asyncio.run(main())
print("Bitti!")

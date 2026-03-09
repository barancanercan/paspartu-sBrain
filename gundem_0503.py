import asyncio
import edge_tts

async def main():
    text = """
    Türkiye gündeminin özeti, 5 Mart 2026 sabahı. Son yirmi dört saatin en önemli gelişmeleri.

    Birinci konu: SEÇİM HAZIRLIKLARI. İl Seçim Komisyonu denetim ekipleri yerel yönetimlerdeki seçim hazırlık çalışmalarını denetliyor. Seçim merkezlerinde güvenli elektrik tedariki sağlanması gerektiği vurgulandı.

    İkinci konu: ÖZGÜR ÖZEL VE AKARYAKIT. CHP Genel Başkanı Özgür Özel'in dediği oldu. Akaryakıtta fiyat artışları ÖTV'den karşılanacak.

    Üçüncü konu: İMAMOĞLU. İstanbul Büyükşehir Belediye Başkanı Ekrem İmamoğlu'nun savunması ve adaylık tartışması gündemde. BBC'de geniş haber yayınlandı.

    Dördüncü konu: DIŞ POLİTİKA VE İRAN. Cumhurbaşkanı Erdoğan İran füzesi hakkında değerlendirme yaptı. Uyarıların en net biçimde yapıldığını söyledi. Dışişleri Bakanı Fidan TBMM'yi bilgilendirecek. TBMM Dışişleri Komisyonu Başkanı Fuat Oktay, Türkiye'yi kapsayan çatışma riski uyarısı yaptı.

    Beşinci konu: EKONOMİ. Hazine destekli kredi limiti 201 milyar lirayı aştı. Tahvillerde satış ve kaçış başladı. Piyasalarda savaş baskısı var. Körfez'le ticarette iptaller başladı, navlun üçe katlandı.

    Altıncı konu: İMRALI HEYETİ. İmralı Heyeti'nden iki bakana ziyaret gerçekleşti.

    Yedinci konu: DEM PARTİ. Ahmet Özer DEM Parti'yi ziyaret etti.

    İşte sabah gündemi. Detaylar veritabanımızda.
    """
    
    communicate = edge_tts.Communicate(
        text,
        "tr-TR-AhmetNeural",
        rate="+10%"
    )
    await communicate.save("/root/.openclaw/workspace/gundem_0503.wav")

asyncio.run(main())
print("Bitti!")

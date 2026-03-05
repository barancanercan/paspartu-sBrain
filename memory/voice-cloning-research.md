# Ses Klonlama Araştırması - 2026-03-03 Güncelleme

## Baran'ın Önerdiği Ücretsiz/Açık Kaynak Seçenekler

### 1. Kokoro-82M ✅ Denendi
- **Durum:** Kurulamadı - PyTorch 915MB gerektiriyor
- **Sorun:** CPU'da çalışsada, PyTorch kütüphanesi çok büyük
- **Sonuç:** ❌ Başarısız

### 2. Qwen3-TTS
- **GitHub:** https://github.com/QwenLM/Qwen3-TTS
- **Özellik:** 0.6B hafif model, CPU'da çalışabilir
- **Durum:** Henüz denenmedi

### 3. Kyutai Pocket TTS
- **Durum:** 2026'da çıkacak/henüz yayınlanmadı
- **Sonuç:** Henüz mevcut değil

### 4. Chatterbox (Resemble AI)
- **Kurulum:** `pip install chatterbox-tts`
- **Durum:** Henüz denenmedi

---

## Mevcut Durum

Bu sunucuda (CPU only):
- ❌ Gerçek ses klonlama yapılamıyor (GPU yok)
- ✅ Standart TTS çalışıyor (Edge-TTS ile)

## Öneri
Baran'ın bilgisayarında LM Studio veya Pinokio kullanarak Qwen3-TTS veya Kokoro-82M çalıştırması gerekiyor.

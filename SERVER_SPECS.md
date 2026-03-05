# Sunucu Özellikleri (CRITICAL)

## Donanım
| Özellik | Değer |
|---------|-------|
| **RAM** | 2.9 GB (Kullanılabilir: ~2.2 GB) |
| **CPU** | AMD EPYC |
| **Disk** | 7.8 GB (Doluluk: 65%) |
| **Swap** | Yok |

## Limitasyonlar
- ❌ GPU yok
- ❌ Ses klonlama modelleri çalışmıyor (RAM yetersiz)
- ❌ HuggingFace/GitHub'dan büyük dosya indirme (LFS) çalışmıyor
- ✅ Python pip paketleri çalışıyor
- ✅ eSpeak-NG çalışıyor
- ✅ Edge-TTS çalışıyor (en iyi ses)
- ✅ Clawhub kurulu

## Çalışan Çözümler
- **TTS:** Edge-TTS (Microsoft AhmetNeural - Türkçe erkek sesi)
- **Scraping:** Scrapling
- **CLI:** GitHub CLI (gh)

## Yapılacaklar
- GitHub auth yapılandırması
- Ses klonlama için GPU'lu sunucu gerekli

---

*Bu bilgi her zaman ön planda tutulmalı. Herhangi bir görev için önce bu spec'lere bak!*

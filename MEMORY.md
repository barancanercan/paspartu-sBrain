# MEMORY.md - Long-term Memory

## ⚠️ SUNUCU ÖZELLİKLERİ (ÖNEMLİ!)
**Detaylar:** `/root/.openclaw/workspace/SERVER_SPECS.md`
- RAM: 2.9 GB (yetersiz!)
- CPU: AMD EPYC
- GPU: Yok
- Ses klonlama: Çalışmıyor
- LFS indirme: Çalışmıyor

---

## About Baran (Güncellenmiş: 2026-03-05)

### İş ve Akademik Profil
- **İş:** Ankara Büyükşehir Belediyesi'nde Kıdemli Veri Bilimci
- **Deneyim:** 4+ yıl veri bilimi, son 1+ yıldır LLM odaklı
- **Eğitim:** İstatistik Yüksek Lisans (tezi NLP/AI odaklı)

### Sağlık Geçmişi (ÖNEMLİ!)
- **Kaza:** 20 Ağustos 2025'te trafik kazası geçirdi
- **İyileşme:** 126 günlük süreç
- **İşe Dönüş:** 24 Aralık 2025
- **Etkileri:** Odaklanma ve fiziksel enerji konusunda zorluklar yaşıyor

---

### Aktif Projeler

**1. Microcosmos** (En aktif)
- Türk vatandaşlarının anket verilerine dayalı persona simülasyon platformu
- Sanal kahvehane ortamında persona etkileşimi
- Mini-Microcosmos: FastAPI + React + Ollama (yerel LLM)

**2. OpenClaw**
- KiloClaw VPS üzerinde çalışıyor
- Scrapling Python kütüphanesi entegre
- Zamanlanmış görevler + Markdown raporlar

**3. PageGeneralOCR**
- Türk askeri tarihi belgeleri analizi
- Gemini 2.5 Pro ile Türkçe tarihsel analiz

**4. Meclis İstihbarat Sistemi**
- Meclis/belediye meclis üyelerinin sosyal medya analizi
- Green/Red/Grey team agent mimarisi
- Gemma3 ile CPU-only çalışıyor

**5. Türk Siyasi LLM Benchmark**
- GLUE, SQuAD, XNLI referanslı Türkçe siyasi LLM değerlendirme

---

### Teknik Tercihler
- **Yerel LLM:** Ollama, Qwen2.5, Gemma3
- **Anti-bot scraping:** Selenium, undetected-chromedriver, Playwright
- **CLI:** Claude Code CLI
- **Tarz:** Pratik, over-engineering'den kaçınan, yerel çözümler

---

### Tanınan Başarılar
- **2024 Ankara seçim tahmin modeli:** %98.8 doğruluk
  - "Cozmic Bazaar Theory" ve multi-agent persona simülasyonları ile
- **Şeffaf Ankara:** Türkiye'nin ilk harita tabanlı açık veri platformu
- **Veri İzleme Koordinatörlüğü:** Türk seçimleri için

---

### İlgi Alanları
- Türk siyasi analizi
- Sivil teknoloji
- AI araştırmaları (Two Minute Papers takip)
- Psikolojik savaş ve algı yönetimi kitapları
- GitHub'da aktif
- Medium'da teknik makaleler

---

### Diğer Projeler (Takip Edilecek)
- mizan-ai: Tool-Augmented RAG Multi-Agent Platform
- Jarvis / News Intelligence Agent
- YÖK-Dil sınavı hazırlığı (İngilizce hedefler)
- Medium: "İleri Seviye Prompt Engineering Teknikleri" blog serisi

---

## Sleep Pattern
- **Typical sleep:** ~23:00 - ~08:00
- **Notes:** Sleeps late at night, doesn't wake up early
- **Important:** Don't disturb between 23:00-08:00 unless urgent

---

## Setup Log
- 2026-03-02: Initial setup - identity and user info configured
- 2026-03-02: Avatar created - robot image from Baran
- 2026-03-02: Scrapling skill installed, cron jobs configured (07:30 scraping, 09:00 report)
- 2026-03-02: Voice cloning research started
- 2026-03-03: Edge-TTS working (AhmetNeural - Turkish male voice)
- 2026-03-03: ClawHub installed with multiple skills
- 2026-03-03: News Intelligence Agent installed (news-intelligence-agent)
- 2026-03-03: Daily news cron job set (08:00 TR)
- 2026-03-05: Persona sistemi kuruldu, Türk siyaseti araştırıldı
- 2026-03-10: Gündem sistemi düzeltildi - web_fetch + HEARTBEAT kullanılıyor (ücretsiz)

## Skills to Configure
- GitHub CLI
- 1Password CLI

## Persona Sistemi
- Detaylı mimari: memory/persona_sistem_arsiv.md
- Aktif persona: persona1 (35-44 yaş, erkek, muhafazakar, Antalya)
- TGSS veritabanı ile besleniyor

## Bugünkü Çalışmalar (2026-03-05)
- İmamoğlu tutuklanması detaylı araştırması
- Türk siyasi partiler analizi
- @ajansmuhbir1923 tweetleri analizi

---

## Yüklü Skill'ler (ClawHub)

Toplam: 12 skill yüklü

| Skill | Versiyon | Kuruluş |
|-------|----------|---------|
| self-improving | 1.1.3 | 2026-03-02 |
| openai-whisper | 1.0.0 | 2026-03-02 |
| humanizer | 1.0.0 | 2026-03-02 |
| youtube-watcher | 1.0.0 | 2026-03-02 |
| chirp | 1.0.1 | 2026-03-02 |
| github | 1.0.0 | 2026-03-03 |
| automation-workflows | 0.1.0 | 2026-03-03 |
| agent | 1.0.0 | 2026-03-03 |
| x-post-automation | 1.0.0 | 2026-03-03 |
| openclaw-github-assistant | 2.0.1 | 2026-03-03 |
| multi-agent-collaboration | 1.0.0 | 2026-03-03 |
| scrapling | (manuel) | 2026-03-02 |

**Not:** self-improving-agent (https://clawhub.ai/pskoett/self-improving-agent) ZATEN KURULU!

---

## GitHub Repolar

- **Ana repo:** https://github.com/barancanercan/paspartu-sBrain
  - Workspace dosyaları (personas, memory, skills)
  - Otomatik push: Her 6 saat

- **news-intelligence-agent:** Baran'ın haber toplama sistemi
  - Konum: /root/.openclaw/workspace/news-intelligence-agent/
  - Ayrı repo olarak tutuluyor (submodule değil)

---

## ClawHub Konfigürasyonu
- Konum: /root/.openclaw/workspace/.clawhub/lock.json

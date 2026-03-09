import requests

# HuggingFace CDN link
url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/tr/tr_TR/fahrettin/medium/tr_TR-fahrettin-medium.onnx"

print("İndirme başlıyor...")

try:
    with requests.get(url, stream=True, allow_redirects=True, timeout=60) as r:
        r.raise_for_status()
        with open("/root/.openclaw/workspace/piper/tr_TR-fahrettin-medium.onnx", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("Başarili!")
except Exception as e:
    print(f"Hata: {e}")

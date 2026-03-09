import asyncio
import edge_tts

async def main():
    communicate = edge_tts.Communicate(
        "Merhaba! Benim adım Paspartu. Sonunda seni duyabiliyorum!",
        "tr-TR-AhmetNeural"  # Türkçe erkek sesi
    )
    await communicate.save("/root/.openclaw/workspace/edge_test.wav")

asyncio.run(main())
print("Bitti!")

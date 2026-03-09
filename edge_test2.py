import asyncio
import edge_tts

async def main():
    communicate = edge_tts.Communicate(
        "Merhaba! Benim adım Paspartu. Artık seninle daha hızlı konuşabiliyorum!",
        "tr-TR-AhmetNeural",
        rate="+20%"  # %20 daha hızlı
    )
    await communicate.save("/root/.openclaw/workspace/edge_test2.wav")

asyncio.run(main())
print("Bitti!")

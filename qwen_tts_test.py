#!/usr/bin/env python3
"""Qwen3-TTS voice cloning script"""

import torch
from qwen_tts import Qwen3TTSModel

# Reference voice
ref_voice = "/root/.openclaw/workspace/reference_voice.mp3"
output_file = "/root/.openclaw/workspace/cloned_voice.wav"

print("Loading Qwen3-TTS model (0.6B)...")
# device parametresi kaldırıldı - .to("cpu") ile yapacağız
model = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice")
model.to("cpu")  # CPU'ya taşı

print("Generating voice with your reference...")
# Türkçe metin
text = "Merhaba Baran! Ben Paspartu, senin sesinle konusuyorum!"

audio = model.generate_custom_voice(
    text=text,
    language="turkish",
    speaker_wav=ref_voice
)

# Save audio
import scipy.io.wavfile as sfr
sfr.write(output_file, 24000, audio)

print(f"Done! Saved to: {output_file}")

#!/usr/bin/env python3
"""Kokoro-82M ONNX voice cloning script"""

from kokoro_onnx import Kokoro
import soundfile as sf

# Reference voice
ref_voice = "/root/.openclaw/workspace/reference_voice.mp3"
output_file = "/root/.openclaw/workspace/cloned_voice.wav"

print("Loading Kokoro model...")
kokoro = Kokoro("kokoro-v1.0.onnx", "voices.json")

print("Generating voice...")
text = "Merhaba Baran! Ben Paspartu, senin sesinle konusuyorum!"

# Türkçe erkek sesi - tm_mert veya tm_kerem
samples, sample_rate = kokoro.create(
    text,
    voice="tm_mert",
    speed=1.0,
    lang="tr"
)

# Save audio
sf.write(output_file, samples, sample_rate)

print(f"Done! Saved to: {output_file}")

#!/usr/bin/env python3
"""Voice cloning script using Coqui TTS"""

from TTS.api import TTS
import os

# Reference voice file
ref_voice = "/root/.openclaw/workspace/reference_voice.mp3"
output_file = "/root/.openclaw/workspace/cloned_voice.wav"

# Test text
text = "Merhaba Baran! Ben Paspartu, sesinle konuşuyorum!"

print("Loading TTS model...")
# Using a multilingual model
tts = TTS(model_name="multilingual", gpu=False)

print("Cloning voice from reference...")
tts.tts_to_file(
    text=text,
    speaker_wav=ref_voice,
    language="tr",
    file_path=output_file
)

print(f"Voice cloned! Output: {output_file}")

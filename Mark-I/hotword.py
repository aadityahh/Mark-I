import pvporcupine
import pyaudio
import struct
import os
from dotenv import load_dotenv
load_dotenv()

is_awake=False

porcupine=pvporcupine.create(
    access_key=os.getenv("PORCUPINE_ACCESS_KEY"),
    keyword_paths=["hey-mark_en_windows_v4_0_0.ppn"]
)
pa = pyaudio.PyAudio()
stream=pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

def listen_for_hotword():
    pcm=stream.read(porcupine.frame_length, exception_on_overflow=False)
    pcm=struct.unpack_from("h"*porcupine.frame_length, pcm)

    result=porcupine.process(pcm)
    if result>=0:
        return True
    return False
    
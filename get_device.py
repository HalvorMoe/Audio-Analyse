import pyaudio
import numpy as np

p = pyaudio.PyAudio()
print(p.get_device_info_by_index(7))
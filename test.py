import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation


channel = 1
Sample_rate = 44100
device = 2
frames_buffer = 512
duration = 2

# Audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=channel, rate=Sample_rate, input=True, input_device_index=device, frames_per_buffer=frames_buffer)

t = np.linspace(0, duration, Sample_rate * duration, endpoint=False)

while True:
    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    print(data)
stream.stop_stream()
stream.close()
p.terminate()
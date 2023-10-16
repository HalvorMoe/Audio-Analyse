import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of audio channels
RATE = 44100  # Sampling Rate in Hz
CHUNK = 1024  # Number of frames per buffer
DEVICE = 2    # Which audio device to use

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=DEVICE,
                frames_per_buffer=CHUNK)

# Create a figure and axes
fig, ax = plt.subplots()
x = np.linspace(0, RATE//2, CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(0, 255)
ax.set_xlim(0, RATE//2)

def update(frame):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    yf = np.fft.fft(data)
    line.set_ydata(np.abs(yf[0:CHUNK])  / (128 * CHUNK))
    return line,

# Create an animation
ani = FuncAnimation(fig, update, blit=True)

# Show the plot
plt.show()
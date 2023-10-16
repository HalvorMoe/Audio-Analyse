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

# Create a figure and axis
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(0, 255)

def update(frame):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    print(data)
    line.set_ydata(data)
    return line,

# Create an animation
ani = FuncAnimation(fig, update, blit=True)

# Show the plot
plt.show()
import sounddevice as sd
from scipy.io.wavfile import write

# Define recording parameters
time = 5  # Recording duration in seconds
fs = 44100  # Sampling rate

# Record audio
print("Recording...")
recording = sd.rec(int(time * fs), samplerate=fs, channels=2)
sd.wait()
print("Recording completed!")

# Save recording as WAV file
filename = "voice_recording.wav"
write(filename, fs, recording)

print(f"Recording saved as: {filename}")

import librosa
import numpy as np
from tensorflow.keras.models import load_model
from playsound import playsound
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Load trained model
model = load_model("results/siren_model.h5")

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# Open file dialog for user to upload audio
print("📂 Please select an audio file")

Tk().withdraw()  # hide main tkinter window
audio_file = askopenfilename(
    title="Select Audio File",
    filetypes=[("WAV files", "*.wav")]
)

if not audio_file:
    print("❌ No file selected")
    exit()

print("Selected File:", audio_file)

# Extract features
features = extract_features(audio_file)
features = features.reshape(1, -1)

# Predict
prediction = model.predict(features)

print("Raw Prediction:", prediction)

siren_probability = prediction[0][0]

print("Siren Probability:", siren_probability)

# Decision
if siren_probability > 0.5:
    print("🚑 Siren Detected")
else:
    print("❌ Non Siren")

# Always play the uploaded audio
print("🔊 Playing audio...")
playsound(audio_file)
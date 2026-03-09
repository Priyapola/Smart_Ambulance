print("✅ RUNNING NEW MULTI-FILE TEST")

import librosa
import numpy as np
from tensorflow.keras.models import load_model

# ✅ Correct path (parent folder)
model = load_model("../models/audio_ann.h5")

def extract_mfcc(file_path):
    audio, sr = librosa.load(file_path, duration=3)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# ✅ Test siren vs traffic
test_files = [
    ("SIREN", "../datasets/sounds/siren/ambulance/sound_10.wav"),
    ("TRAFFIC", "../datasets/sounds/non_siren/traffic/sound_401.wav")
]

for label, file_path in test_files:
    features = extract_mfcc(file_path)
    prob = model.predict(np.expand_dims(features, axis=0))[0][0]
    print(f"{label} → Probability = {prob:.4f}")

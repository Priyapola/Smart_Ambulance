import os
import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import Callback

# ==============================
# CREATE RESULTS FOLDER
# ==============================

os.makedirs("results", exist_ok=True)

# ==============================
# DATASET PATHS
# ==============================

DATASET_PATH = "dataset/UrbanSound8K"
AUDIO_PATH = os.path.join(DATASET_PATH, "audio")
METADATA_PATH = os.path.join(DATASET_PATH, "metadata", "UrbanSound8K.csv")

print("Loading metadata...")
metadata = pd.read_csv(METADATA_PATH)

# ==============================
# FEATURE EXTRACTION
# ==============================

def extract_features(file_path):

    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    return np.mean(mfcc.T, axis=0)

features = []
labels = []

print("Extracting features from audio...")

for index, row in metadata.iterrows():

    file_name = row["slice_file_name"]
    fold = "fold" + str(row["fold"])
    class_id = row["classID"]

    file_path = os.path.join(AUDIO_PATH, fold, file_name)

    try:

        data = extract_features(file_path)

        # Siren classID = 8
        label = 1 if class_id == 8 else 0

        features.append(data)
        labels.append(label)

    except:
        pass

X = np.array(features)
y = np.array(labels)

print("Dataset shape:", X.shape)

# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================
# CUSTOM METRICS TRACKER
# ==============================

precision_history = []
recall_history = []
f1_history = []

class MetricsCallback(Callback):

    def on_epoch_end(self, epoch, logs=None):

        y_pred = self.model.predict(X_test)

        y_pred_classes = (y_pred > 0.5).astype(int).flatten()

        precision = precision_score(y_test, y_pred_classes)
        recall = recall_score(y_test, y_pred_classes)
        f1 = f1_score(y_test, y_pred_classes)

        precision_history.append(precision)
        recall_history.append(recall)
        f1_history.append(f1)

# ==============================
# BUILD MODEL
# ==============================

print("Building model...")

model = Sequential()

model.add(Dense(256, input_shape=(40,), activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))

model.compile(

    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ==============================
# TRAIN MODEL
# ==============================

print("Training model...")

history = model.fit(

    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[MetricsCallback()]
)

# ==============================
# SAVE MODEL
# ==============================

model.save("results/siren_model.h5")

print("Model saved.")

# ==============================
# FINAL EVALUATION
# ==============================

y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int).flatten()

accuracy = accuracy_score(y_test, y_pred_classes)
precision = precision_score(y_test, y_pred_classes)
recall = recall_score(y_test, y_pred_classes)
f1 = f1_score(y_test, y_pred_classes)

print("\nFinal Results")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

# ==============================
# CONFUSION MATRIX
# ==============================

cm = confusion_matrix(y_test, y_pred_classes)

plt.figure()

sns.heatmap(cm, annot=True, fmt="d")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("results/confusion_matrix.png")
plt.clf()

# ==============================
# ACCURACY CURVE
# ==============================

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title("Accuracy Curve")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend(["Train", "Validation"])

plt.savefig("results/accuracy_curve.png")
plt.clf()

# ==============================
# PRECISION CURVE
# ==============================

plt.plot(precision_history)

plt.title("Precision Curve")
plt.xlabel("Epoch")
plt.ylabel("Precision")

plt.savefig("results/precision_curve.png")
plt.clf()

# ==============================
# RECALL CURVE
# ==============================

plt.plot(recall_history)

plt.title("Recall Curve")
plt.xlabel("Epoch")
plt.ylabel("Recall")

plt.savefig("results/recall_curve.png")
plt.clf()

# ==============================
# F1 SCORE CURVE
# ==============================

plt.plot(f1_history)

plt.title("F1 Score Curve")
plt.xlabel("Epoch")
plt.ylabel("F1 Score")

plt.savefig("results/f1_score_curve.png")
plt.clf()

# ==============================
# COMBINED METRICS GRAPH
# ==============================

plt.plot(history.history['accuracy'], label="Accuracy")
plt.plot(precision_history, label="Precision")
plt.plot(recall_history, label="Recall")
plt.plot(f1_history, label="F1 Score")

plt.title("Model Performance Metrics")
plt.xlabel("Epoch")
plt.ylabel("Score")

plt.legend()

plt.savefig("results/combined_metrics.png")
plt.clf()

print("\nAll graphs saved inside RESULTS folder.")
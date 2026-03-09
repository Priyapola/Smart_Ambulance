# TODO.md — Smart Ambulance Detection (PC-only prototype)

**Source:** Read @"Smart" (Smart.pptx) — project brief and literature review included.

---

## Goal (one line)

Build a **PC-only demo** (no Raspberry Pi required) that detects ambulances from CCTV/video (YOLOv8) and detects sirens from audio (MFCC + NN), then simulates traffic-signal control via a local Flask web UI.

---

## High-level plan (checked off as we complete)

* [ ] **0. Read @Smart** — Confirmed I read Smart.pptx and used it as reference for scope and requirements.

### Setup & infra

* [ ] **1. Environment setup** (venv, core packages)

  * Files: `steps.md` (setup steps), `.gitignore`
  * Acceptance: `venv` created + `pip install -r requirements.txt` works

### Data collection & preprocessing

* [ ] **2. Vision dataset** (collect / annotate)

  * Collect ambulance images/videos, annotate with LabelImg/Roboflow, YOLO format.
  * Files: `datasets/vision/...`, `src/prepare_vision_data.py`
  * Acceptance: 200+ labeled images or link to public dataset.

* [ ] **3. Audio dataset** (siren and non-siren)

  * Collect UrbanSound8K or recorded clips, normalize, split to folders.
  * Files: `datasets/audio/...`, `src/prepare_audio_data.py`
  * Acceptance: 100+ clips total, balanced classes.

### Models (training & inference)

* [ ] **4. Vision — quick inference (pretrained YOLOv8)**

  * File: `src/vision_infer.py`
  * Acceptance: bounding boxes show ambulance detection on sample video.

* [ ] **5. Vision — train on custom data (YOLOv8)**

  * File: `src/vision_train.py`, `src/data.yaml`
  * Acceptance: model trained and `runs/train/exp/weights/best.pt` produced.

* [ ] **6. Audio — feature extraction & training**

  * Files: `src/audio_features.py`, `src/audio_train.py`
  * Acceptance: model saved at `models/audio_ann.h5`, validation accuracy >80%.

* [ ] **7. Audio — live/sliding-window inference**

  * File: `src/audio_infer.py`
  * Acceptance: outputs siren probability and triggers after debounced positives.

### Integration & Demo (PC-only simulation)

* [ ] **8. Integration server (Flask)**

  * File: `src/integration_server.py`
  * UI in `src/traffic_ui/index.html`
  * Acceptance: UI shows green when detection is reported.

* [ ] **9. Connect detectors to server**

  * Add POST request from `vision_infer.py` & `audio_infer.py` to `/report_detection`.
  * Acceptance: end-to-end demo works on PC.

* [ ] **10. Route planner (optional)**

  * File: `src/route_planner.py` using networkx/osmnx.
  * Acceptance: computes a route with mock congestion.

### Testing, docs & security

* [ ] **11. Test cases & evaluation**

  * Deliverable: sample videos/audios in `tests/` + metrics.
  * Acceptance: documented accuracy, mAP, latency.

* [ ] **12. Documentation & dev notes**

  * Files: `README.md`, `dev.md`, `steps.md`, and this `todo.md` review section.
  * Acceptance: clear runbook to reproduce demo locally.

* [ ] **13. Security & production checklist**

  * Add checklist in `dev.md`.
  * Ensure no secrets, proper validation, no debug endpoints in production.

### Cleanup & delivery

* [ ] **14. Packaging & demo assets**

  * Deliverable: sample video/audio + demo video + instructions.
  * Acceptance: 2–3 min demo video showing system.

---

## Principles

* Keep everything PC-only (no Raspberry Pi hardware needed).
* Minimal, simple, well-commented scripts.
* Security-first: no secrets, safe endpoints.
* Follow "simplicity-first" approach: build MVPs, avoid complexity.

---

## Files to be created

* `src/vision_infer.py`
* `src/vision_train.py`
* `src/audio_features.py`
* `src/audio_train.py`
* `src/audio_infer.py`
* `src/integration_server.py`
* `src/traffic_ui/index.html`
* `steps.md`
* `dev.md`
* `README.md`

---

## steps.md (mini quickstart)

1. Create & activate virtualenv.
2. `pip install -r requirements.txt`.
3. Run `python src/integration_server.py`.
4. In separate terminals run `python src/vision_infer.py` and `python src/audio_infer.py`.
5. Open [http://localhost:5000](http://localhost:5000) → see traffic light simulation.

---

## Review section (to fill later)

* Summary of changes made, timestamps, files edited, security checks performed.

---




27-09-25

# TODO.md — Smart Ambulance Detection (PC-only prototype)

**Source:** Read @"Smart" (Smart.pptx) — project brief and literature review included.

---

## Goal (one line)

Build a **PC-only demo** (no Raspberry Pi required) that detects ambulances from CCTV/video (YOLOv8) and detects sirens from audio (MFCC + NN), then simulates traffic-signal control via a local Flask web UI.

---

## High-level plan (checked off as we complete)

* ✅ **0. Read @Smart** — Confirmed I read Smart.pptx and used it as reference for scope and requirements.

### Setup & infra

* ✅ **1. Environment setup** (venv, core packages)

  * Files: `steps.md` (setup steps), `.gitignore`
  * Acceptance: `venv` created + `pip install -r requirements.txt` works

### Data collection & preprocessing

* ✅ **2. Vision dataset** (collect / annotate)

  * Used **Roboflow ambulance dataset (version 20)**, YOLO format.
  * Organized into `datasets/vision/images/{train,val}` and `datasets/vision/labels/{train,val}`.
  * Configured `data.yaml`.
  * Files: `datasets/vision/...`
  * Acceptance: ✅ dataset prepared.

* [ ] **3. Audio dataset** (siren and non-siren)

  * TODO: Collect UrbanSound8K or other siren dataset.
  * Files: `datasets/audio/...`, `src/prepare_audio_data.py`
  * Acceptance: 100+ clips total, balanced classes.

### Models (training & inference)

* ✅ **4. Vision — quick inference (pretrained YOLOv8)**

  * File: `src/vision_infer.py`
  * ✅ Tested pretrained YOLOv8 (`yolov8n.pt`) on sample images → bounding boxes worked.

* 🟡 **5. Vision — train on custom data (YOLOv8)**

  * File: `src/vision_train.py`, `datasets/vision/data.yaml`
  * ✅ Training launched with absolute path fix.
  * ⏳ Training in progress (currently epoch 4/20).
  * Expected: `runs/train/exp/weights/best.pt`.

* [ ] **6. Audio — feature extraction & training**

  * Files: `src/audio_features.py`, `src/audio_train.py`
  * Acceptance: model saved at `models/audio_ann.h5`, validation accuracy >80%.

* [ ] **7. Audio — live/sliding-window inference**

  * File: `src/audio_infer.py`
  * Acceptance: outputs siren probability and triggers after debounced positives.

### Integration & Demo (PC-only simulation)

* [ ] **8. Integration server (Flask)**

  * File: `src/integration_server.py`
  * UI in `src/traffic_ui/index.html`
  * Acceptance: UI shows green when detection is reported.

* [ ] **9. Connect detectors to server**

  * Add POST request from `vision_infer.py` & `audio_infer.py` to `/report_detection`.
  * Acceptance: end-to-end demo works on PC.

* [ ] **10. Route planner (optional)**

  * File: `src/route_planner.py` using networkx/osmnx.
  * Acceptance: computes a route with mock congestion.

### Testing, docs & security

* [ ] **11. Test cases & evaluation**

  * Deliverable: sample videos/audios in `tests/` + metrics.
  * Acceptance: documented accuracy, mAP, latency.

* [ ] **12. Documentation & dev notes**

  * Files: `README.md`, `dev.md`, `steps.md`, and this `todo.md` review section.
  * Acceptance: clear runbook to reproduce demo locally.

* [ ] **13. Security & production checklist**

  * Add checklist in `dev.md`.
  * Ensure no secrets, proper validation, no debug endpoints in production.

### Cleanup & delivery

* [ ] **14. Packaging & demo assets**

  * Deliverable: sample video/audio + demo video + instructions.
  * Acceptance: 2–3 min demo video showing system.

---

## Principles

* Keep everything PC-only (no Raspberry Pi hardware needed).
* Minimal, simple, well-commented scripts.
* Security-first: no secrets, safe endpoints.
* Follow "simplicity-first" approach: build MVPs, avoid complexity.

---

## Files created / in progress

* ✅ `src/vision_train.py`
* ⏳ `src/vision_infer.py` (basic version with pretrained model tested; needs update for custom weights)
* ⏳ `datasets/vision/data.yaml`
* ❌ Pending: audio scripts, integration server, UI, docs

---

## steps.md (mini quickstart)

1. Create & activate virtualenv.
2. `pip install -r requirements.txt`.
3. Run `python src/integration_server.py`.
4. In separate terminals run `python src/vision_infer.py` and `python src/audio_infer.py`.
5. Open [http://localhost:5000](http://localhost:5000) → see traffic light simulation.

---

## Review section (progress log)

* ✅ Environment setup (venv, packages).
* ✅ Roboflow dataset downloaded & structured.
* ✅ `data.yaml` fixed with absolute paths.
* ✅ Pretrained YOLOv8 inference tested.
* ✅ Custom training started successfully (epoch 4/20 running now).  
* ⏳ Next: finish training → generate `best.pt` → run custom inference.

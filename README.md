# object_detection_v1

## 📌 Project Overview
This repository contains a simple object detection project built around YOLOv8 (Ultralytics) and a custom dataset. It includes:

- A YOLOv8 model checkpoint (`yolov8n.pt`)
- A labeled dataset in YOLO format (`object_detection_dataset/`)
- Notebook for experiments (`Object_detection_Project.ipynb`)
- A small Flask inference app (`app.py`, `templates/index.html`)
- Labeling tools (`labelImg/`)
- Reference images for visualization and debugging (`ref_images/`)

## 🗂️ Repository Structure
- `app.py` – Flask app for running inference and viewing detections.
- `Object_detection_Project.ipynb` – Notebook for training, evaluation, and experiments.
- `dataset.yaml` – YOLOv8 dataset config.
- `yolov8n.pt` – Pretrained YOLOv8 nano weights.
- `object_detection_dataset/` – Custom dataset in YOLO format:
  - `images/`
  - `labels/`
  - `train.txt`, `val.txt`, `test.txt`
  - `dataset.yaml`
- `ref_images/` – Reference images used for debugging, visualization, or demos.
- `runs/` – Output from training and detection runs (created by Ultralytics training/detect).
- `labelImg/` – LabelImg tool for creating YOLO-format annotations.

## ✅ What This Project Covers
This project is intended to teach and demonstrate:

- How to prepare a custom dataset for YOLOv8 (images + YOLO-format `.txt` labels)
- How to configure a dataset with `dataset.yaml`
- How to train and validate a YOLOv8 model using Ultralytics
- How to run inference on images and visualize detections
- How to build a simple Flask UI to serve inference results
- How to use `labelImg` for generating and editing annotations
- How to organize reference images (`ref_images/`) for testing and comparisons

## 🧰 Getting Started
1. Create a Python environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements-flask.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser to `http://localhost:5000` to see inference results.

## 📌 Using Reference Images (`ref_images/`)
The `ref_images/` folder is intended for:

- Storing sample images used in demos or documentation
- Comparing detection outputs across model versions
- Quickly validating that the pipeline works end-to-end

You can add images to `ref_images/` and run inference against them using the notebook or the Flask app.

## 📄 Notes
- If you retrain the model, your training outputs will appear under `runs/train/`.
- If you run detection, outputs appear under `runs/detect/`.

---

If you'd like the README to include step-by-step training commands (e.g., `yolo train ...`), just say so and I can add those details.

# YOLOv8 Flask App

Simple web app to run object detection with **yolov8n.pt**. Upload an image and see bounding boxes on the same page.

## Setup

```bash
pip install -r requirements-flask.txt
```

If `yolov8n.pt` is not in this folder, it will be downloaded automatically on first run.

## Run

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser. Choose an image and optional confidence threshold, then click **Detect**.

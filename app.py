"""
Simple Flask app for YOLOv8 object detection (yolov8n.pt).
Upload an image to get detections with bounding boxes.
"""

import io
import os
import numpy as np
import cv2
from flask import Flask, request, render_template, send_file
from ultralytics import YOLO

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload

# Load model once at startup (works when run as script or from notebook)
try:
    _base = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _base = os.getcwd()
MODEL_PATH = os.path.join(_base, "yolov8n.pt")
model = YOLO(MODEL_PATH)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return "No image uploaded", 400

    file = request.files["image"]
    if file.filename == "":
        return "No image selected", 400

    allowed = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed:
        return f"Invalid format. Use: {', '.join(allowed)}", 400

    image_bytes = file.read()
    # Decode to numpy array (YOLO does not accept raw bytes)
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is None:
        return "Could not decode image", 400

    results = model.predict(
        source=image,
        conf=float(request.form.get("conf", 0.25)),
        save=False,
        verbose=False,
    )

    annotated = results[0].plot()  # BGR numpy array
    _, buf = cv2.imencode(".jpg", annotated)
    return send_file(
        io.BytesIO(buf.tobytes()),
        mimetype="image/jpeg",
        as_attachment=False,
        download_name="detection.jpg",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

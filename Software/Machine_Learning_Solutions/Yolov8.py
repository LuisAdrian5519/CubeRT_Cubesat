# Importar librerías

from ultralytics import YOLO

# Build a new model from scratch

model = YOLO("yolov8n.yaml")

# train the model

model.train(data="config.yaml", epochs=15, batch=16)
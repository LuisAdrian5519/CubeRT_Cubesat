# Import libraries

from ultralytics import YOLO

# Select a model

model = YOLO("yolov11n.yaml")

# train the model

model.train(data="config.yaml", epochs=15, batch=16)
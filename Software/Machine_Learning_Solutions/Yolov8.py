# Import libraries

from ultralytics import YOLO

# Select a model

model = YOLO("yolov11n.yaml")

# train the model

# model.train(data="config.yaml", epochs=15, batch=16)

# model.train(data="config.yaml", epochs=10, batch=16, device=0, fraction = 0.30)


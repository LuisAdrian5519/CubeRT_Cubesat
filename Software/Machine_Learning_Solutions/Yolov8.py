# Import libraries

from ultralytics import YOLO

# Select a model

model = YOLO("yolov8n.yaml")

# train the model

# model.train(data="config.yaml", epochs=15, batch=16)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.1,
#             lrf=0.01)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.6,
#             weight_decay=0.0,)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.225,
#             translate=0.45,
#             scale=0.45,
#             flipud=0.5,
#             fliplr=0.5)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.45,
#             translate=0.9,
#             scale=0.9,
#             flipud=1.0,
#             fliplr=1.0)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0,
#             shear=0.0,
#             perspective=0.0,
#             mosaic=0.0,
#             mixup=0.0,)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0,
#             shear=5.0,
#             perspective=0.0005,
#             mosaic=0.5,
#             mixup=0.5)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0,
#             shear=10.0,
#             perspective=0.001,
#             mosaic=1.0,
#             mixup=1.0)

model.train(data="config.yaml", epochs=100, batch=32, device=0, workers=0, 
             lr0=0.01,
             lrf=0.001,
             momentum=0.98,
             weight_decay=0.001,
             warmup_epochs=3,
             warmup_momentum=0.98,
             degrees=0.0,
             translate=0.0,
             scale=0.0,
             flipud=0.0,
             fliplr=0.0,
             shear=0.0,
             perspective=0.0,
             mosaic=0.0,
             mixup=0.0,
             hsv_h=0.0,
             hsv_s=0.0,
             hsv_v=0.0,
             copy_paste=0.0)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0,
#             shear=0.0,
#             perspective=0.0,
#             mosaic=0.0,
#             mixup=0.0,
#             hsv_h=0.05,
#             hsv_s=0.45,
#             hsv_v=0.45,
#             copy_paste=0.5)

# model.train(data="config.yaml", epochs=15, batch=32, device=0, fraction = 0.20, workers=0, 
#             lr0=0.01,
#             lrf=0.001,
#             momentum=0.98,
#             weight_decay=0.001,
#             warmup_epochs=3,
#             warmup_momentum=0.98,
#             degrees=0.0,
#             translate=0.0,
#             scale=0.0,
#             flipud=0.0,
#             fliplr=0.0,
#             shear=0.0,
#             perspective=0.0,
#             mosaic=0.0,
#             mixup=0.0,
#             hsv_h=0.1,
#             hsv_s=0.9,
#             hsv_v=0.9,
#             copy_paste=1.0)



# Importar librerías

import cv2
import logging
from ultralytics import YOLO

# Cargar el modelo Entrenado

model = YOLO(r"C:/Users/usuario/Documents/Luis Adrian Cabrera/Proyectos/Representative_teams/Fox Robotics/Cubesat/CubeRT_Cubesat/Software/Machine_Learning_Solutions/runs/detect/train16/weights/best.pt")

logging.getLogger("ultralytics").setLevel(logging.CRITICAL)

# Iniciar Cámara

cap = cv2.VideoCapture(0)
frame_counter = 0

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    # Obtención de dimensiones de la imagen de entrada

    height, width, _ = frame.shape

    image_center_x = width // 2
    image_center_y = height // 2

    # Implementar modelo de Object Detection
    
    results = model(frame)
    
    detections = results[0].boxes
    
    for box in detections:
        
        # Obtención de centros del objeto y Error en X y Y

        x1, y1, x2, y2 = box.xyxy[0] 
        
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        distance_x = center_x - image_center_x
        distance_y = center_y - image_center_y
                
        # Dibujo de objetos detectados

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)  
        cv2.putText(frame, f'Center: ({center_x}, {center_y})', (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        # Impresión de variables

        print("-----------------------")
        print("Moon: x = {} | y = {}".format(center_x, center_y))
        print("Error: x = {} | y = {}".format(distance_x, distance_y))

    # Desplegar Imagen procesada

    cv2.imshow("YOLOv8 Real-Time Detection", frame)
    
    # Parámetro de salida del programa

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

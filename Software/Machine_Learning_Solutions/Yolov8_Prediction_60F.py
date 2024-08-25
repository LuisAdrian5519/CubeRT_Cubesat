# Importar librerías

import cv2
import logging
from ultralytics import YOLO
import machine
import time

# Configuración del pin del servo
servo_pin = machine.Pin(18)
servo = machine.PWM(servo_pin, freq=50)

# Función para mover el servo
def mover_servo(angulo):
    duty = int((angulo / 180) * 102) + 26
    servo.duty(duty)

# Cargar el modelo Entrenado

model = YOLO(r"C:/Users/usuario/Documents/Luis Adrian Cabrera/Proyectos/Fox Robotics/Cubesat/Software/runs/detect/train16/weights/last.pt")

logging.getLogger("ultralytics").setLevel(logging.CRITICAL)

# Iniciar Cámara

cap = cv2.VideoCapture(1)
frame_counter = 0


# Posición inicial del servo en el centro del frame
angulo_actual = -90
mover_servo(angulo_actual)

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1

    if frame_counter % 60 == 0:

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
        
            # Ajustar el ángulo del servo
            if distance_x > 0:
                angulo_actual += 1
            elif distance_x < 0:
                angulo_actual -= 1

            angulo_actual = max(0, min(180, angulo_actual))
            mover_servo(angulo_actual)

                        # Impresión de variables

            print("-----------------------")
            print("Moon: x = {} | y = {}".format(center_x, center_y))
            print("Error: x = {} | y = {}".format(distance_x, distance_y))
            print("-----------------------")



    # Desplegar Imagen procesada

    cv2.imshow("YOLOv8 Real-Time Detection", frame)
    
    # Parámetro de salida del programa

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

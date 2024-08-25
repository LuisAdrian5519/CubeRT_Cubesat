# Importar librerías

import cv2
import logging
from ultralytics import YOLO
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep

# Configuración del pin del servo con pigpio
factory = PiGPIOFactory()
servo = AngularServo(18, pin_factory=factory)

# Función para mover el servo
def mover_servo(angulo):
    servo.angle = angulo

# Cargar el modelo Entrenado

model = YOLO(r"/home/foxrobotics/Documents/train16/weights/best.pt")

logging.getLogger("ultralytics").setLevel(logging.CRITICAL)

# Iniciar Cámara

cap = cv2.VideoCapture(0)
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

        # Inicializar el ajuste del ángulo del servo
        angulo_ajustado = angulo_actual
    
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

            # Ajustar el ángulo del servo hasta que distance_x sea 0, con un límite de iteraciones
            max_iteraciones = 50
            iteracion_actual = 0

            # Ajustar el ángulo del servo hasta que distance_x sea 0
            while distance_x != 0 and iteracion_actual < max_iteraciones:
                if distance_x > 0:
                    angulo_ajustado += 5
                elif distance_x < 0:
                   angulo_ajustado -= 5

                # Limitar el ángulo del servo dentro del rango permitido
                angulo_ajustado = max(-90, min(90, angulo_ajustado))

                # Mover el servo al ángulo ajustado
                mover_servo(angulo_ajustado)

                # Recalcular distance_x después del movimiento del servo
                distance_x = center_x - image_center_x

                # Incrementar el contador de iteraciones
                iteracion_actual += 1

                # Opcional: Agregar un pequeño retardo para evitar movimientos demasiado rápidos
                sleep(0.01)

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
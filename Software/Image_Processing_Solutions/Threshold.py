# Importar librerías

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Acceder a la cámara y leer la Imagen de entrada

cap = cv2.VideoCapture(1)
frame_counter = 0

while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        frame_counter += 1 

        if frame_counter % 50 == 0: 

            # Convertir Imagen de entrada a Escala de grises y aplicar función Threshold

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            Th, gray_trsh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
            gray=gray_trsh

            rows = gray.shape[0]

            # Aplicar la transformada de Hough a la imagen de entrada y realizar búsqueda de círculos con la función Houghcircles.

            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                        param1=50, param2=20,
                                        minRadius=20, maxRadius=80)

            if circles is not None:

                circles = np.uint16(np.around(circles))

                # Dibujar circulos encontrados

                for i in circles[0, :]:
                    center = (i[0], i[1])
                    radius = i[2]

                    # Imagen gris

                    cv2.circle(gray, center, 1, (0, 100, 100), 3)
                    cv2.circle(gray, center, radius, (0, 255, 255), 3)

                    # Imagen original

                    cv2.circle(frame, center, 1, (0, 100, 100), 3)
                    cv2.circle(frame, center, radius, (0, 255, 255), 3)

                    # Imprimir posicion del circulo
                    print(f"Moon: {center}")

            # Desplegar imagen original e imagen procesada

            cv2.imshow("Circle Detection", gray)
            cv2.imshow("OG img",frame)

        # Parámetro de salida del programa

            if cv2.waitKey(1) == 27:
                break

cap.release()
cv2.destroyAllWindows()
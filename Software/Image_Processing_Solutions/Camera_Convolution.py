# Importar librerías

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Kernel-Sobel FIlter application for x & y axis Border Detection

def Convolution_filter(frame):

    # Kernel-Sobel Convolution Matrix for Vertical Borders Detection

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    # Kernel-Sobel Convolution Matrix for Horizontal Borders Detection

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    
    filtered_x = cv2.filter2D(frame, -1, sobel_x)
    filtered_y = cv2.filter2D(frame, -1, sobel_y)  
    filtered_frame = cv2.addWeighted(filtered_x, 0.5, filtered_y, 0.5, 0)

    return filtered_frame


# Camera Lecture
cap = cv2.VideoCapture(1)
frame_counter = 0

while True:
    ret, frame = cap.read()  

    if not ret:
        break

    frame_counter += 1

    if frame_counter % 50 == 0:
        filtered_frame = Convolution_filter(frame)


        # Circle Detection
        gray = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2GRAY)

        rows = gray.shape[0]
    
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=rows / 16,
                               param1=100, param2=30,
                               minRadius=5, maxRadius=30)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
    
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

                cv2.circle(filtered_frame, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(filtered_frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

                print(x,y)

        # Original Image & Filtered Image Comparison

        cv2.imshow('Original Image', frame)

        cv2.imshow('filtered Image', filtered_frame) 
    
    
        # Close Program Condition
    
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()
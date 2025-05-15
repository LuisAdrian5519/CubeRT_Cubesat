import os

label_dir = "C:/Users/josea/Documents/Luis Adrian/Moon_Dataset/Corrected_Augmented_Dataset/train/labels"

for label_file in os.listdir(label_dir):
    file_path = os.path.join(label_dir, label_file)
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    corrected_lines = []
    for line in lines:
        parts = line.strip().split()
        parts[0] = '0'  # Reemplaza la clase por 0
        corrected_lines.append(" ".join(parts) + "\n")
    
    with open(file_path, "w") as file:
        file.writelines(corrected_lines)

print("Todas las etiquetas han sido corregidas.")
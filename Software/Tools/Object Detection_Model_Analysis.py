
# Confusion Matrix Input Data

True_Positives = 152
True_Negatives = 0
False_Positives = 13
False_Negatives = 48

# Auxiliar

Total_Correct_Guesses = True_Positives + True_Negatives
Total_Incorrect_Guesses = False_Positives + False_Negatives

Total_Guesses = Total_Correct_Guesses + Total_Incorrect_Guesses

# Analysis

Sensitivity = True_Positives / (True_Positives + False_Negatives)

Accuracy = (Total_Correct_Guesses) / (Total_Guesses)

Precision = True_Positives / (True_Positives + False_Positives)

Recall = True_Positives / (True_Positives + False_Negatives)

F1 = (2 * Precision * Recall) / (Precision + Recall)



Specificity = True_Negatives / (True_Negatives + False_Positives)

True_Positive_Rate = Sensitivity

False_Positive_Rate = 1 - Specificity

print("")
print("Analysis:")
print("")
print(f"Sensitivity: {Sensitivity}")
print("")
print(f"Specificity: {Specificity}")
print("")
print(f"True_Positive_Rate: {True_Positive_Rate}")
print("")
print(f"False_Positive_Rate: {False_Positive_Rate}")
print("")
print(f"Accuracy: {Accuracy}")
print("")
print(f"Precision: {Precision}")
print("")
print(f"Recall: {Recall}")
print("")
print(f"F1: {F1}")
# Zadanie 14 -lekcja 5

models = [
    ('Logistic Regression', 0.78, 1.2),
    ('Random Forest', 0.92 , 45.6),
    ('SVM', 0.85, 12.3),
    ('XGBoost', 0.95, 67.8)
]

# Sortowanie modeli według dokładności (accuracy)
sorted_by_accuracy = sorted(models, key=lambda x: x[1], reverse=True)
print("Modele posortowane według dokładności:")
for models in sorted_by_accuracy:
    print(models)
# file_operations.py

def read_foods(filename, encoding='utf-8'):
    foods = {}
    with open(filename, 'r', encoding=encoding) as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 5:
                name = parts[0]
                try:
                    calories = float(parts[1])
                    protein = float(parts[2])
                    carbs = float(parts[3])
                    fat = float(parts[4])
                    foods[name] = {'calories': calories, 'protein': protein, 'carbs': carbs, 'fat': fat}
                except ValueError:
                    print(f"Erreur de conversion pour l'aliment: {name}")
    return foods


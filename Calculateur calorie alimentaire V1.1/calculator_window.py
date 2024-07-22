import tkinter as tk
from tkinter import ttk
import os
from file_operations import read_foods
from nutrition_calculator import calculate_nutrition
from file_processor import process_file
from autocomplete_combobox import AutocompleteEntry

def create_main_window(root):
    main_window = tk.Toplevel(root)
    main_window.title("Calculateur de calories")
    main_window.geometry("1030x800")

    # Lire les données des aliments à partir du fichier
    filename = os.path.join(os.path.dirname(__file__), 'foods.txt')
    foods = read_foods(filename)

    # Créer des LabelFrames pour chaque repas (4 repas au total)
    frames = [ttk.LabelFrame(main_window, text=f"Repas {i+1}", padding=(10, 10), relief="solid", borderwidth=2) for i in range(4)]
    for i, frame in enumerate(frames):
        frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

    # Initialiser les listes pour les variables des aliments et les entrées de poids
    food_vars = [[tk.StringVar() for _ in range(7)] for _ in range(4)]
    weight_entries = [[ttk.Entry(frames[meal_index]) for _ in range(7)] for meal_index in range(4)]

    # Créer les étiquettes, AutocompleteEntries et entrées pour chaque repas dans les frames respectives
    autocomplete_entries = []
    for meal_index, frame in enumerate(frames):
        for i in range(7):
            food_label = ttk.Label(frame, text=f"Aliment {i + 1}:", font=("Arial", 10, "normal"))
            food_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")
            
            food_entry = AutocompleteEntry(frame, textvariable=food_vars[meal_index][i], font=("Arial", 10))
            food_entry.set_completion_list(list(foods.keys()))
            food_entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="we")
            autocomplete_entries.append(food_entry)
            
            weight_label = ttk.Label(frame, text=f"Poids (g):", font=("Arial", 10, "normal"))
            weight_label.grid(row=i + 1, column=2, padx=10, pady=5, sticky="e")
            
            weight_entries[meal_index][i].grid(row=i + 1, column=3, padx=10, pady=5, sticky="we")

    # Étiquette et entrée pour les calories journalières désirées
    desired_calories_label = ttk.Label(main_window, text="Calorie journalière désirée:", font=("Arial", 12, "bold"))
    desired_calories_label.grid(row=11, column=0, padx=10, pady=5, sticky="e")

    desired_calories_entry = ttk.Entry(main_window, font=("Arial", 12))
    desired_calories_entry.grid(row=11, column=1, padx=10, pady=5, sticky="we")

    # Ajouter un espace vide pour les boutons sous les calories
    main_window.grid_rowconfigure(12, weight=1)

    # Fonction pour réinitialiser les champs et recharger les données
    def reset_fields():
        # Désactiver la mise à jour automatique
        for entry in autocomplete_entries:
            entry.auto_update = False
        
        # Recharger les données
        foods = read_foods(filename)
        
        # Mettre à jour chaque AutocompleteEntry avec les nouvelles données
        for entry in autocomplete_entries:
            entry.set_completion_list(list(foods.keys()))
        
        # Réinitialiser les champs
        for meal_index in range(4):
            for i in range(7):
                food_vars[meal_index][i].set("")
                weight_entries[meal_index][i].delete(0, tk.END)
        desired_calories_entry.delete(0, tk.END)
        
        # Réactiver la mise à jour automatique
        for entry in autocomplete_entries:
            entry.auto_update = True

    # Bouton pour calculer les valeurs nutritionnelles
    def calculate_nutrition_wrapper():
        calculate_nutrition(main_window, desired_calories_entry, food_vars, weight_entries)

    # Placer les boutons "Réinitialiser" et "Calculer Nutrition"
    calculate_button = ttk.Button(main_window, text="Calculer Nutrition", command=calculate_nutrition_wrapper)
    calculate_button.grid(row=12, column=1, padx=10, pady=5, sticky="e")

    reset_button = ttk.Button(main_window, text="Réinitialiser", command=reset_fields)
    reset_button.grid(row=12, column=1, padx=10, pady=5, sticky="w")

    # Ajouter le bouton "Ajouter Aliment" avec la fonction appropriée
    add_food_button = ttk.Button(main_window, text="Ajouter/supprimer Aliment", command=process_file)
    add_food_button.grid(row=12, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    # Fonction pour fermer la fenêtre principale
    def close_program():
        root.quit()

    main_window.protocol("WM_DELETE_WINDOW", close_program)

    # Lancer l'interface graphique
    main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre racine
    create_main_window(root)

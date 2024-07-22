#nutrition_calculator

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
from file_operations import read_foods

def calculate_nutrition(root, desired_calories_entry, food_vars, weight_entries):
    try:
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0

        meal_totals = []  # Liste pour stocker les totaux de chaque repas
        meal_details = []  # Liste pour stocker les détails de chaque repas

        # Lire les données des aliments à partir du fichier
        filename = os.path.join(os.path.dirname(__file__), 'foods.txt')
        foods = read_foods(filename, encoding='utf-8')

        # Itérer sur chaque repas (4 repas au total)
        for meal_index in range(4):
            meal_calories = 0
            meal_protein = 0
            meal_carbs = 0
            meal_fat = 0
            details = ""

            # Itérer sur chaque aliment dans le repas (jusqu'à 7 aliments)
            for i in range(7):
                selected_food = food_vars[meal_index][i].get()
                weight = weight_entries[meal_index][i].get()

                if selected_food and weight:
                    weight = float(weight)
                    if weight <= 0:
                        raise ValueError("Le poids doit être un nombre positif.")

                    nutrition = foods[selected_food]

                    # Calculer les valeurs nutritionnelles en fonction du poids
                    calories = (weight / 100) * nutrition['calories']
                    protein = (weight / 100) * nutrition['protein']
                    carbs = (weight / 100) * nutrition['carbs']
                    fat = (weight / 100) * nutrition['fat']

                    meal_calories += calories
                    meal_protein += protein
                    meal_carbs += carbs
                    meal_fat += fat

                    # Formater et ajouter les informations de l'aliment aux détails
                    details += f"{selected_food} ({weight}g):\n"
                    details += f"  - Calories: {calories:.2f}\n"
                    details += f"  - Protéines: {protein:.2f}g\n"
                    details += f"  - Glucides: {carbs:.2f}g\n"
                    details += f"  - Lipides: {fat:.2f}g\n\n"

            # Ajouter les totaux du repas aux totaux généraux
            total_calories += meal_calories
            total_protein += meal_protein
            total_carbs += meal_carbs
            total_fat += meal_fat

            meal_totals.append((meal_calories, meal_protein, meal_carbs, meal_fat))
            meal_details.append(details)

        # Générer le texte des totaux journaliers
        total_text = f"  - Total Calories: {total_calories:.2f}\n"
        total_text += f"  - Total Protéines: {total_protein:.2f}g\n"
        total_text += f"  - Total Glucides: {total_carbs:.2f}g\n"
        total_text += f"  - Total Lipides: {total_fat:.2f}g\n"

        # Calculer et afficher la différence par rapport aux calories désirées si saisies
        desired_calories = desired_calories_entry.get()
        if desired_calories:
            desired_calories = float(desired_calories)
            calories_difference = desired_calories - total_calories
            total_text += f"\nDifférence avec les calories désirées ({desired_calories} calories): {calories_difference:.2f} calories"

        # Masquer la fenêtre principale
        root.withdraw()

        # Créer une nouvelle fenêtre pour afficher les résultats nutritionnels
        result_window = tk.Toplevel(root)
        result_window.title("Résultats Nutritionnels")
        result_window.geometry("800x600")  # Définir la taille initiale
        result_window.minsize(800, 600)  # Définir la taille minimale
        result_window.resizable(width=False, height=True)  # Empêcher le redimensionnement horizontal

        # Cadre principal pour organiser les sections
        main_frame = ttk.Frame(result_window)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Configurer la grille principale
        main_frame.grid_rowconfigure(0, weight=1)  # Totaux journaliers
        main_frame.grid_rowconfigure(1, weight=1)  # Totaux des repas
        main_frame.grid_rowconfigure(2, weight=3)  # Détails des repas
        main_frame.grid_rowconfigure(3, weight=0)  # Espace pour les boutons
        main_frame.grid_rowconfigure(4, weight=0)  # Espace pour le bouton "Enregistrer"
        main_frame.grid_columnconfigure(0, weight=1)

        # Cadre pour les totaux journaliers
        daily_totals_frame = ttk.LabelFrame(main_frame, text="Totaux Journaliers", padding=(10, 10))
        daily_totals_frame.grid(row=0, column=0, sticky="nsew")

        total_font = ('Helvetica', 12, 'bold')  # Police en gras avec une taille de 12
        result_label_total = tk.Label(daily_totals_frame, text=total_text, justify="center", anchor="center", padx=10, pady=10, font=total_font)
        result_label_total.pack(fill=tk.BOTH, expand=True)

        # Cadre pour les totaux des repas
        meal_totals_frame = ttk.LabelFrame(main_frame, text="Totaux pour chaque repas", padding=(10, 10))
        meal_totals_frame.grid(row=1, column=0, sticky="nsew")

        for col in range(4):
            meal_totals_frame.columnconfigure(col, weight=1, uniform="totals")

        for idx, (calories, protein, carbs, fat) in enumerate(meal_totals):
            result_text_totals = f"Totaux pour le repas {idx + 1}:\n\n"
            result_text_totals += f"  - Total Calories: {calories:.2f}\n"
            result_text_totals += f"  - Total Protéines: {protein:.2f}g\n"
            result_text_totals += f"  - Total Glucides: {carbs:.2f}g\n"
            result_text_totals += f"  - Total Lipides: {fat:.2f}g\n"

            result_label_totals = tk.Label(meal_totals_frame, text=result_text_totals, justify="left", anchor="w", padx=10, pady=10, borderwidth=2, relief="groove")
            result_label_totals.grid(row=0, column=idx, padx=(0, 10), sticky="nsew")

        # Cadre pour les détails des repas avec une barre de défilement
        details_frame = ttk.Frame(main_frame)
        details_frame.grid(row=2, column=0, sticky="nsew")

        canvas = tk.Canvas(details_frame)
        scrollbar = ttk.Scrollbar(details_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Configurer les colonnes pour le cadre des détails des repas
        meal_details_lf = ttk.LabelFrame(scrollable_frame, text="Détails de chaque repas", padding=(10, 10))
        meal_details_lf.pack(fill="both", expand=True)

        for col in range(4):
            meal_details_lf.columnconfigure(col, weight=1, uniform="totals")

        for idx, details in enumerate(meal_details):
            if not details.strip():
                details = "Aucun aliment sélectionné\n"
            result_label_details = tk.Label(meal_details_lf, text=details, justify="left", anchor="w", padx=10, pady=10, borderwidth=2, relief="groove")
            result_label_details.grid(row=0, column=idx, padx=(0, 10), sticky="nsew")

        # Cadre pour les boutons
        button_frame = ttk.Frame(main_frame, padding=(10, 10))
        button_frame.grid(row=3, column=0, columnspan=4, sticky="ew")

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # Boutons "Précédent" et "Enregistrer" alignés sur la même ligne
        back_button = ttk.Button(button_frame, text="Précédent", command=lambda: go_to_main_window(root, result_window))
        back_button.grid(row=0, column=0, padx=(0, 5), pady=10, sticky="e")

        save_button = ttk.Button(button_frame, text="Enregistrer", command=lambda: save_results(result_window, total_text, meal_totals, meal_details))
        save_button.grid(row=0, column=1, padx=(5, 0), pady=10, sticky="w")

        # Lier l'événement de fermeture de la fenêtre des résultats pour quitter le programme
        result_window.protocol("WM_DELETE_WINDOW", lambda: close_program(root))

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def go_to_main_window(root, result_window):
    result_window.destroy()
    root.deiconify()

def save_results(result_window, total_text, meal_totals, meal_details):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Totaux Journaliers:\n")
            file.write(total_text + "\n")
            file.write("Totaux des repas:\n")
            for idx, (calories, protein, carbs, fat) in enumerate(meal_totals):
                file.write(f"Repas {idx + 1}:\n")
                file.write(f"  - Total Calories: {calories:.2f}\n")
                file.write(f"  - Total Protéines: {protein:.2f}g\n")
                file.write(f"  - Total Glucides: {carbs:.2f}g\n")
                file.write(f"  - Total Lipides: {fat:.2f}g\n")
            file.write("\nDétails des repas:\n")
            for idx, details in enumerate(meal_details):
                file.write(f"Repas {idx + 1}:\n")
                file.write(details + "\n")
        messagebox.showinfo("Enregistrement", "Les résultats ont été enregistrés avec succès.")
        result_window.destroy()

def close_program(root):
    root.quit()

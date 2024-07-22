import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_food_data(food_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food_name}&search_simple=1&action=process&json=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['count'] > 0:
            # Rechercher le produit qui correspond le mieux au terme de recherche
            for product in data['products']:
                if food_name.lower() in product.get('product_name', '').lower():
                    return {
                        'product_name': product.get('product_name', 'N/A'),
                        'nutriments': product.get('nutriments', {})
                    }
            # Si aucun produit ne correspond exactement, retourner le premier résultat
            product = data['products'][0]
            return {
                'product_name': product.get('product_name', 'N/A'),
                'nutriments': product.get('nutriments', {})
            }
        else:
            messagebox.showerror("Erreur", f"Produit {food_name} non trouvé.")
    else:
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des données pour {food_name}: {response.status_code}")
    return None

def search_food():
    food_name = food_entry.get().strip()
    if food_name:
        food_data = get_food_data(food_name)
        if food_data:
            nutriments = food_data['nutriments']
            calories = nutriments.get('energy-kcal_100g', 'N/A')
            proteins = nutriments.get('proteins_100g', 'N/A')
            carbs = nutriments.get('carbohydrates_100g', 'N/A')
            fats = nutriments.get('fat_100g', 'N/A')

            result_label.config(text=f"Produit: {food_data['product_name']}\nCalories: {calories} kcal\nProtéines: {proteins} g\nGlucides: {carbs} g\nLipides: {fats} g")
        else:
            result_label.config(text="Aliment non trouvé.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom d'aliment.")

def reset_fields():
    food_entry.delete(0, tk.END)
    result_label.config(text="")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Calculateur de Calories Alimentaires")

# Configuration de la grille
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Ajouter des widgets
tk.Label(root, text="Nom de l'aliment:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
food_entry = ttk.Entry(root)
food_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

search_button = ttk.Button(root, text="Rechercher", command=search_food)
search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="", anchor=tk.W, justify=tk.LEFT)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

reset_button = ttk.Button(root, text="Réinitialiser", command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Démarrer l'application Tkinter
root.mainloop()

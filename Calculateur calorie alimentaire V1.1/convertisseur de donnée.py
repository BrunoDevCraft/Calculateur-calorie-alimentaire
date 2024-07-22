import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from file_operations import read_foods  # Assurez-vous que la fonction read_foods est importée

# Définir le chemin du fichier spécifique
SPECIFIC_FILE_PATH = os.path.join(os.path.dirname(__file__), 'listing aliment.txt')
MODIFIED_FILE_PATH = os.path.join(os.path.dirname(__file__), 'foods.txt')

def process_file():
    if os.path.isfile(SPECIFIC_FILE_PATH):
        try:
            # Lancer le Bloc-notes avec le fichier spécifique
            subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', SPECIFIC_FILE_PATH], shell=True)

            # Attendre que l'utilisateur ait fini d'éditer et d'enregistrer le fichier
            messagebox.showinfo("Information", "Modifiez le fichier dans Notepad, puis cliquez sur OK une fois terminé.")
            
            # Lire le contenu du fichier modifié
            with open(SPECIFIC_FILE_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Modifier le contenu
            new_lines = []

            # Supprimer la première ligne
            if len(lines) > 0:
                lines.pop(0)
            
            # Traiter les lignes restantes
            for index, line in enumerate(lines):
                line = line.rstrip()  # Supprimer les espaces de fin

                if line:  # Ignorer les lignes vides
                    # Remplacer "|" par ":"
                    line = line.replace('|', ':')

                    # Supprimer les espaces de fin de chaque partie avant ":"
                    parts = line.split(':')
                    parts[0] = parts[0].rstrip()  # Supprimer les espaces après le nom de l'aliment

                    if index == 0:  # Ligne 1 (après suppression de la première ligne)
                        # Remplacer les "-" par une chaîne vide (ou autre traitement spécifique)
                        parts = [part.replace('-', '') for part in parts]
                    else:
                        # Remplacer "-" par "0.0" et supprimer les espaces dans les valeurs
                        parts = [part if i == 0 else part.replace('-', '0.0').replace(' ', '') for i, part in enumerate(parts)]

                    new_line = ':'.join(parts)
                    new_lines.append(new_line + '\n')  # Ajouter '\n' pour maintenir les sauts de ligne

            # Écrire le contenu modifié dans un nouveau fichier
            with open(MODIFIED_FILE_PATH, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)

            # Vérifier le contenu du fichier modifié
            foods = read_foods(MODIFIED_FILE_PATH)
            print("Données lues du fichier modifié :")
            for name, nutrition in foods.items():
                print(f"{name}: {nutrition}")

            messagebox.showinfo("Succès", f"Le fichier modifié a été enregistré sous le nom '{MODIFIED_FILE_PATH}'.")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", f"Le fichier {SPECIFIC_FILE_PATH} n'a pas été trouvé.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestion des fichiers")

# Créer et placer le bouton dans la fenêtre
btn_process = tk.Button(root, text="Ajouter/Supprimer", command=process_file)
btn_process.pack(pady=20)

# Lancer l'interface graphique
root.mainloop()

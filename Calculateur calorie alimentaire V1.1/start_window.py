#start_window

import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
from calculator_window import create_main_window  # Importer la fonction depuis le fichier du calculateur

SPECIFIC_FILE_PATH = os.path.join(os.path.dirname(__file__), 'listing aliment.txt')

def show_start_window(root):
    start_window = tk.Toplevel(root)
    start_window.title("Bienvenue")
    start_window.geometry("800x600")
    
    # Frame pour le titre
    title_frame = tk.Frame(start_window)
    title_frame.place(relx=0.5, rely=0.4, anchor="center")  # Centrer horizontalement et verticalement

    # Titre centré sur deux lignes
    title_label = tk.Label(title_frame, text="Calculateur \nCalorie Alimentaire V1.1", font=("Arial", 24, "bold"), anchor="center")
    title_label.pack(pady=20)
    
    # Fonction pour démarrer la fenêtre principale
    def start_main_window():
        start_window.withdraw()  # Masquer la fenêtre de présentation
        create_main_window(root)  # Afficher la fenêtre principale

    # Fonction pour ouvrir la fenêtre d'informations
    def open_info_window():
        info_window = tk.Toplevel(start_window)
        info_window.title("Informations sur le programme")
        info_window.geometry("395x500")

        # Créer un widget Text pour le texte multi-lignes
        info_text = tk.Text(info_window, wrap="word", padx=10, pady=10)
        info_text.pack(expand=True, fill="both")

        # Ajouter les informations à afficher
        info_message = (
            "Bienvenue dans le Calculateur de Calories Alimentaire V1.1\n\n"
            "Ce programme vous permet de calculer les besoins nutritionnels\n"
            "basés sur les aliments que vous consommez au cours de la journée.\n\n"
            "Fonctionnalités :\n"
            "- Entrez les aliments consommés pour chaque repas.\n"
            "- Indiquez le poids de chaque aliment en gramme.\n"
            "- Obtenez un calcul des calories et autres informations nutritionnelles.\n\n"
            "-> Source:\n" 
            "  alimentaire :\n"      
            "  https://www.benchpresschampion.com/dietetique/Calories.pdf modifié avec chatgpt 3.5\n\n"
            "-> Pour ouvrir le fichier liste aliment, assurez-vous d'avoir le chemin suivant existant:\n"
            "  C:\\Windows\\System32\\notepad.exe \n"
            "----------------------------------------------\n"
            "----------------------------------------------\n"
            "Dernier ajout: \n\n"
            "Page de présentation;\n"
            "fichier information;\n"
            "liste aliment;\n"
            "Boutons à action logique:\n"
            "démarrer, info, fermer, réinitialise, précédent, enregistrer\n"
        )
        info_text.insert(tk.END, info_message)
        info_text.config(state=tk.DISABLED)  # Désactiver la modification du texte
        
        # Ajouter un bouton pour ouvrir le fichier texte spécifique
        open_file_button = ttk.Button(info_window, text="Ouvrir liste aliment", command=open_specific_file)
        open_file_button.pack(pady=10)

    # Fonction pour ouvrir le fichier texte spécifique avec Bloc-notes
    def open_specific_file():
        #os.chmod(SPECIFIC_FILE_PATH, 666)  # 0o444 est le mode lecture seule pour tous les utilisateurs
    
        if os.path.isfile(SPECIFIC_FILE_PATH):
            try:
                # Lancer le Bloc-notes avec le fichier spécifique
                subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', SPECIFIC_FILE_PATH], shell=True)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier avec Bloc-notes. Erreur : {e}")
        else:
            messagebox.showerror("Erreur", f"Le fichier {SPECIFIC_FILE_PATH} n'a pas été trouvé.")

    # Fonction pour quitter le programme
    def quit_program():
        start_window.destroy()  # Ferme la fenêtre de présentation
        root.quit()             # Termine l'application principale
    
    # Frame pour les boutons en bas
    button_frame = tk.Frame(start_window)
    button_frame.pack(side="bottom", pady=150)  # Ajuster le padding pour plus d'espace en bas
    
    # Style pour les boutons avec dimensions spécifiques
    style = ttk.Style()
    style.configure("TButton",
                font=('Arial', 18, 'bold'),  # Taille de la police initiale
                padding=(20, 10))            # Padding (horizontal, vertical)

    # Boutons de la fenêtre de présentation
    start_button = ttk.Button(button_frame, text="Démarrer", command=start_main_window, style="TButton")
    start_button.pack(side="left", padx=20)

    info_button = ttk.Button(button_frame, text="Info", command=open_info_window, style="TButton")
    info_button.pack(side="left", padx=20)

    quit_button = ttk.Button(button_frame, text="Fermer", command=quit_program, style="TButton")
    quit_button.pack(side="left", padx=20)

    # Démarrer la fenêtre de présentation
    start_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre racine
    show_start_window(root)

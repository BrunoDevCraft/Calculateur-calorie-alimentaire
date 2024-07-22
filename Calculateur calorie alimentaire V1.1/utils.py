#utils
import tkinter as tk

def display_nutrition_results(results, main_window, root):
    result_window = tk.Toplevel(main_window)
    result_window.title("Résultats Nutritionnels")

    # Afficher les résultats dans un widget Text
    result_text = tk.Text(result_window, wrap="word", padx=10, pady=10)
    result_text.pack(expand=True, fill="both")

    # Insérer les résultats dans le widget Text
    for key, value in results.items():
        result_text.insert(tk.END, f"{key}: {value}\n")

    result_text.config(state=tk.DISABLED)  # Désactiver la modification du texte

    # Fonction pour fermer la fenêtre de résultats
    def close_result_window():
        result_window.deiconify()
        #result_window.destroy()
        if not tk.Toplevel(root).winfo_exists():  # Check if all windows are closed
            root.quit()  # Terminer l'application principale
        
    result_window.protocol("WM_DELETE_WINDOW", close_result_window)

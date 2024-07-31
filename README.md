# Calculateur de Calories Alimentaires V1.1

## Description

Ce programme est un calculateur de calories alimentaires qui permet aux utilisateurs de suivre leurs apports nutritionnels quotidiens en entrant les aliments consommés et leurs poids. 
Il fournit une analyse détaillée des calories, protéines, glucides et lipides consommés.

## Principe de Fonctionnement

1. **Fenêtre de Démarrage** : À l'exécution du programme, une fenêtre de démarrage apparaît, offrant les options suivantes :
   - **Démarrer** : Lance la fenêtre principale du calculateur de calories.
   - **Info** : Affiche des informations sur le programme et des instructions supplémentaires.
   - **Fermer** : Quitte l'application.

2. **Fenêtre Principale** : Dans cette fenêtre, vous pouvez :
   - **Saisir les aliments** : Pour chaque repas (4 repas au total), sélectionnez les aliments à partir d'une liste déroulante avec autocomplétion et entrez leur poids en grammes.
   - **Calculer la Nutrition** : Cliquez sur le bouton "Calculer Nutrition" pour obtenir les valeurs nutritionnelles totales pour chaque repas et pour la journée entière.
   - **Réinitialiser les Champs** : Utilisez le bouton "Réinitialiser" pour effacer toutes les saisies et recommencer. Cela permet également de mettre directement à jour la liste des aliments.
   - **Ajouter/Supprimer des Aliments** : Cliquez sur "Ajouter/supprimer Aliment" pour mettre à jour la liste des aliments disponibles.

3. **Affichage des Résultats** :
   - Les résultats nutritionnels sont affichés dans une nouvelle fenêtre, montrant les totaux journaliers et les détails de chaque repas.
   - Vous pouvez enregistrer les résultats en tant que fichier texte en cliquant sur "Enregistrer".

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger Python à partir de [python.org](https://www.python.org/).
2. Installez les modules nécessaires en exécutant la commande suivante dans votre terminal : pip install tkinter
3. Placez les fichiers suivants dans le même répertoire :
- `main - calculateur calorie alimentaire.py`
- `start_window.py`
- `calculator_calorie.py`
- `nutrition_calculator.py`
- `convertisseur de donnée.py`
- `file_operations.py`
- `file_processor.py`
- `utils.py`
- `autocomplete_combobox.py`
- `foods.txt`
- `listing aliment.txt`

## Utilisation

1. Exécutez le fichier `main - calculateur calorie alimentaire.py` : python 'main - calculateur calorie alimentaire.py'

2. Une fenêtre de démarrage s'affiche avec les options "Démarrer", "Info" et "Fermer".
- **Démarrer** : Lance la fenêtre principale du calculateur de calories.
- **Info** : Affiche des informations sur le programme.
- **Fermer** : Quitte l'application.

3. Dans la fenêtre principale, entrez les aliments consommés pour chaque repas et leurs poids en grammes.
4. Cliquez sur "Calculer Nutrition" pour obtenir les valeurs nutritionnelles totales.
5. Utilisez le bouton "Réinitialiser" pour effacer tous les champs et recommencer.
6. Cliquez sur "Ajouter/Supprimer Aliment" pour gérer les aliments disponibles.

## Fichiers de Données

- **listing aliment.txt** : Contient une liste des aliments pour l'autocomplétion.
- **foods.txt** : Contient les informations nutritionnelles des aliments.
                  ATTENTION: En cours de conception, plusieurs sources différentes peuvent faire varier les résultats.

                  Lorsque les valeurs sont 0.5 ou 0.85, référez-vous au 'listing aliment.txt' pour savoir si elles sont 
                  précise ou peuvent être inférieur, voir supérieur (Le programme actuel, ne fait pas le dinstingo). De plus 
                  si dans calorie, il y a marqué '0' c'est que dans la table Ciqal de 2020 que j'ai utilisé cette valeur 
                  n'était pas indiquée.

## Informations Supplémentaires

Pour plus d'informations sur le programme, cliquez sur le bouton "Info" dans la fenêtre de démarrage. 

**Source des données alimentaires** : 
      "https://www.data.gouv.fr/fr/datasets/table-de-composition-nutritionnelle-des-aliments-ciqual/"

## Contact

Pour toute question ou suggestion, veuillez contacter `complexboy@outlook.fr`.

En date du 31 Juillet 2024



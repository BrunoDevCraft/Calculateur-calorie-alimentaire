# 🥗 NutriCalc v3

> Calculateur nutritionnel journalier — application web mono-fichier, 100 % client-side.

---

## 🤖 À propos du projet

**NutriCalc** est issu d'un programme de base qui a été progressivement enrichi et amélioré grâce à la collaboration de **plusieurs intelligences artificielles** (Claude, ChatGPT, etc.). Chaque itération a permis d'ajouter de nouvelles fonctionnalités, d'affiner l'interface, d'optimiser le code et d'enrichir la base de données alimentaire.

La version actuelle — **v3** — constitue une refonte complète intégrant : un système de plans de repas sauvegardables, un calendrier nutritionnel mensuel, des graphiques d'évolution et un gestionnaire de base de données alimentaire.

> Le fichier `NutriCalc_v3.html` est **autonome** : aucune installation, aucun serveur, aucune dépendance externe à télécharger. Il suffit de l'ouvrir dans un navigateur.

---

## 📁 Structure du dossier

```
/
├── NutriCalc_v3.html       ← Application principale (fichier unique)
├── README.md               ← Ce fichier
└── source/
    └── foods.txt           ← Listing complet des aliments (base de données exportable)
```

> ⚠️ **Le fichier `source/foods.txt`** contient le listing exhaustif des aliments intégrés à l'application. Il peut être modifié manuellement, puis réimporté directement dans NutriCalc via le gestionnaire de base de données.

---

## ✨ Fonctionnalités

### 🧮 Calculateur (onglet principal)
- **4 repas** paramétrables : Petit-déjeuner, Déjeuner, Dîner, Collation
- **7 lignes par repas** avec autocomplétion intelligente sur la base alimentaire
- Navigation clavier dans les suggestions (↑ ↓ Entrée Échap)
- **Objectif calorique journalier** avec barres de progression en temps réel (calories, protéines, glucides, lipides)
- Calcul instantané des macronutriments par repas et au total
- Affichage de l'écart par rapport à l'objectif (au-dessus / en dessous / atteint)
- Détail aliment par aliment dépliable
- **Export des résultats** en fichier texte
- **Sauvegarde du plan** courant avec nom personnalisé

### 📋 Plans de repas (onglet Mes Plans)
- Sauvegarde illimitée de plans nommés avec date et couleur de label
- Rechargement d'un plan dans le calculateur en un clic
- Suppression individuelle
- Persistance via `localStorage` (données conservées entre sessions)

### 📅 Calendrier nutritionnel (onglet Calendrier)
- Vue mensuelle navigable (mois précédent / suivant)
- Assignation d'un plan sauvegardé à n'importe quel jour
- Code couleur des jours selon le plan assigné
- **Statistiques rapides** : moyenne calorique, meilleur/pire jour du mois
- **Rapport imprimable** avec sélection de période (7 jours, mois en cours, 30 jours, 3 mois)
  - Graphique d'évolution des calories (Canvas)
  - Graphique des macronutriments (Canvas)
  - Tableau récapitulatif jour par jour
  - Bouton d'impression natif

### 🗄️ Base de données alimentaire (onglet Base de données)
- **~150+ aliments intégrés** couvrant : viandes, poissons, produits laitiers, féculents, légumes, fruits, matières grasses, légumineuses, etc.
- Valeurs pour 100 g : calories (kcal), protéines (g), glucides (g), lipides (g)
- Ajout manuel d'un nouvel aliment via formulaire
- Suppression d'un aliment
- Recherche/filtre en temps réel dans le tableau
- **Import** depuis un fichier `.txt` externe (format `foods.txt`)
- **Export** de toute la base en fichier `.txt`
- Les aliments ajoutés manuellement sont persistés en `localStorage`

---

## 📄 Format du fichier `foods.txt`

Chaque ligne correspond à un aliment, selon le format suivant :

```
Nom de l'aliment:calories:protéines:glucides:lipides
```

**Exemple :**
```
Poulet, blanc, cuit:165:31:0:3.57
Riz blanc, cuit:130:2.69:28.17:0.28
Oeuf entier, cuit:155:12.58:1.12:10.61
```

**Règles :**
- Encodage : **UTF-8**
- Séparateur : **deux-points** `:`
- Les lignes commençant par `#` sont ignorées (commentaires)
- Les lignes vides sont ignorées
- Les valeurs numériques utilisent le point `.` comme séparateur décimal

---

## 🚀 Utilisation

1. Ouvrir `NutriCalc_v3.html` dans un navigateur moderne (Chrome, Firefox, Edge, Safari)
2. *(Optionnel)* Importer `source/foods.txt` via l'onglet **Base de données → Importer .txt** pour enrichir ou remplacer la base intégrée
3. Saisir un objectif calorique journalier
4. Remplir les repas avec les aliments et leur poids en grammes
5. Cliquer sur **Calculer** pour obtenir le bilan nutritionnel
6. Sauvegarder le plan et l'assigner dans le calendrier

---

## 🛠️ Technique

| Élément | Détail |
|---|---|
| Type | Application HTML mono-fichier |
| Dépendances runtime | Google Fonts (DM Serif Display, DM Mono, Instrument Sans) |
| Stockage | `localStorage` (plans, aliments personnalisés, calendrier) |
| Graphiques | Canvas API natif |
| Compatibilité | Tout navigateur moderne (ES2020+) |
| Framework | Aucun — HTML / CSS / JS vanilla |

---

## 📝 Historique des versions

| Version | Évolutions principales |
|---|---|
| v1 | Programme de base : calculateur 4 repas, base alimentaire simple |
| v2 | Amélioration UI, autocomplétion, export résultats |
| v3 | Plans sauvegardables, calendrier mensuel, rapports graphiques, gestionnaire BDD complet |

---

*Projet développé et amélioré de façon itérative avec l'assistance de plusieurs outils d'IA générative.*

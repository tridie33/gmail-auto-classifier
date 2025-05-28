# Gmail Auto Classifier

Ce projet Python permet de **classer automatiquement les emails Gmail** dans différents labels personnalisés, comme :

- `Confirmation Candidatures`
- `Refus Candidatures`
- `Réponses Positives`
- `Newsletters`

##  Fonctionnalités

- Connexion à Gmail via OAuth2
- Lecture des mails récents
- Classification automatique des mails selon leur contenu
- Application des bons labels
- Exécution automatisée avec `cron` (Linux/macOS) ou le Planificateur de tâches Windows



## Structure du projet

```bash
gmail-auto-classifier/
│
├── gmail.py               # Fonctions utilitaires pour Gmail
├── classify_old.py        # Classe les anciens mails existants
├── classify_new.py        # Classe automatiquement les nouveaux mails 
├── authorize.py           # Script pour générer le token d'accès
├── README.md              # Fichier d'explication du projet
├── requirements.txt       # Dépendances Python
├── credentials.json       # Clé OAuth2 téléchargée depuis Google Cloud Console (non incluse ici)
├── token.json             # Jeton d’accès utilisateur (généré automatiquement)
```

## Génération des fichiers credentials.json et token.json
#### Étape 1 — Créer un projet Google Cloud
Va sur : https://console.cloud.google.com

Crée un nouveau projet (par exemple : Gmail Classifier)

Active l’API Gmail :

"API & Services" → "Library" → "Gmail API" → Enable

#### Étape 2 — Créer les identifiants OAuth2
Dans "API & Services" > "Identifiants"

Clique sur "Créer des identifiants" > "ID client OAuth"

Type d’application : Application de bureau

Télécharge le fichier credentials.json

Place ce fichier à la racine de ton projet

#### Étape 3 — Générer token.json
Lance une seule fois le script suivant :

```bash
python authorize.py
```
Cela ouvrira une fenêtre de navigateur pour t’authentifier avec ton compte Gmail. Une fois validée, un fichier **token.json** sera généré automatiquement.
Ce fichier contient ton jeton d'accès personnel. Il est requis pour que le script puisse accéder à ta boîte Gmail.

## Exécution des scripts
Pour classer les anciens mails existants :
```bash
python classify_old.py
```
Pour classer automatiquement les nouveaux mails (à relancer toutes les minutes) :
```bash
python classify_new.py
```

## Automatisable via :
-cron (Linux/macOS)
-Planificateur de tâches Windows

## Prérequis
Python 3.10+
Compte Gmail
Accès à Google Cloud Console

##Installe les dépendances :
```bash
pip install -r requirements.txt
```
## Remarques
Ne partage jamais tes fichiers credentials.json et token.json publiquement.
L'authentification OAuth fonctionne uniquement pour les comptes ajoutés dans les utilisateurs testeurs tant que l'application n’est pas validée publiquement.
Les mails sont classés en fonction de règles simples définies dans classify_old.py et classify_new.py.

## Sécurité
Les fichiers sensibles sont ignorés dans .gitignore par défaut pour éviter leur publication.

## Contribution
Améliorations bienvenues ! Tu peux cloner ce dépôt, tester et proposer des suggestions.

## Licence
Ce projet est open-source. Libre à toi de le modifier ou de t’en inspirer pour usage personnel ou professionnel.

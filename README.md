# ProjetInfo2A Velib'Hunter

**Projet informatique 2A – ENSAI 2023-2024 (Sujet 8 : les vélibs)**  
Application Python pour améliorer l'accès aux stations Vélib’ à Paris, en exploitant les données publiques d'OpenData Paris.

## Objectif du projet

Velib'Hunter est une application conçue pour :

- localiser la station la plus proche avec au moins un vélo disponible ;
- identifier la station la moins fréquentée sur une période donnée ;
- déterminer l’arrondissement le plus fréquenté.

Le tout repose sur une architecture modulaire, un backend en Python et une base de données SQLite.

## Arborescence du projet

```
ProjetInfo2A/
├── api/                 # Contrôleurs et gestion des requêtes utilisateur
├── database/            # DAO et initialisation de la base SQLite
├── schema/              # Business Objects : Station, Date, Record, etc.
├── service/             # Logique métier
├── websocket/           # Serveur WebSocket pour mises à jour en temps réel
├── tests/               # Tests unitaires
├── deployment/          # Docker et Docker Compose
├── main.py              # Point d'entrée principal
└── README.md            # Ce fichier
```

## Prérequis

- Python version 3.9 ou supérieure
- pip (gestionnaire de paquets Python)
- Docker et Docker Compose (optionnel)
- Un outil de test d’API comme Insomnia ou Postman

## Installation et exécution

### 1. Cloner le dépôt

```
git clone https://github.com/anasselbasra/ProjetInfo2A.git
cd ProjetInfo2A
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```
python -m venv env
source env/bin/activate    # Pour Linux/macOS
env\Scripts\activate       # Pour Windows
```

### 3. Installer les dépendances

```
pip install -r requirements.txt
```

### 4. Initialiser la base de données

```
python database/init_db.py
```

### 5. Lancer l’application

```
python main.py
```

## Tests

Pour exécuter les tests unitaires :

```
pytest tests/
```

## Déploiement avec Docker

Si vous souhaitez déployer l’application via Docker :

```
docker-compose up --build
```

L’API sera accessible sur le port 8000 (sauf si modifié dans `docker-compose.yml`).

## Principaux endpoints API

- `GET /nearest_station?lat=...&lon=...`  
  Renvoie la station la plus proche avec un vélo disponible.

- `GET /least_busy_station?start_date=...&end_date=...`  
  Renvoie la station la moins fréquentée dans l’intervalle spécifié.

- `GET /most_busy_arrondissement?start_date=...&end_date=...`  
  Renvoie l’arrondissement parisien le plus fréquenté sur la période donnée.

## Fonctionnalités avancées

- Serveur WebSocket pour mises à jour en temps réel.
- Conteneurisation avec Docker et Docker Compose.
- Architecture trois-tiers : base de données, couche service, couche API.
- Support de requêtes CRUD pour manipulation avancée de la base.

## Équipe projet

- Coline Brier  
- Antoine Croxo  
- Anass El Basraoui  
- Arnaud Favre-Bonvin  
- Mathieu Nobre  

Encadrant : Samuel Goutin


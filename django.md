
### 1. Initialisation du projet

- Installation de Django : `pip install django`
- Création du projet : `python -m django startproject config .`

### 2. Configuration Docker 🐳

- Création du `Dockerfile` (Python 3.12-slim)
- Création du `docker-compose.yml` (Services `web` et `db` PostgreSQL)
- Création du `.env` pour les variables d'environnement (DB, User, Password)
- Mise à jour de `.dockerignore`

### 3. Git & Versioning

- Initialisation du dépôt
- Création de la branche `mohamed`
- Ajout du remote : `https://github.com/ealmvin/patrimoineSportif.git`
- Push du code

### 4. Création des Modèles

- Analyse du fichier `sites-sportifs-emblematiques.json`
- Création des modèles dans `patrimoine_sportif/models.py` :
  - `SiteOlympique`
  - `Typologie`
  - `Denomination`
  - `DateReference`
  - `Site` (Model principal avec relations)

### 5. Base de données & Migrations

- Configuration de `config/settings.py` pour PostgreSQL (via `os.environ` et `.env`)
- Ajout de `psycopg2-binary` dans `requirements.txt`
- Exécution des migrations via Docker :
  ```bash
  docker-compose exec web python manage.py makemigrations
  docker-compose exec web python manage.py migrate
  ```

# Aide-mémoire Django

## 📋 Checklist d'Étapes

- [ ] Initialiser un projet django & Git
- [ ] Installer / configurer django
- [ ] Définir les models
- [ ] Migrer la base de données
- [ ] Lier à l'admin -> saisie des données
- [ ] Créer des vues & URLs
- [ ] Créer des templates
- [ ] Gérer les fichiers statiques
- [ ] Personnaliser l'admin

## ⚙️ Configuration & Commandes

### 1. Installation de l'environnement

```bash
python -m venv venv

# Windows (CMD/PowerShell)
venv\Scripts\activate

# Bash (Git Bash)
source venv/Scripts/activate
```

### 2. Initialisation du projet

```bash
pip install django
django-admin startproject config .  # crée le projet django (dans le dossier courant)
```

### 3. Commandes de gestion courantes

```bash
python manage.py migrate          # crée/met à jour la base de données
python manage.py createsuperuser  # crée un superuser (admin)
python manage.py runserver        # lance le serveur de développement
```
### 4. Création d'une app 

```bash

# arreter le serveur si il tourne


# creer une app
python manage.py startapp app_name

# ajouter l'app au projet
config/settings.py

# ajouter la vue
www/views.py 

# ajouter l'url
config/urls.py

# ajouter le template
www/templates/www/index.html

```
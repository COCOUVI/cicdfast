# cicdfast — API FastAPI avec chaîne CI/CD complète

Petite API FastAPI pour mettre en pratique une chaîne CI/CD complète, du push GitHub jusqu'à la mise en production sécurisée en HTTPS.

## Stack technique

- **FastAPI + Pytest** : API + tests automatisés
- **Docker + Docker Hub** : conteneurisation et registre d'images
- **GitHub Actions (CI/CD)** : intégration et déploiement continus
- **AWS EC2** : hébergement production
- **Nginx** : reverse proxy
- **DNS + HTTPS avec Let's Encrypt** : accès sécurisé

## Fonctionnement de la CI/CD

### CI — `.github/workflows/ci.yml`

Déclenchée sur `push` et `pull_request` vers `main` :

1. **format** : vérification avec `ruff format --check`
2. **test** : installation avec `uv` + exécution `pytest`
3. **docker** : build de l'image `cicdfast:latest`
4. **docker-push** : si tout réussit, build + push vers Docker Hub

### CD — `.github/workflows/cd.yml`

Déclenchée après succès de la CI :

1. Connexion SSH à EC2
2. `docker pull` de la dernière image depuis Docker Hub
3. Stop / remove de l'ancien conteneur
4. `docker run -d --restart unless-stopped -p 8000:8000`

En production, Nginx redirige le trafic vers le conteneur sur le port 8000, avec HTTPS via Let's Encrypt.

## API

Endpoints disponibles :

- `GET /` → `{"message": "API en ligne"}`
- `GET /health` → `{"status": "ok"}`
- `GET /mycicd` → `{"message": "ci et cd sont prets a 100 %"}`

## Installation locale

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancer le serveur

```bash
uvicorn app.main:app --reload
```

API disponible sur : http://localhost:8000
Docs Swagger : http://localhost:8000/docs

## Lancer les tests

```bash
pytest
```

## Lancer avec Docker

```bash
docker build -t cicdfast:latest .
docker run -p 8000:8000 cicdfast:latest
```

## Structure du projet

```
app/main.py             # endpoints FastAPI
tests/test_main.py      # tests Pytest
Dockerfile              # image Python 3.12-slim + uvicorn
.github/workflows/     # pipelines CI et CD
```

## Auteur

Alexandro COCOUVI

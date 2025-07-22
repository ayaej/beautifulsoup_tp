# 📚 TP BeautifulSoup4 – Scraping, API & Front

Projet complet réalisé dans le cadre d'un TP sur le scraping web avec BeautifulSoup4, incluant :

* un scraper Python + MongoDB
* une API Flask REST
* une interface React moderne et stylisée
* une configuration Docker pour exécution isolée

---

## 📁 Structure du projet

```
beautifulsoup_tp/
├── Backend/                      # Scraper, base MongoDB et API Flask
│   ├── scraper.py               # Récupération des articles
│   ├── database.py              # Connexion MongoDB (via Docker)
│   ├── filters.py               # Requêtes Mongo pour les filtres
│   ├── api.py                   # Routes Flask
│   ├── main.py                  # Lancement du scraping
│   └── requirements.txt        # Dépendances Python
│
├── tp-beautifulsoup4-front/    # Application React
│   ├── src/
│   │   ├── App.jsx              # Composant principal
│   │   ├── App.css              # Thème stylisé (couleurs, fond animé)
│   │   ├── components/          # Filtres et affichage articles
│   │   └── api.js               # Appels vers l'API Flask
│   └── public/                 # Fichiers statiques
│
├── docker-compose.yml          # Configuration Docker (MongoDB + Flask API)
└── README.md                   # Documentation
```

---

## ⚙️ Installation (avec Docker)

### 1. Prérequis

* [Docker](https://www.docker.com/) et [Docker Compose](https://docs.docker.com/compose/install/) installés

### 2. Lancer le projet

```bash
cd beautifulsoup_tp

docker-compose up --build
```

* Cela lance **MongoDB** (port 27017) et l'**API Flask** (port 5000)
* L’API sera disponible sur : [http://localhost:5000/articles](http://localhost:5000/articles)

### 3. Lancer le scraping dans le conteneur

```bash
docker-compose exec backend python main.py
```

Les articles seront insérés dans la base Mongo (service `mongo`)

---

## 📡 API Flask

L'API est démarrée automatiquement par Docker.

### Endpoints :

* `GET /articles` : liste des articles
* Filtres : `title`, `author`, `subcategory`, `startDate`, `endDate`

---

## 🗄️ Interface React (facultatif si déployée à part)

Lancer en local :

```bash
cd tp-beautifulsoup4-front
npm install
npm start
```

Accessible via : [http://localhost:3000](http://localhost:3000)

* Filtres dynamiques : titre, auteur, date, sous-catégorie
* Cartes stylées, responsive, avec fond animé

---

## 📆 Base de données MongoDB

Gérée via Docker avec :

```yaml
services:
  mongo:
    image: mongo:7.0
    ports:
      - "27017:27017"
```

Dans le code, la connexion se fait sur :

```python
MongoClient("mongodb://mongo:27017/")
```

---

## ✅ Améliorations possibles

* [ ] Ajouter un conteneur pour le front
* [ ] Déploiement complet (API + front)
* [ ] Ajout de tests automatisés



# 📚 TP BeautifulSoup4 – Scraping, API & Front

Projet complet réalisé dans le cadre d'un TP sur le scraping web avec BeautifulSoup4, incluant :

* un scraper Python + MongoDB
* une API Flask REST
* une interface React moderne et stylisée

---

## 📁 Structure du projet

```
beautifulsoup_tp/
├── Backend/                      # Scraper, base MongoDB et API Flask
│   ├── scraper.py               # Récupération des articles
│   ├── database.py              # Connexion MongoDB
│   ├── filters.py               # Requêtes Mongo pour les filtres
│   ├── api.py                   # Routes Flask
│   ├── main.py                  # Lancement du scraping
│   └── test.py                  # (Facultatif) tests simples
│
├── tp-beautifulsoup4-front/    # Application React
│   ├── src/
│   │   ├── App.jsx              # Composant principal
│   │   ├── App.css              # Thème stylisé (couleurs, fond animé)
│   │   ├── components/          # Filtres et affichage articles
│   │   └── api.js               # Appels vers l'API Flask
│   └── public/                 # Fichiers statiques
│
└── README.md                   # Documentation
```

---

## ⚙️ Installation

### Backend (Python)

```bash
cd Backend
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

🔧 Assure-toi d’avoir un serveur MongoDB local ou distant.

### Frontend (React)

```bash
cd tp-beautifulsoup4-front
npm install
npm start
```

---

## 🕸️ Scraping

Lancement manuel depuis `main.py` :

```bash
cd Backend
python main.py
```

➡️ Cela récupère les articles depuis plusieurs pages et les enregistre dans MongoDB.

---

## 🔌 API Flask

Pour lancer le serveur Flask :

```bash
cd Backend
flask run
```

Par défaut disponible sur `http://localhost:5000`

### Endpoints principaux :

* `/articles?title=...&author=...&subcategory=...&startDate=...&endDate=...`

---

## 🖼️ Interface React

Accessible sur `http://localhost:3000`

* Filtres dynamiques : titre, auteur, date, sous-catégorie
* Cartes d’articles stylées avec vignettes, badges, résumé, etc.
* Thème moderne 🎨 avec fond animé (CSS custom)

---

## ✅ À faire / Bonus possibles

* [ ] Déploiement sur Vercel (front) & Render/Heroku (API)
* [ ] Pagination des résultats dans le front
* [ ] Ajout de tests automatisés



from pymongo import MongoClient

def get_db():
    """
    Connexion à la base MongoDB locale.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tp_bs4"]
    return db

def save_article(article):
    """
    Insère un article dans la collection 'articles'
    """
    db = get_db()
    collection = db["articles"]

    # éviter les doublons via l'URL
    if not collection.find_one({"url": article["url"]}):
        collection.insert_one(article)
        print(f"✅ Article enregistré : {article['title']}")
    else:
        print(f"⚠️ Article déjà présent : {article['title']}")

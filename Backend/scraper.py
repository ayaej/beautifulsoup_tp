import requests
from bs4 import BeautifulSoup
from dateutil import parser
import re
import json
import time  # Ajout pour gérer les délais entre les requêtes

BASE_URL = "https://www.blogdumoderateur.com"

def get_article_links(max_pages=1):
    links = []
    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/page/{page}/" if page > 1 else BASE_URL
        print(f"🌐 Scraping page: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Vérifie les erreurs HTTP
        except requests.RequestException as e:
            print(f"❌ Erreur lors de la requête HTTP : {e}")
            continue

        soup = BeautifulSoup(response.content, "lxml")
        articles = soup.select("article header.entry-header a")
        for a in articles:
            href = a.get("href")
            if href:
                links.append(href)
        time.sleep(1)  # Délai pour éviter de surcharger le serveur
    return links

def scrape_article(url):
    print(f"\n🔎 Scraping {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Vérifie les erreurs HTTP
    except requests.RequestException as e:
        print(f"❌ Erreur lors de la requête HTTP : {e}")
        return None

    soup = BeautifulSoup(response.content, "lxml")
    article_data = {}

    # Titre
    title_tag = soup.find("h1", class_="entry-title") or soup.find("h1", class_="title-intro") or soup.find("h1")
    article_data["title"] = title_tag.text.strip() if title_tag else None
    if not article_data["title"]:
        print("❌ Titre introuvable")

    # Thumbnail
    thumbnail_tag = soup.find("meta", property="og:image")
    article_data["thumbnail"] = thumbnail_tag["content"] if thumbnail_tag else None

    # Catégories
    category_links = soup.select(".post-categories a, .entry-meta .category a, .breadcrumb a, .categories a")
    if not category_links:
        print(f"⚠️ Aucun lien de catégorie trouvé pour l'article : {url}")
        print(f"HTML brut des catégories : {soup.select_one('.post-categories, .entry-meta, .breadcrumb, .categories')}")
    if category_links:
        article_data["category"] = category_links[0].text.strip()
        article_data["subcategory"] = category_links[1].text.strip() if len(category_links) > 1 else None
    else:
        article_data["category"] = None
        article_data["subcategory"] = "Non spécifiée"  # Valeur par défaut

    if not article_data["subcategory"]:
        print(f"❌ Sous-catégorie introuvable pour l'article : {url}")

    # Résumé
    excerpt_tag = soup.find("p", class_="excerpt") or soup.select_one(".post-content > p")
    if excerpt_tag:
        article_data["summary"] = excerpt_tag.text.strip()
    else:
        meta_desc = soup.find("meta", attrs={"name": "description"})
        article_data["summary"] = meta_desc["content"].strip() if meta_desc and meta_desc.has_attr("content") else None

    if not article_data["summary"]:
        print("❌ Résumé introuvable")

    # Date
    date_tag = soup.find("time")
    if date_tag and date_tag.has_attr("datetime"):
        try:
            date_obj = parser.parse(date_tag["datetime"])
            article_data["date"] = date_obj.strftime("%Y-%m-%d")
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de la date : {e}")
            article_data["date"] = None
    else:
        article_data["date"] = None
        for script in soup.find_all("script"):
            if script.string and "dataLayer" in script.string:
                try:
                    match = re.search(r"dataLayer\s*=\s*(\[.*?\]);", script.string, re.DOTALL)
                    if match:
                        data = json.loads(match.group(1))
                        if isinstance(data, list) and "datePublished" in data[0]:
                            date_raw = data[0]["datePublished"]
                            date_obj = parser.parse(date_raw)
                            article_data["date"] = date_obj.strftime("%Y-%m-%d")
                            break
                except Exception as e:
                    print(f"❌ Erreur lors de l'analyse des données JSON : {e}")
                    continue

    if not article_data["date"]:
        print("❌ Date introuvable")

    # Auteur
    author_tag = (
        soup.select_one(".author a, .post-meta .author, .entry-meta .author, [rel='author'], .author-name")
        or soup.select_one(".byline a")  # Ajout d'un sélecteur alternatif
        or soup.select_one(".meta-author")  # Ajout d'un autre sélecteur alternatif
    )
    article_data["author"] = author_tag.text.strip() if author_tag else None
    if not article_data["author"]:
        print(f"❌ Auteur introuvable pour l'article : {url}")

    # Contenu
    content_block = soup.select_one(".post-content") or soup.select_one(".entry-content")
    if content_block:
        paragraphs = content_block.find_all(["p", "h2", "li"])
        text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.text.strip())
        article_data["content"] = text.strip()
    else:
        article_data["content"] = None

    if not article_data["content"]:
        print("❌ Contenu introuvable")

    # Images
    image_dict = []
    if content_block:
        images = content_block.find_all("img")
        for img in images:
            img_url = img.get("src") or img.get("data-src")
            alt_text = img.get("alt") or ""
            if img_url:
                image_dict.append({"url": img_url, "alt": alt_text.strip()})
    article_data["images"] = image_dict

    # URL
    article_data["url"] = url

    # Vérification minimale
    required = ["title", "content", "date"]
    if any(article_data.get(f) is None for f in required):
        print("❌ Article incomplet — non sauvegardé.")
        return None

    return article_data

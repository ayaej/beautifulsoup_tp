from scraper import get_article_links, scrape_article
from database import save_article

def main():
    links = get_article_links(max_pages=2)

    print(f"🔗 {len(links)} liens trouvés")

    for url in links:
        try:
            article = scrape_article(url)
            save_article(article)
        except Exception as e:
            print(f"❌ Erreur pour {url}: {e}")

if __name__ == "__main__":
    main()

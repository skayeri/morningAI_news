import feedparser
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import yaml
import os

# 썸네일 가져오기 함수
def get_thumbnail(url):
    try:
        html = requests.get(url, timeout=3).text
        soup = BeautifulSoup(html, 'html.parser')
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            return og["content"]
    except:
        pass
    return "assets/default.png"

# 메인 크롤링 함수
def crawl():
    with open("crawler/sites.yaml", "r", encoding="utf-8") as f:
        sites = yaml.safe_load(f)

    articles = []
    for source, rss_url in sites.items():
        feed = feedparser.parse(rss_url)
        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", ""),
                "source": source,
                "thumbnail": get_thumbnail(entry.link)
            })

    os.makedirs("feeds", exist_ok=True)
    with open("feeds/ai_news.json", "w", encoding="utf-8") as f:
        json.dump({
            "updated": datetime.now().isoformat(),
            "articles": articles
        }, f, ensure_ascii=False, indent=2)

    print(f"크롤링 완료: {len(articles)}개 기사 저장됨")

if __name__ == "__main__":
    crawl()

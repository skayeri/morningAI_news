import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

site_list_path = Path("crawler/site_list.json")
output_path = Path("output")
news_file = Path("news.json")  # moved to root for git.io
log_file = output_path / "log.json"
output_path.mkdir(exist_ok=True)

now = datetime.now()
date_str = now.strftime("%Y.%m.%d")
time_str = now.strftime("%H:%M")

log_data = {}
if log_file.exists():
    with open(log_file, "r", encoding="utf-8") as f:
        log_data = json.load(f)
if date_str not in log_data:
    log_data[date_str] = []
log_data[date_str].append(time_str)
run_count = len(log_data[date_str])

updated_at = f"{date_str}"
if run_count > 1:
    updated_at += f".({run_count}번째) {time_str}"
else:
    updated_at += f" {time_str}"

def fetch_generic_news(site):
    articles = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(site, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        if "brunch.co.kr" in site:
            for article in soup.select(".wrap_article .item_article")[:2]:
                title = article.select_one(".tit_subject").text.strip()
                link = article.select_one("a")['href']
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "news.hada.io" in site:
            for article in soup.select(".topic")[:2]:
                title = article.select_one(".title").text.strip()
                link = "https://news.hada.io" + article.select_one("a")['href']
                thumbnail = "https://news.hada.io/static/logo.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "it.chosun.com" in site:
            for article in soup.select(".list_item")[:2]:
                a_tag = article.select_one("a")
                if not a_tag: continue
                title = a_tag.text.strip()
                link = a_tag['href']
                if not link.startswith("http"):
                    link = "https://it.chosun.com" + link
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "eopla.net" in site:
            for article in soup.select(".post-preview")[:2]:
                a_tag = article.select_one("a")
                if not a_tag: continue
                title = a_tag.text.strip()
                link = a_tag['href']
                if not link.startswith("http"):
                    link = "https://eopla.net" + link
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "digitaltoday.co.kr" in site:
            for article in soup.select(".item")[:2]:
                title = article.select_one(".title").text.strip()
                link = article.select_one("a")["href"]
                if not link.startswith("http"):
                    link = "https://digitaltoday.co.kr" + link
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "itworld.co.kr" in site:
            for article in soup.select(".article-list .item")[:2]:
                a_tag = article.select_one("a")
                if not a_tag: continue
                title = a_tag.text.strip()
                link = a_tag['href']
                if not link.startswith("http"):
                    link = "https://www.itworld.co.kr" + link
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "aitimes.com" in site:
            for article in soup.select(".news_list li")[:2]:
                a_tag = article.select_one("a")
                if not a_tag: continue
                title = a_tag.text.strip()
                link = a_tag['href']
                if not link.startswith("http"):
                    link = "https://www.aitimes.com" + link
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "yozm.wishket.com" in site:
            for article in soup.select(".css-1dv1kvn")[:2]:  # 클래스는 변경될 수 있음
                title_el = article.select_one("h4")
                a_tag = article.select_one("a")
                if not title_el or not a_tag: continue
                title = title_el.text.strip()
                link = "https://yozm.wishket.com" + a_tag['href']
                thumbnail = article.select_one("img")
                thumbnail = thumbnail['src'] if thumbnail else "default.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

    except Exception as e:
        print(f"[Error] {site}: {e}")
    return articles

with open(site_list_path, "r", encoding="utf-8") as f:
    site_list = json.load(f)

all_articles = []
for site in site_list:
    all_articles.extend(fetch_generic_news(site))

with open(news_file, "w", encoding="utf-8") as f:
    json.dump({"updated_at": updated_at, "articles": all_articles}, f, ensure_ascii=False, indent=2)

with open(log_file, "w", encoding="utf-8") as f:
    json.dump(log_data, f, ensure_ascii=False, indent=2)
    

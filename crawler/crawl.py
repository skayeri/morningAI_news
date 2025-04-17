import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

site_list_path = Path("crawler/site_list.json")
output_path = Path("output")
news_file = output_path / "news.json"
log_file = output_path / "log.json"
output_path.mkdir(exist_ok=True)

# 날짜 및 시간 정보
now = datetime.now()
date_str = now.strftime("%Y.%m.%d")
time_str = now.strftime("%H:%M")

# 실행 로그
log_data = {}
if log_file.exists():
    with open(log_file, "r", encoding="utf-8") as f:
        log_data = json.load(f)
if date_str not in log_data:
    log_data[date_str] = []
log_data[date_str].append(time_str)
run_count = len(log_data[date_str])

# 업데이트 시간 포맷
updated_at = f"{date_str}"
if run_count > 1:
    updated_at += f".({run_count}번째) {time_str}"
else:
    updated_at += f" {time_str}"

# 간단한 사이트별 뉴스 크롤링 함수 예시
# 실제 크롤링 로직은 사이트 구조에 따라 구현 필요
def fetch_news_from(site):
    articles = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(site, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        if "brunch.co.kr" in site:
            for article in soup.select(".wrap_article .item_article")[:2]:
                title = article.select_one(".tit_subject").text.strip()
                link = article.select_one("a")['href']
                thumbnail = article.select_one("img")['src']
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        elif "news.hada.io" in site:
            for article in soup.select(".topic")[:2]:
                title = article.select_one(".title").text.strip()
                link = "https://news.hada.io" + article.select_one("a")['href']
                thumbnail = "https://news.hada.io/static/logo.png"
                articles.append({"title": title, "link": link, "thumbnail": thumbnail})

        # 다른 사이트는 필요시 추가 구현

    except Exception as e:
        print(f"[Error] {site}: {e}")
    return articles

# 전체 뉴스 수집
with open(site_list_path, "r", encoding="utf-8") as f:
    site_list = json.load(f)

all_articles = []
for site in site_list:
    all_articles.extend(fetch_news_from(site))

# 저장
with open(news_file, "w", encoding="utf-8") as f:
    json.dump({"updated_at": updated_at, "articles": all_articles}, f, ensure_ascii=False, indent=2)

with open(log_file, "w", encoding="utf-8") as f:
    json.dump(log_data, f, ensure_ascii=False, indent=2)

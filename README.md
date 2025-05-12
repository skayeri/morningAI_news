## 🗞️ Morning AI News
AI 관련 최신 뉴스를 매일 쉽게 확인할 수 있는 개인 뉴스 대시보드입니다.  
Python으로 뉴스 RSS 피드를 크롤링하여 `ainews.json`을 생성하고, GitHub Pages를 통해 미니 웹사이트로 시각화합니다.
👉 [사이트 바로가기](https://skayeri.github.io/morningAI_news/)<br><br>

## 🧠 주요 기능
- ✅ 주요 IT/AI 뉴스 사이트에서 기사 자동 수집
- ✅ 썸네일, 제목, 링크를 카드 형태로 시각화
- ✅ Python 실행 한 번으로 새 데이터 반영
- ✅ 깔끔하고 심플한 HTML/CSS UI
<br><br>

## 🗂️ 프로젝트 구조
```
morningAI_news
├── assets
│   └── default.png
├── crawler
│   ├── crawler.py
│   ├── site_list.json
│   └── utils.py
├── index.html
├── style.css
├── script.js
├── ainews.json
└── README.md
```

## 🛠️ 사용법

#### 1. 필수 라이브러리 설치

```bash conda install -c conda-forge feedparser beautifulsoup4 requests```

#### 2. 사이트 목록 수정 (crawler/site_list.json)
```json
[
  "https://news.hada.io/rss",
  "https://brunch.co.kr/rss",
  "https://digitaltoday.co.kr/rss"
]
```

#### 3. 크롤링 실행
```bash
cd crawler
python crawler.py
```

#### 4. GitHub Pages에서 확인
크롤링 후 ai_news.json이 최신 뉴스로 업데이트되며,
GitHub Pages에 자동 반영됩니다.
<br><br>
## 🎨 데모 UI (스크린샷)

![스크린샷 2025-05-12 232705](https://github.com/user-attachments/assets/3e58b553-de05-489b-9d1e-7d9b0ef3ed9c)

<br><br>
## 📌 TODO (계획 중)
- [x] 기사 날짜 추가
- [ ] 뉴스 페이지 추가
- [ ] UI 수정

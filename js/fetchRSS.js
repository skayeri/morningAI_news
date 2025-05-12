fetch('feeds/ai_news.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('news-container');
    data.articles.forEach(article => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <a href="${article.link}" target="_blank">
          <img src="${article.thumbnail}" alt="thumbnail">
        </a>
        <div class="card-body">
          <h3>${article.title}</h3>
          <p class="date">${formatDate(article.published)} 발행</p>
        </div>
      `;
      container.appendChild(card);
    });
  });

// 날짜 포맷팅 함수
function formatDate(dateString) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');  // 월은 0부터 시작하므로 1을 더해줘야 함
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  
  return `${year}.${month}.${day} ${hours}:${minutes}`;
}
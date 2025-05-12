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
        </div>
      `;
      container.appendChild(card);
    });
  });
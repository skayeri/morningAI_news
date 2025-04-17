fetch('../output/news.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("news-container");
    data.articles.forEach(article => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <a href="${article.link}" target="_blank">
          <img src="${article.thumbnail}" alt="thumbnail" />
          <h3>${article.title}</h3>
        </a>
      `;
      container.appendChild(card);
    });
    document.getElementById("timestamp").textContent = `업데이트: ${data.updated_at}`;
  })
  .catch(error => {
    console.error("Error loading news:", error);
  });

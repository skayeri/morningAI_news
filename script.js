fetch("news.json")
  .then((res) => res.json())
  .then((data) => {
    const container = document.getElementById("news-container");
    const timestamp = document.getElementById("timestamp");
    data.articles.forEach((article) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <a href="${article.link}" target="_blank">
          <img src="${article.thumbnail}" onerror="this.src='default.png'" alt="thumbnail">
          <div class="content">
            <a href="${article.link}" target="_blank">${article.title}</a>
          </div>
        </a>
      `;
      container.appendChild(card);
    });
    timestamp.textContent = `업데이트: ${data.updated_at}`;
  });

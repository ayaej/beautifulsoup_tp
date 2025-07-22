import React from "react";

function ArticleList({ articles }) {
  if (articles.length === 0) return <p>Aucun article trouvé.</p>;

  return (
    <div className="article-list">
      {articles.map((a, idx) => (
        <div key={idx} className="article-card">
          <h3>{a.title}</h3>
          <p><strong>Auteur :</strong> {a.author}</p>
          <p><strong>Date :</strong> {a.date}</p>
          <p>{a.summary}</p>
          <a href={a.url} target="_blank" rel="noopener noreferrer">Lire l'article</a>
        </div>
      ))}
    </div>
  );
}

export default ArticleList;

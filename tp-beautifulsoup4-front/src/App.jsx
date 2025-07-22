import React, { useState, useEffect } from "react";
import Filters from "./components/Filters";
import ArticleList from "./components/ArticleList";
import api from "./api";
import "./App.css";

function App() {
  const [filters, setFilters] = useState({
    title: "",
    author: "",
    subcategory: "",
    startDate: "",
    endDate: "",
  });

  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await api.get("/articles", { params: filters });
        setArticles(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, [filters]);

  return (
    <div className="App">
      <h1>TP BeautifulSoup - Articles</h1>
      <Filters filters={filters} onChange={setFilters} />
      <ArticleList articles={articles} />
    </div>
  );
}

export default App;

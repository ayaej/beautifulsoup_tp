import React from "react";

function Filters({ filters, onChange }) {
  return (
    <div className="filters">
      <input
        type="text"
        placeholder="Recherche par titre"
        value={filters.title}
        onChange={(e) => onChange({ ...filters, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="Auteur"
        value={filters.author}
        onChange={(e) => onChange({ ...filters, author: e.target.value })}
      />
      <input
        type="text"
        placeholder="Sous-catégorie"
        value={filters.subcategory}
        onChange={(e) => onChange({ ...filters, subcategory: e.target.value })}
      />
      <input
        type="date"
        value={filters.startDate}
        onChange={(e) => onChange({ ...filters, startDate: e.target.value })}
      />
      <input
        type="date"
        value={filters.endDate}
        onChange={(e) => onChange({ ...filters, endDate: e.target.value })}
      />
    </div>
  );
}

export default Filters;

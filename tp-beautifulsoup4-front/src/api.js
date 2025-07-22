import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // adresse de ton backend Flask
});

export default api;

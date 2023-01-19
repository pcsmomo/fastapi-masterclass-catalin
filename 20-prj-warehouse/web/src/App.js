import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Products } from "./routes/Products";
import { ProductsCreate } from "./routes/ProductCreate";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Products />} />
        <Route path="/create" element={<ProductsCreate />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Products } from "./routes/Products";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Products />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

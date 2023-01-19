import { useState } from "react";
import { useNavigate } from "react-router-dom";

export const ProductsCreate = () => {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");

  return (
    <div className="new_product body">
      <div className="new_product_title title">Create a new product</div>
      <div>
        <input
          className="input-1"
          placeholder="Name"
          onChange={(event) => setName(event.target.value)}
        />
      </div>
      <div>
        <input
          className="input-1"
          placeholder="Price"
          onChange={(event) => setPrice(event.target.value)}
        />
      </div>
      <div>
        <input
          className="input-1"
          placeholder="Quantity"
          onChange={(event) => setQuantity(event.target.value)}
        />
      </div>
      <button className="button-4" onClick={null}>
        Create product
      </button>
    </div>
  );
};

import { useEffect, useState } from "react";

export const Order = () => {
  const [id, setId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [message, setMessage] = useState("");

  return (
    <div className="body">
      <div className="order_title title">Order</div>
      <div>
        <input
          className="input-1"
          placeholder="Product ID"
          onChange={(event) => setId(event.target.value)}
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
        Place order
      </button>
      <div className="form_message">{message}</div>
    </div>
  );
};

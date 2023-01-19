import { useEffect, useState } from "react";

const PRODUCTS_URL = "http://localhost:8000/";
const ORDERS_URL = "http://localhost:8001/";

export const Order = () => {
  const [id, setId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(PRODUCTS_URL + "product/" + id)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        const price = parseFloat(data.price) * 1.2;
        setMessage(`Your product price is $${price}`);
      });
  }, [id]);

  const handleCreate = (event) => {
    event.preventDefault();

    const json_string = JSON.stringify({
      product_id: id,
      quantity: quantity,
    });

    const requestOptions = {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: json_string,
    };

    fetch(ORDERS_URL + "orders", requestOptions)
      .then((response) => {
        if (!response.ok) {
          throw response;
        }
      })
      .then((data) => {
        setMessage(`Order for ${quantity} items sent`);
      })
      .catch((error) => {
        console.log(error);
      });
  };

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
      <button className="button-4" onClick={handleCreate}>
        Place order
      </button>
      <div className="form_message">{message}</div>
    </div>
  );
};

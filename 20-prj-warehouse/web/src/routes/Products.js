import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Products.css";

const BASE_URL = "http://localhost:8000/";

export const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + "products")
      .then((response) => {
        const json = response.json();
        if (response.ok) {
          return json;
        }
        throw response;
      })
      .then((data) => {
        setProducts(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="products_div body">
      <div className="products_title title">Products</div>
      <div className="products_add_div">
        <Link to={`/create`} className="product_add button-4">
          Add
        </Link>
        <table className="products_table">
          <thead className="products_table_head">
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
            <th scope="col">Actions</th>
          </thead>
          <tbody>
            {products.map((product) => {
              return (
                <tr className="products_table_row" key={product.id}>
                  <td className="products_table_td">{product.id}</td>
                  <td className="products_table_td">{product.name}</td>
                  <td className="products_table_td">{product.price}</td>
                  <td className="products_table_td">{product.quantity}</td>
                  <td className="products_table_td">
                    <button className="product_delete_link" onClick={null}>
                      Delete
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <div className="products_order_div">
        <Link to={`/order`} className="products_order button-4">
          Order
        </Link>
      </div>
    </div>
  );
};

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';
import './styles/Store.css';


const baseURL = 'http://localhost:8000'
const apiURL = `${baseURL}/api`






const Store = () => {
    const [products, setProducts] = useState([])

    const getProducts = () => {
        axios.get(`${apiURL}/products/`).then(res => {
            setProducts(res.data)
            console.log(res.data);
        })
    }

    useEffect(() => {
        getProducts()
    }, [])




    return (
        <div>
            <h1>Store Page</h1>
            {
                products.map(
                    (product, index) =>
                        <ProductCard product={product} url={baseURL} />
                )
            }
        </div>
    );
}

export default Store;

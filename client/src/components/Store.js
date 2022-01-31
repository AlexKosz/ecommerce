import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';





const Store = () => {
    const [products, setProducts] = useState([])

    const baseURL = 'http://localhost:8000/api/'

    const getProducts = () => {
        axios.get(`${baseURL}products/`).then(res => {
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
                        <ProductCard product={product} />
                )
            }
        </div>
    );
}

export default Store;

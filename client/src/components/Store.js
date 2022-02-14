import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';
import './styles/Store.css';


const Store = (props) => {
    const baseURL = props.urls.baseURL
    const apiURL = props.urls.apiURL


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
        <div className='mainStore'>
            <h1>Store Page</h1>
            <div className='productsWrapper'>
                {
                    products.map(
                        (product, index) =>
                            <a href={`/product/${product.id}`} key={product.id}><ProductCard product={product} url={baseURL} /></a>
                    )
                }
            </div>
        </div>
    );
}

export default Store;

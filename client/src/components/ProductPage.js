import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/ProductPage.css';


const baseURL = 'http://localhost:8000'
const apiURL = `${baseURL}/api`


const ProductPage = () => {
    const [product, setProduct] = useState([])

    const getProduct = () => {
        axios.get(`${apiURL}/products/`).then(res => {
            setProduct(res.data)
            console.log(res.data);
        })
    }

    useEffect(() => {
        getProduct()
    }, [])




    return (
        <div className='mainProductPage'>
            <h3>Product</h3>
        </div>
    );
}

export default ProductPage;

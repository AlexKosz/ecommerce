import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/ProductPage.scss';
import { useParams } from '@reach/router';
import Stars from './Stars';

const ProductPage = (props) => {
    const apiURL = props.urls.apiURL
    const baseURL = props.urls.baseURL
    const { productId } = useParams()
    const [product, setProduct] = useState([])

    const getProduct = () => {
        axios.get(`${apiURL}/product/${productId}`).then(res => {
            setProduct(res.data)
            console.log(res.data);
        })
    }

    useEffect(() => {
        getProduct()
    }, [])

    const percent = product.average_star_rating * 20

    return (
        <div className='mainProductPage'>
            <a href="/">Back to main page</a>
            <div className='mainProductWrapper'>
                <img src = {`${baseURL}${product.image}`} />
                <div className='productInfo'>
                    <h1>{product.name}</h1>
                    <Stars rating={product.average_star_rating}/>
                </div>
                <div className='productActions'>
                    <button>Add to cart</button>
                </div>
                
            </div>

        </div>
    );
}

export default ProductPage;

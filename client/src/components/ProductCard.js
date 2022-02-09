import React from 'react';
import './styles/ProductCard.css';

const ProductCard = (props) => {
    const url = props.url
    const product = props.product

    const dollars = Math.floor(product.price_in_cents / 100)
    let cents = product.price_in_cents % 100



    if (product.image == '/default.jpg') {
        product.image = null
    }


    if (cents < 10) {
        cents = '0' + cents.toString()
    }



    return (
        <div className='productCard'>
            <h1>{product.name}</h1>
            <h2>{`${dollars}.${cents}`}</h2>
            <img src={`${url}${product.image}`} alt={product.description} className='productCardImage'/>
        </div>
    );





}

export default ProductCard;
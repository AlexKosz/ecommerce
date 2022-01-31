import React from 'react';


const ProductCard = (props) => {
    console.log('a');
    const product = props.product
    const dollars = Math.floor(product.price_in_cents / 100)
    let cents = product.price_in_cents % 100

    if (cents < 10) {
        cents = '0' + cents.toString()
    }



    return (
        <div>
            <h1>{product.name}</h1>
            <h2>{`${dollars}.${cents}`}</h2>
            <img src={product.image} />
        </div>
    );
}

export default ProductCard;
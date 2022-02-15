export const addToCart = (item, quantity, userId) =>{
    let cart = JSON.parse(window.localStorage.getItem("cart"));
    if(cart){
        if(cart[item]){
            cart[item] = cart[item] + quantity
        }
        else{
            cart[item] = quantity
        }
    }
    else{
        cart[item] = quantity
    }

    window.localStorage.setItem("cart", JSON.stringify(cart));
    console.log(JSON.parse(window.localStorage.getItem("cart")))





    if(userId != null){
        console.log("You are logged in")
    }    
}


export const mergeCarts= () => {
    console.log("merging now")
    // let sessionCart = JSON.parse(window.localStorage.getItem("cart"))
    // let user = JSON.parse(window.localStorage.getItem("user"));
    

}


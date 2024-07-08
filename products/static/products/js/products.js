var productPrice = document.getElementById("product-price");
var currencyFormatter = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' });

document.getElementById("id_product_size").addEventListener("change", (event)=>{let price = priceList[0];
    if (event.target.value.includes('Large')){
        price = priceList[1];
    };
    productPrice.innerText = currencyFormatter.format(price);
    console.log(currencyFormatter.format(price));
});
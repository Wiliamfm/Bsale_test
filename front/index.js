let base_url= "http://localhost:8000";
document.addEventListener('DOMContentLoaded', () => {
    let page= sessionStorage.getItem("page");
    if(page == null){
        page= 1;
        sessionStorage.setItem("page", page);
    }
    getProducts(base_url + '?page=' + page)
    document.getElementById("previous_page").addEventListener('click', () => {
        pagination("prev");
    })
    document.getElementById("next_page").addEventListener('click', () => {
        pagination("next");
    });
    document.getElementById("btn_search").addEventListener('submit', (event) => {
        event.preventDefault();
        console.log(document.getElementById("input_search").value);
        getProducts(base_url + "?q=" + document.getElementById("input_search").value);
    });
});

function pagination(type){
    let div= document.getElementById("div_products");
    div.textContent= "";
    let page= sessionStorage.getItem("page");
    if(type == "next"){
        page++;
    }else{
        page--;
    }
    sessionStorage.setItem("page", page);
    getProducts(base_url + '?page=' + page)
}

function getProducts(url){
    fetch(url)
    .then(response => response.json())
    .then(products => {
        let div= document.getElementById("div_products");
        div.style.padding= "10px";
        div.style.margin= "10px"
        //div.style.display= "flex";
        for(let i = 0; i < products.length; i++){
            //console.log(products[i]);
            let div_card= document.createElement("div");
            div_card.className= "card";
            //div_card.style.width= "800px";
            div_card.style.margin= "5px";
            div.appendChild(div_card);
            let img= document.createElement("img");
            img.className= "card-img-top";
            img.src= products[i].url_image;
            img.alt= products[i].name;
            //img.width= "100";
            //img.height= "100";
            div_card.appendChild(img);
            let div_body= document.createElement("div");
            div_body.className= "card-body";
            let name= document.createElement("h1");
            name.textContent= products[i].name;
            div_body.appendChild(name);
            let category= document.createElement("h6");
            category.textContent= products[i].category.name;
            div_body.appendChild(category);
            let price= document.createElement("h6");
            price.textContent= "PRICE: " + products[i].price;
            div_body.appendChild(price);
            let discount= document.createElement("h6");
            discount.textContent= "DISCOUNT: " + products[i].discount;
            div_body.appendChild(discount);
            div_card.appendChild(div_body);
        };
    }).catch(err => console.log(err));
}
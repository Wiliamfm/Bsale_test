let base_url= "http://localhost:8000";
document.addEventListener('DOMContentLoaded', () => {
    getProducts(base_url);
});

function getProducts(url){
    fetch(url)
    .then(response => response.json())
    .then(products => {
        console.log(products);
    }).catch(err => console.log(err));
}
from fastapi import FastAPI
from db_models import db, Product as db_product, Category as db_category
from models import Product, Category

ITEMS_PER_PAGE= 10

app = FastAPI()
@app.get("/")
async def root(q: str | None= None, category: str | None = None, order: str | None = None, page: int | None = None):
    """ Get all products store in the database. Params: - query: filter products by 'query'. - category: filter products by categor - order: order products ascending or descending. - page: pagination for products. returns: List of products: """
    db.connect()
    query= db_product.select(db_product, db_category).join(db_category).paginate(1, ITEMS_PER_PAGE)
    if q:
        query= query.where(db_product.id.in_(db_product.select(db_product.id).join(db_category).where(db_product.name.contains(q))))
    if category:
        query= query.where(db_product.id.in_(db_product.select(db_product.id).join(db_category).where(db_category.name.contains(category))))
    if order:
        if order == "DESC":
            query= query.order_by(db_product.name.desc())
        else:
            query= query.order_by(db_product.name)
    if page:
        query= query.paginate(page, ITEMS_PER_PAGE)
    products: list[Product]= [Product(id= p.id, name= p.name, url_image= p.url_image, price= p.price, discount= p.discount, category= Category(id= p.category.id, name= p.category.name)) for p in query]
    db.close()
    return products

@app.get("/category")
async def category ():
    db.connect()
    query= db_category.select()
    categories: list[Category]= [Category(id= c.id, name= c.name) for c in query]
    db.close()
    return categories
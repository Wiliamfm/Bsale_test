from fastapi import FastAPI
from db_models import db, Product as db_product, Category as db_category
from models import Product, Category

ITEMS_PER_PAGE= 20

app = FastAPI()
@app.get("/")
async def root(q: str | None= None, category: str | None = None, order: str | None = None, page: int | None = None):
    """ Get all products store in the database. Params: - query: filter products by 'query'. - category: filter products by categor - order: order products ascending or descending. - page: pagination for products. returns: List of products: """
    db.connect()
    query= db_product.select(db_product, db_category).join(db_category).paginate(1, ITEMS_PER_PAGE)
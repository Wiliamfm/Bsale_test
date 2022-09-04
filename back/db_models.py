from decimal import Decimal
from peewee import *

db= MySQLDatabase(database= "bsale_test", user= "bsale_test", password= "bsale_test", host= "mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com", autoconnect= False)

class Category(Model):
    id: int = IntegerField()
    name: str = CharField()

    class Meta:
        database= db

class Product(Model):
    id: int = IntegerField()
    name: str= CharField()
    url_image: str= CharField()
    price: Decimal= DecimalField()
    discount: int= IntegerField()
    category: Category= ForeignKeyField(Category, column_name= "category")

    class Meta:
        database= db
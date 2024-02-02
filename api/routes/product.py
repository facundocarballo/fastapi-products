from fastapi import APIRouter, HTTPException
from domain.product import Product
from database.connection import create_local_connection
from infrastructure.product.mongodb import ProductRepositoryMongoDB

product_routes = APIRouter()
mongo_client = create_local_connection()
db = mongo_client["ScalablePath"]
product_collection = db["product"]

@product_routes.post("/product")
async def create_product(product: Product):
    mongo_repository = ProductRepositoryMongoDB(product_collection)
    try:
        new_product = mongo_repository.create(product)
        return {
            "message": "Product created...",
            "product": new_product
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@product_routes.get("/product")
async def get_products():
    mongo_repository = ProductRepositoryMongoDB(product_collection)
    try:
        products = await mongo_repository.get()
        return {
            "message": "Product created...",
            "products": products
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_routes.delete("/product")
async def delete_product(product: Product):
    mongo_repository = ProductRepositoryMongoDB(product_collection)
    try:
        product_deleted = mongo_repository.delete(product)
        return {
            "message": "Task deleted successfully.",
            "task": product_deleted
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
from domain.product import Product
from infrastructure.product.repository import ProductRepository
from pymongo.collection import Collection
from datetime import datetime
from bson import ObjectId

class ProductRepositoryMongoDB(ProductRepository):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection
        super().__init__()

    def create(self, product: Product) -> Product:
        dict_product = dict(product)
        del dict_product["id"]

        try:
            product_id = self.collection.insert_one(dict_product).inserted_id
        except Exception as e:
            raise ValueError("Error inserting product. " + str(e))

        return Product(
            id=str(product_id),
            name=product.name,
            description=product.description,
            photo_url=product.photo_url,
            price=product.price,
            deleted_at=None
        )
    
    def delete(self, product: Product) -> Product:
        product.deleted_at = datetime.now().timestamp()
        try:
            res = self.collection.update_one({"_id": ObjectId(product.id)}, {
                "$set": {
                    "deleted_at": product.deleted_at
                }
            })
            print("Result: ", res)
        except Exception as e:
            raise ValueError("Error deleting the product. " + str(e))
        
        return product
    
    async def get(self) -> [Product]:
        products = []
        try:
            cursor = self.collection.find({"deleted_at": None})
            for doc in cursor:
                products.append(Product(
                    id=str(doc["_id"]),
                    name=doc["name"],
                    description=doc["description"],
                    photo_url=doc["photo_url"],
                    price=doc["price"],
                    deleted_at=doc["deleted_at"]
                ))

        except Exception as e:
            raise ValueError("Error finding all the products. " + str(e))

        return products
    
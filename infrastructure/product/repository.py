from abc import ABC, abstractmethod
from domain.product import Product

class ProductRepository:
    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get(self, product: Product) -> [Product]:
        pass

    @abstractmethod
    def delete(self, product: Product) -> Product:
        pass
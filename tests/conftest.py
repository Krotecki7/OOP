import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def category(product, product2):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения функций для удобства жизни",
        products=[product, product2],
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

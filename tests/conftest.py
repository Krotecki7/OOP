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


product_1 = ["Sony QLED 4K", "Фоновая подсветка", 123000.0, 7]


@pytest.fixture
def category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром",
        products=[product_1],
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


product_1 = ["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7]


@pytest.fixture
def category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром",
        products=[product_1]
    )

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


@pytest.fixture
def category(product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения функций для удобства жизни",
        products=[product]
    )

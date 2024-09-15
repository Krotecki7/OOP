import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def lawngrass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def lawngrass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

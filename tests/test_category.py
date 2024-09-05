
def test_category(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения функций для удобства жизни"
    )

    assert len(category.products_in_list) == 2
import pytest
from src.product import Product
from src.category import Category


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения функций для удобства жизни"

    assert len(category.products_in_list) == 1
    assert category.category_count == 1


def test_products_property(category):
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0. Остаток: 5\n"
        "Iphone 15, 210000.0. Остаток: 8\n"
    )


def test_str_category(category):
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0. Остаток: 5\n"


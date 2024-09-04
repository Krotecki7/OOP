import pytest
from src.product import Product
from src.category import Category


product_1 = ["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7]


def test_category(category):
    assert category.name == "Телевизоры"
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром"

    assert len(category.products_in_list) == 1
    assert category.category_count == 2


def test_products_property(category):
    assert '55" QLED 4K, 123000.0. Остаток: 7'

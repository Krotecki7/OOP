import pytest


product_1 = ["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7]


def test_category(category):
    assert category.name == "Телевизоры"
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert category.products == [product_1]

    assert len(category.products) == 1
    assert category.category_count == 1

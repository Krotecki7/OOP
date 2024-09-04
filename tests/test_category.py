product_1 = ["Sony QLED 4K", "Фоновая подсветка", 123000.0, 7]


def test_category(category):
    assert category.name == "Телевизоры"
    assert (
        category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром"
    )

    assert len(category.products_in_list) == 1
    assert category.category_count == 1


def test_products_property(category):
    assert category.products == "['Sony QLED 4K', 'Фоновая подсветка', 123000.0, 7]\n"

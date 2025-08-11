from _pydecimal import Decimal

from domain.product import Product


def test_product_initialization():
    product = Product("Pipoca", Decimal('5.99'))
    assert product.get_name() == "Pipoca"
    assert product.get_price() == Decimal('5.99')


def test_product_price():
    product = Product("Refrigerante", Decimal('2.50'))
    assert product.get_price() == Decimal('2.50')
    product = Product("Doce", Decimal('1.25'))
    assert product.get_price() == Decimal('1.25')


def test_product_name():
    product = Product("Batatas", Decimal('3.00'))
    assert product.get_name() == "Batatas"
    product = Product("Chocolate", Decimal('4.50'))
    assert product.get_name() == "Chocolate"

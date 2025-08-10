from domain.customer import Customer


def test_create_customer():
    customer = Customer('João', '12345678901')
    assert customer.get_name() == 'João'
    assert customer.get_document() == '12345678901'


def test_set_customer_name():
    customer = Customer('Maria', '98765432100')
    customer.set_name('Ana')
    assert customer.get_name() == 'Ana'
    assert customer.get_document() == '98765432100'


def test_customer_document():
    customer = Customer('Carlos', '11223344556')
    assert customer.get_document() == '11223344556'
    customer.set_name('Roberto')
    assert customer.get_name() == 'Roberto'
    assert customer.get_document() == '11223344556'

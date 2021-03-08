import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt' : 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt' : 5, 'unit_price': 7.5, 'discount': 10}}
    return products
@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateOrderSim1(invoice):
    invoice = Invoice()
    products = {'Computer': {'qnt': 10, 'unit_price': 999.99, 'discount': 3.1415},
                'Laptop': {'qnt': 5, 'unit_price': 799.99, 'discount': 0}}
    assert invoice.totalPurePrice(products) == 13685.7

def test_CanCalculateOrderSim2(invoice):
    invoice = Invoice()
    products = {'Pen': {'qnt': 0, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 1, 'unit_price': 7.5, 'discount': 100}}
    assert invoice.totalPurePrice(products) == 0.0
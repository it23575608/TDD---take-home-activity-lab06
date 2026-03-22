# tests/test_discounts.py
import pytest
from unittest.mock import Mock
from src.cart import Cart

def setup_cart_with_item(sku, price, qty, available=100):
    mock_catalog = Mock()
    mock_catalog.get_by_sku.return_value = Mock(price=price)
    mock_inventory = Mock()
    mock_inventory.get_available.return_value = available
    cart = Cart(catalog=mock_catalog, inventory_service=mock_inventory)
    cart.add_item(sku, qty)
    return cart

def test_bulk_discount_applied_at_10_units():
    
    cart = setup_cart_with_item("BULK-ITEM", 100, 10)
    assert cart.get_total() == 900

def test_order_discount_applied_at_1000_total():
    
    cart = setup_cart_with_item("EXPENSIVE-ITEM", 1000, 1)
    assert cart.get_total() == 950
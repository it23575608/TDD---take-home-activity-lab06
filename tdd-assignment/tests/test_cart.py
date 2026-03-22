# tests/test_cart.py
import pytest
from unittest.mock import Mock
from src.cart import Cart

def test_add_item_not_in_catalog_fails():
    # Mocking the catalog
    mock_catalog = Mock()
    mock_catalog.get_by_sku.return_value = None  # Simulate SKU not found
    
    cart = Cart(catalog=mock_catalog)
    with pytest.raises(ValueError, match="Product not in catalog"):
        cart.add_item(sku="INVALID-SKU", quantity=1)

def test_remove_item_decreases_total():
    mock_catalog = Mock()
    # Mock returning a product object with a price of 100
    mock_product = Mock(price=100)
    mock_catalog.get_by_sku.return_value = mock_product
    
    cart = Cart(catalog=mock_catalog)
    cart.add_item("PROD-01", 2) # Total 200
    cart.remove_item("PROD-01")
    assert cart.get_total() == 0
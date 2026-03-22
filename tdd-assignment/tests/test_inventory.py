
import pytest
from unittest.mock import Mock
from src.cart import Cart

def test_add_item_fails_if_insufficient_inventory():
    mock_catalog = Mock()
    mock_catalog.get_by_sku.return_value = Mock(price=100)
    
    
    mock_inventory = Mock()
    mock_inventory.get_available.return_value = 5 
    
    
    cart = Cart(catalog=mock_catalog, inventory_service=mock_inventory)
    
    
    with pytest.raises(ValueError, match="Insufficient inventory"):
        cart.add_item(sku="LAPTOP-001", quantity=10)
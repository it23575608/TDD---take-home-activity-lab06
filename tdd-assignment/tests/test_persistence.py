# tests/test_persistence.py
import pytest
from unittest.mock import Mock
from src.checkout import CheckoutService

def test_successful_checkout_creates_and_saves_order():
    mock_gateway = Mock()
    mock_inventory = Mock()
    mock_inventory.get_available.return_value = 100
    
    # A simple list to act as our "Fake Repository"
    fake_order_repo = [] 
    
    mock_cart = Mock()
    mock_cart.get_total.return_value = 500
    mock_cart.items = [] # Simplified for the test
    
    # Passing order_repo into the service (this will cause a TypeError)
    service = CheckoutService(
        payment_gateway=mock_gateway, 
        inventory_service=mock_inventory, 
        order_repo=fake_order_repo
    )
    
    service.process(mock_cart, token="tok_123")
    
    assert len(fake_order_repo) == 1
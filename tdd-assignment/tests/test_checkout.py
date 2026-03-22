import pytest
from unittest.mock import Mock
from src.checkout import CheckoutService

def test_checkout_fails_on_payment_error():
    # 1. Setup mocks for BOTH dependencies
    mock_gateway = Mock()
    mock_gateway.charge.side_effect = Exception("Card Declined")
    
    mock_inventory = Mock() # The missing piece!
    
    mock_cart = Mock()
    mock_cart.get_total.return_value = 500
    mock_cart.items = [] 
    
    # 2. Inject both into the service
    service = CheckoutService(payment_gateway=mock_gateway, inventory_service=mock_inventory)
    
    # 3. Action
    result = service.process(mock_cart, token="bad_card")
    
    # 4. Assert
    assert result == "PAYMENT_FAILED"
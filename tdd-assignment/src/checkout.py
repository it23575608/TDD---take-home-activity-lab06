import datetime

class Order:
    """The Domain Object representing a completed purchase."""
    def __init__(self, items, total):
        self.items = items
        self.total = total
        self.timestamp = datetime.datetime.now()

class CheckoutService:
    def __init__(self, payment_gateway, inventory_service, order_repo):
        self.payment_gateway = payment_gateway
        self.inventory_service = inventory_service
        self.order_repo = order_repo

    def process(self, cart, token):
        if not self._is_stock_available(cart):
            return "ERR_STOCK"

        try:
            total_price = cart.get_total()
            self.payment_gateway.charge(total_price, token)
            
            # Use the repository interface to save
            new_order = Order(items=cart.items, total=total_price)
            self.order_repo.append(new_order) 
            
            return "SUCCESS"
        except Exception:
            return "PAYMENT_FAILED"

    def _is_stock_available(self, cart):
        return all(self.inventory_service.get_available(i.sku) >= i.quantity for i in cart.items)
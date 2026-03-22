class LineItem:
    def __init__(self, sku, price, quantity):
        self.sku = sku
        self.price = price
        self.quantity = quantity

class DiscountRules:
    @staticmethod
    def apply_bulk(item):
        if item.quantity >= 10:
            return (item.price * item.quantity) * 0.10
        return 0

    @staticmethod
    def apply_order_discount(total):
        if total >= 1000:
            return total * 0.05
        return 0

class Cart:
    def __init__(self, catalog, inventory_service):
        self.catalog = catalog
        self.inventory_service = inventory_service
        self.items = []

    def add_item(self, sku, quantity):
        if quantity <= 0: raise ValueError("Quantity must be positive")
        
        if self.inventory_service.get_available(sku) < quantity:
            raise ValueError("Insufficient inventory")

        product = self.catalog.get_by_sku(sku)
        if not product: raise ValueError("Product not in catalog")
        
        self.items.append(LineItem(sku, product.price, quantity))

    def get_total(self):
        total = 0
        for item in self.items:
            line_total = (item.price * item.quantity) - DiscountRules.apply_bulk(item)
            total += line_total
        
        total -= DiscountRules.apply_order_discount(total)
        return total
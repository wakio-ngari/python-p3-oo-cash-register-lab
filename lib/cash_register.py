class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction = 0.0
    
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.last_transaction = price * quantity
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0
    
    def get_items(self):
        return self.items

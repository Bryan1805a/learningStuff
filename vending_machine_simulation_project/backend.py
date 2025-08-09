class VendingMachine:
    """Backend logic for the vending machine"""
    
    def __init__(self):
        self.products = [
            {"name": "Coca Cola", "price": 25, "stock": 10},
            {"name": "Orange Juice", "price": 15, "stock": 8},
            {"name": "Pepsi", "price": 25, "stock": 12},
            {"name": "Coffee", "price": 12, "stock": 15},
            {"name": "Fresh Water", "price": 8, "stock": 20},
            {"name": "Tea", "price": 10, "stock": 10}
        ]
        self.inserted_money = 0
        self.selected_product = None
    
    def get_products(self):
        """Return list of available products"""
        return self.products.copy()
    
    def insert_money(self, amount):
        """Add money to the machine"""
        if amount > 0:
            self.inserted_money += amount
            return True
        return False
    
    def select_product(self, product_name):
        """Select a product by name"""
        for product in self.products:
            if product["name"] == product_name and product["stock"] > 0:
                self.selected_product = product
                return True
        return False
    
    def can_purchase(self):
        """Check if current selection can be purchased"""
        if not self.selected_product:
            return False, "No product selected"
        
        if self.selected_product["stock"] <= 0:
            return False, "Product out of stock"
            
        if self.inserted_money < self.selected_product["price"]:
            needed = self.selected_product["price"] - self.inserted_money
            return False, f"Insufficient funds. Need ${needed} more"
            
        return True, "Ready to purchase"
    
    def purchase(self):
        """Complete the purchase transaction"""
        can_buy, message = self.can_purchase()
        
        if not can_buy:
            return False, message, 0
        
        # Calculate change
        change = self.inserted_money - self.selected_product["price"]
        
        # Update stock
        self.selected_product["stock"] -= 1
        
        # Store purchase info for return
        purchased_item = self.selected_product["name"]
        
        # Reset machine state
        self.inserted_money = 0
        self.selected_product = None
        
        return True, f"Purchased {purchased_item} successfully!", change
    
    def cancel_transaction(self):
        """Cancel transaction and return all money"""
        refund = self.inserted_money
        self.inserted_money = 0
        self.selected_product = None
        return refund
    
    def get_status(self):
        """Get current machine status"""
        return {
            "inserted_money": self.inserted_money,
            "selected_product": self.selected_product["name"] if self.selected_product else None,
            "selected_price": self.selected_product["price"] if self.selected_product else 0
        }
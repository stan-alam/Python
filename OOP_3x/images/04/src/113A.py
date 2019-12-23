#113.A
class InvalidWithDrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account does not have sufficient funds for ${amount}")
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance

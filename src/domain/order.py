from src.domain.coffee_bean import CoffeeBean


class Order:
    """Representa un pedido de café."""

    def __init__(self, coffee_bean: CoffeeBean, grams: int, preparation_method: str):
        self.coffee_bean = coffee_bean
        self.grams = grams
        self.preparation_method = preparation_method
        self.status = "PENDING"

    def confirm(self):
        self.status = "CONFIRMED"

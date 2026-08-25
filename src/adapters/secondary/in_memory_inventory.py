from src.ports.inventory_port import InventoryPort


class InMemoryInventoryAdapter(InventoryPort):
    """Implementa InventoryPort usando un diccionario en memoria."""

    def __init__(self):
        self.inventory = {
            "Geisha": 1000,
            "Bourbon Rosado": 800,
            "Caturra": 500,
        }

    def has_stock(self, bean_name: str, grams: int) -> bool:
        available = self.inventory.get(bean_name, 0)
        return available >= grams

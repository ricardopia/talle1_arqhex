from abc import ABC, abstractmethod


class InventoryPort(ABC):
    """Contrato para consultar si existe inventario suficiente."""

    @abstractmethod
    def has_stock(self, bean_name: str, grams: int) -> bool:
        pass

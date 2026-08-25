from abc import ABC, abstractmethod
from src.domain.order import Order


class OrderRepositoryPort(ABC):
    """Contrato para guardar un pedido."""

    @abstractmethod
    def save(self, order: Order) -> None:
        pass

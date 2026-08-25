from src.domain.order import Order
from src.ports.order_repository_port import OrderRepositoryPort


class InMemoryOrderAdapter(OrderRepositoryPort):
    """Implementa OrderRepositoryPort guardando pedidos en una lista."""

    def __init__(self):
        self.orders = []

    def save(self, order: Order) -> None:
        self.orders.append(order)

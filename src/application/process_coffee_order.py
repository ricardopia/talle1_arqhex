from src.domain.exceptions import InsufficientInventoryError
from src.domain.order import Order
from src.ports.inventory_port import InventoryPort
from src.ports.order_repository_port import OrderRepositoryPort


class ProcessCoffeeOrderUseCase:
    """Caso de uso que procesa un pedido de café."""

    def __init__(
        self,
        inventory_port: InventoryPort,
        order_repository_port: OrderRepositoryPort,
    ):
        # Inyección de dependencias: recibe puertos, no adaptadores concretos.
        self.inventory_port = inventory_port
        self.order_repository_port = order_repository_port

    def execute(self, order: Order) -> Order:
        has_stock = self.inventory_port.has_stock(
            order.coffee_bean.name,
            order.grams,
        )

        if not has_stock:
            raise InsufficientInventoryError(
                "No hay inventario suficiente para procesar el pedido."
            )

        order.confirm()
        self.order_repository_port.save(order)
        return order

from src.domain.coffee_bean import CoffeeBean
from src.domain.order import Order
from src.domain.exceptions import InsufficientInventoryError
from src.application.process_coffee_order import ProcessCoffeeOrderUseCase


class CoffeeOrderCLI:
    """Adaptador primario: permite al usuario entrar al sistema por consola."""

    def __init__(self, process_order_use_case: ProcessCoffeeOrderUseCase):
        self.process_order_use_case = process_order_use_case

    def run(self):
        print("\n=== Specialty Coffee Roasters ===")

        bean_name = input("Tipo de grano (Geisha, Bourbon Rosado, Caturra): ").strip()

        try:
            grams = int(input("Cantidad en gramos: "))
        except ValueError:
            print("La cantidad debe ser un número entero.")
            return

        preparation_method = input("Método de preparación (V60, Chemex, Prensa, etc.): ").strip()

        coffee_bean = CoffeeBean(bean_name)
        order = Order(coffee_bean, grams, preparation_method)

        try:
            result = self.process_order_use_case.execute(order)
            print("\nPedido procesado correctamente.")
            print(f"Estado del pedido: {result.status}")
        except InsufficientInventoryError as error:
            print(f"\nPedido rechazado: {error}")

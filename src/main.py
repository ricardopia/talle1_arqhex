from src.adapters.secondary.in_memory_inventory import InMemoryInventoryAdapter
from src.adapters.secondary.in_memory_order import InMemoryOrderAdapter
from src.application.process_coffee_order import ProcessCoffeeOrderUseCase
from src.adapters.primary.coffee_order_cli import CoffeeOrderCLI


def main():
    # 1. Se crean los adaptadores concretos.
    inventory_adapter = InMemoryInventoryAdapter()
    order_adapter = InMemoryOrderAdapter()

    # 2. Se inyectan en el caso de uso mediante los puertos.
    process_order_use_case = ProcessCoffeeOrderUseCase(
        inventory_adapter,
        order_adapter,
    )

    # 3. Se conecta el adaptador primario al caso de uso.
    cli = CoffeeOrderCLI(process_order_use_case)
    cli.run()


if __name__ == "__main__":
    main()

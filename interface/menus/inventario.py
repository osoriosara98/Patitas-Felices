"""
Menú de inventario de medicamentos
"""

from utils.consola import PROMPT_SELECCIONE_OPCION, MSG_OPCION_INVALIDA
from servicios.inventario_medicamentos import (
    registrar_medicamento, actualizar_stock, mostrar_inventario, verificar_alertas_inventario
)

def submenu_inventario():
    """Menú de inventario de medicamentos"""
    while True:
        print("\n=== Inventario de Medicamentos ===")
        print("1. Registrar medicamento")
        print("2. Actualizar stock")
        print("3. Ver inventario")
        print("4. Verificar alertas")
        print("0. Volver al menú principal")
        opcion = input(PROMPT_SELECCIONE_OPCION)
        
        if opcion == "1":
            registrar_medicamento()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            verificar_alertas_inventario()
        elif opcion == "0":
            break
        else:
            print(MSG_OPCION_INVALIDA)

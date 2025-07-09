"""
Menú de historia clínica
"""

from utils.consola import MENU_VOLVER_PRINCIPAL, PROMPT_SELECCIONE_OPCION, MSG_OPCION_INVALIDA
from servicios.historia_clinica import crear_historia_clinica, consultar_historial_paciente

def submenu_historia_clinica():
    """Menú de historia clínica"""
    while True:
        print("\n=== Historia Clínica ===")
        print("1. Crear historia clínica")
        print("2. Consultar historial de paciente")
        print(MENU_VOLVER_PRINCIPAL)
        opcion = input(PROMPT_SELECCIONE_OPCION)
        
        if opcion == "1":
            crear_historia_clinica()
        elif opcion == "2":
            consultar_historial_paciente()
        elif opcion == "0":
            break
        else:
            print(MSG_OPCION_INVALIDA)

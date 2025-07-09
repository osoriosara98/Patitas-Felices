"""
Menú inicial y gestión de carga de datos
"""

from utils.consola import (
    mostrar_titulo, mostrar_mensaje_exito, mostrar_mensaje_info,
    solicitar_numero, MSG_ENTRADA_NO_VALIDA
)
from data.backup_utils import cargar_backup_interactivo

def mostrar_menu_inicial():
    """Muestra menú inicial para elegir modo de inicio"""
    mostrar_titulo("Bienvenido al Sistema de Gestión Veterinaria Patitas Felices")
    
    print("\n🚀 ¿CÓMO DESEA INICIAR EL SISTEMA?")
    print("="*50)
    print("1. 📁 Cargar backup de días anteriores")
    print("2. 📊 Cargar datos de prueba (demostración)")
    print("3. 🆕 Iniciar con sistema vacío")
    print("="*50)
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            
            if opcion == 1:
                return cargar_backup_interactivo()
            elif opcion == 2:
                from datos_prueba import cargar_datos_prueba
                cargar_datos_prueba()
                return True
            elif opcion == 3:
                mostrar_mensaje_exito("Iniciando con sistema vacío.")
                return False
            else:
                print("⚠️ Opción inválida. Seleccione 1, 2 o 3.")
        except ValueError:
            print(MSG_ENTRADA_NO_VALIDA)

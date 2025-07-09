"""
Sistema de Gestión Veterinaria - Patitas Felices
Punto de entrada principal del sistema
"""

from utils.consola import mostrar_mensaje_info, mostrar_mensaje_exito
from data.backup_utils import limpiar_backups_automaticos
from interface.menus.inicio import mostrar_menu_inicial
from interface.menu_principal import menu

def main():
    """Función principal del sistema"""
    # Limpiar backups automáticos obsoletos al inicio
    print("🧹 Limpiando backups automáticos obsoletos...")
    limpiar_backups_automaticos()
    
    # Mostrar menú inicial para elegir modo de inicio
    datos_cargados = mostrar_menu_inicial()
    
    if datos_cargados:
        print("\n🎯 ¡Sistema listo para continuar trabajando!")
        mostrar_mensaje_info("Sus datos están cargados y listos para usar.")
    else:
        print("\n🆕 Sistema iniciado vacío.")
        mostrar_mensaje_info("Puede comenzar registrando propietarios y pacientes.")
        mostrar_mensaje_info("Sus datos se guardarán automáticamente en un archivo de sesión.")
    
    # Ejecutar el menú principal
    menu()

if __name__ == "__main__":
    main()

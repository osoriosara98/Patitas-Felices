"""
Menú principal del sistema veterinario
"""

from utils.consola import (
    mostrar_titulo, mostrar_seccion, pausa_para_continuar,
    PROMPT_SELECCIONE_OPCION, MSG_OPCION_INVALIDA
)
from data.backup_utils import crear_backup_manual, guardar_al_salir
from data.db import propietarios, pacientes

from servicios.registro_propietario import registrar_propietario
from servicios.registro_paciente import registrar_paciente, ver_mascotas_por_propietario
from servicios.editar_datos import menu_editar_datos
from servicios.informes import generar_informe_mensual
from servicios.inventario_medicamentos import verificar_alertas_inventario

from interface.menus.citas import submenu_citas
from interface.menus.historia import submenu_historia_clinica
from interface.menus.inventario import submenu_inventario
from interface.menus.utilidades import submenu_utilidades

def mostrar_propietarios():
    """Mostrar lista de propietarios"""
    print("\n--- Lista de Propietarios ---")
    if not propietarios:
        print("📭 No hay propietarios registrados.")
    else:
        for p in propietarios.values():
            print(p)
    pausa_para_continuar()

def mostrar_pacientes():
    """Mostrar lista de pacientes"""
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("📭 No hay pacientes registrados.")
    else:
        for p in pacientes.values():
            print(p)
    pausa_para_continuar()

def handle_menu_option(opcion):
    """Maneja las opciones del menú principal"""
    if opcion == "1":
        registrar_propietario()
    elif opcion == "2":
        registrar_paciente()
    elif opcion == "3":
        mostrar_propietarios()
    elif opcion == "4":
        mostrar_pacientes()
    elif opcion == "5":
        ver_mascotas_por_propietario()
    elif opcion == "6":
        submenu_citas()
    elif opcion == "7":
        submenu_historia_clinica()
    elif opcion == "8":
        submenu_inventario()
    elif opcion == "9":
        menu_editar_datos()
    elif opcion == "10":
        generar_informe_mensual()
    elif opcion == "11":
        submenu_utilidades()
    elif opcion == "12":
        crear_backup_manual()
    elif opcion == "13":
        verificar_alertas_inventario()
    elif opcion == "0":
        guardar_al_salir()
        print("Hasta luego 🐾")
        print("¡Gracias por usar el Sistema de Gestión Veterinaria Patitas Felices!")
        return False
    else:
        print(MSG_OPCION_INVALIDA)
    return True

def menu():
    """Menú principal del sistema"""
    while True:
        mostrar_titulo("SISTEMA DE GESTIÓN VETERINARIA - PATITAS FELICES")
        
        mostrar_seccion("📋 GESTIÓN BÁSICA")
        print("1.  Registrar propietario")
        print("2.  Registrar paciente")
        print("3.  Ver propietarios")
        print("4.  Ver pacientes")
        print("5.  Ver mascotas de un propietario")
        
        mostrar_seccion("📅 GESTIÓN DE CITAS")
        print("6.  Menú de citas")
        
        mostrar_seccion("📋 HISTORIA CLÍNICA")
        print("7.  Menú de historia clínica")
        
        mostrar_seccion("💊 INVENTARIO")
        print("8.  Menú de inventario")
        
        mostrar_seccion("✏️ EDICIÓN")
        print("9.  Editar datos")
        
        mostrar_seccion("📊 REPORTES")
        print("10. Generar informe mensual")
        
        mostrar_seccion("🔧 UTILIDADES")
        print("11. Utilidades y reportes avanzados")
        
        mostrar_seccion("💾 BACKUP")
        print("12. Crear backup de datos")
        
        mostrar_seccion("⚠️ ALERTAS")
        print("13. Verificar alertas de inventario")
        
        print("\n0.  Salir")
        print("="*60)
        
        opcion = input(PROMPT_SELECCIONE_OPCION)

        if not handle_menu_option(opcion):
            break

"""
Menú de gestión de citas
"""

from utils.consola import (
    mostrar_seccion, MENU_VOLVER_PRINCIPAL, PROMPT_SELECCIONE_OPCION, MSG_OPCION_INVALIDA
)
from utils.seleccion import seleccionar_paciente, seleccionar_veterinario
from servicios.gestion_citas import ver_citas, cancelar_cita, buscar_citas_por_fecha
from servicios.historia_clinica import registrar_atencion_medica
from data.db import propietarios

def submenu_citas():
    """Menú de gestión de citas"""
    while True:
        print("\n=== Gestión de Citas ===")
        print("1. Registrar nueva cita")
        print("2. Ver todas las citas")
        print("3. Cancelar cita")
        print("4. Buscar citas por fecha")
        print("5. Registrar atención médica")
        print(MENU_VOLVER_PRINCIPAL)
        opcion = input(PROMPT_SELECCIONE_OPCION)
        
        if opcion == "1":
            agendar_cita_mejorada()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            cancelar_cita()
        elif opcion == "4":
            buscar_citas_por_fecha()
        elif opcion == "5":
            registrar_atencion_medica()
        elif opcion == "0":
            break
        else:
            print(MSG_OPCION_INVALIDA)

def agendar_cita_mejorada():
    """Agendar una nueva cita médica"""
    print("\n--- Agendar Cita Médica ---")
    id_propietario = input("Ingrese el ID del propietario: ")
    
    if id_propietario not in propietarios:
        print("Propietario no encontrado. Por favor regístrelo primero.")
        from servicios.registro_propietario import registrar_propietario
        from servicios.registro_paciente import registrar_paciente
        registrar_propietario()
        registrar_paciente()
        return
    
    paciente_seleccionado = seleccionar_paciente(id_propietario)
    if paciente_seleccionado is None:
        return
    
    # Validar fecha
    while True:
        fecha = input("Fecha (YYYY-MM-DD): ")
        from servicios.registro_cita import validar_fecha
        if validar_fecha(fecha):
            break
    
    # Validar hora
    while True:
        hora = input("Hora (HH:MM): ")
        from servicios.registro_cita import validar_hora
        if validar_hora(hora):
            break
    
    motivo = input("Motivo: ")
    id_veterinario = seleccionar_veterinario()
    if id_veterinario is None:
        return
    
    # Registrar la cita con validación
    from servicios.registro_cita import registrar_cita
    if registrar_cita(fecha, hora, motivo, paciente_seleccionado.id, id_veterinario):
        print("🎉 ¡Cita agendada correctamente!")
    else:
        print("❌ Error al agendar la cita.")

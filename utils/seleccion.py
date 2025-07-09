"""
Utilidades para selección de entidades (pacientes, veterinarios, etc.)
"""

from data.db import pacientes, propietarios
from utils.consola import MSG_ENTRADA_NO_VALIDA, mostrar_mensaje_error

def seleccionar_paciente(id_propietario):
    """Permite seleccionar un paciente de un propietario"""
    from servicios.registro_paciente import registrar_paciente
    
    mascotas = [p for p in pacientes.values() if p.id_propietario == id_propietario]
    
    if not mascotas:
        print("Este propietario no tiene pacientes registrados. Registremos uno.")
        registrar_paciente()
        mascotas = [p for p in pacientes.values() if p.id_propietario == id_propietario]
    
    if len(mascotas) == 1:
        return mascotas[0]
    
    print("¿Para cuál paciente es la cita?")
    for idx, m in enumerate(mascotas, 1):
        print(f"{idx}. {m.nombre}")
    
    while True:
        try:
            seleccion = int(input("Seleccione el número correspondiente: "))
            if 1 <= seleccion <= len(mascotas):
                return mascotas[seleccion - 1]
            else:
                print("⚠️ Selección fuera de rango. Intente de nuevo.")
        except ValueError:
            print(MSG_ENTRADA_NO_VALIDA)

def seleccionar_veterinario():
    """Permite seleccionar un veterinario disponible"""
    veterinarios = cargar_veterinarios()
    
    if not veterinarios:
        mostrar_mensaje_error("No hay veterinarios disponibles.")
        return None
    
    print("Veterinarios disponibles:")
    for idx, vet in enumerate(veterinarios, 1):
        print(f"{idx}. {vet['nombre']} (ID: {vet['id']})")
    
    while True:
        try:
            seleccion_vet = int(input("Seleccione el número correspondiente al veterinario: "))
            if 1 <= seleccion_vet <= len(veterinarios):
                return veterinarios[seleccion_vet - 1]["id"]
            else:
                print("⚠️ Selección fuera de rango. Intente de nuevo.")
        except ValueError:
            print("⚠️ Entrada no válida. Ingrese un número.")

def cargar_veterinarios():
    """Carga la lista de veterinarios desde archivo"""
    try:
        with open("data/veterinarios.txt", "r", encoding="utf-8") as file:
            veterinarios = []
            for linea in file:
                partes = linea.strip().split(",")
                if len(partes) >= 2:
                    veterinarios.append({"id": partes[0], "nombre": partes[1]})
            return veterinarios
    except FileNotFoundError:
        print("⚠️ Archivo de veterinarios no encontrado.")
        return []

def seleccionar_opcion_menu(opciones_validas):
    """Selecciona una opción válida del menú"""
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in opciones_validas:
            return opcion
        print("❌ Opción inválida. Intente de nuevo.")

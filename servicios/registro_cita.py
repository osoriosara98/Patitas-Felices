from modelos.cita import Cita
from data.db import citas_registradas
import random
from datetime import datetime

def auto_guardar_datos():
    """Guarda automáticamente los datos de la sesión actual"""
    try:
        from data.db import guardar_sesion_actual
        
        archivo_guardado = guardar_sesion_actual()
        if archivo_guardado:
            nombre_archivo = archivo_guardado.split('\\')[-1] if '\\' in archivo_guardado else archivo_guardado.split('/')[-1]
            print(f"💾 Sesión actualizada: {nombre_archivo}")
        
    except Exception as e:
        print(f"⚠️ Error al actualizar sesión: {e}")

#llamo los vets disponibles

def cargar_veterinarios():
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

#genero aleatoriamente un id para la cita [un radicado]
def generar_id_unico_cita():
    while True:
        nuevo_id = str(random.randint(1000, 9999))
        if not any(cita.id == nuevo_id for cita in citas_registradas):
            return nuevo_id

def validar_fecha(fecha_str):
    """Valida que la fecha esté en formato YYYY-MM-DD y sea válida"""
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        fecha_hoy = datetime.now().date()
        if fecha.date() < fecha_hoy:
            print("⚠️ La fecha no puede ser anterior a hoy.")
            return False
        return True
    except ValueError:
        print("⚠️ Formato de fecha inválido. Use YYYY-MM-DD")
        return False

def validar_hora(hora_str):
    """Valida que la hora esté en formato HH:MM"""
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        print("⚠️ Formato de hora inválido. Use HH:MM")
        return False

def registrar_cita(fecha, hora, motivo, id_paciente, id_veterinario):
    # Validar fecha y hora
    if not validar_fecha(fecha):
        return False
    if not validar_hora(hora):
        return False
        
    cita_id = generar_id_unico_cita()
    nueva_cita = Cita(cita_id, fecha, hora, motivo, id_paciente, id_veterinario)
    citas_registradas.append(nueva_cita)
    print(f"✅ Cita registrada exitosamente con ID: {cita_id}")
    print(f"📅 Fecha: {fecha} - Hora: {hora}")
    
    # Auto-guardar datos
    auto_guardar_datos()
    return True



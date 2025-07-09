# Base de datos en memoria mejorada para el Sistema Veterinario Patitas Felices
from datetime import datetime
import json
import os

# Diccionarios que actúan como "base de datos en memoria"
propietarios = {}
pacientes = {}
citas_registradas = []
medicamentos = {}
historias_clinicas = []

# Configuración de persistencia
DATA_DIR = "data"
BACKUP_DIR = os.path.join(DATA_DIR, "backups")

# Variables globales para control de backup de sesión
BACKUP_SESION_ACTUAL = None
FECHA_SESION_ACTUAL = None

def crear_directorios():
    """Crear directorios necesarios si no existen"""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

def obtener_estadisticas():
    """Obtener estadísticas generales del sistema"""
    stats = {
        "propietarios": len(propietarios),
        "pacientes": len(pacientes),
        "citas_total": len(citas_registradas),
        "citas_agendadas": len([c for c in citas_registradas if c.estado == "agendada"]),
        "citas_realizadas": len([c for c in citas_registradas if c.estado == "realizada"]),
        "citas_canceladas": len([c for c in citas_registradas if c.estado == "cancelada"]),
        "medicamentos": len(medicamentos),
        "stock_bajo": len([m for m in medicamentos.values() if int(m.stock) <= 10]),
        "historias_clinicas": len(historias_clinicas),
        "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return stats

def validar_integridad_datos():
    """Validar la integridad de los datos en memoria"""
    errores = []
    
    # Verificar que todos los pacientes tengan propietarios válidos
    for paciente in pacientes.values():
        if paciente.id_propietario not in propietarios:
            errores.append(f"Paciente {paciente.nombre} (ID: {paciente.id}) tiene propietario inválido: {paciente.id_propietario}")
    
    # Verificar que las citas tengan pacientes válidos
    for cita in citas_registradas:
        if cita.id_paciente not in pacientes:
            errores.append(f"Cita {cita.id} tiene paciente inválido: {cita.id_paciente}")
    
    # Verificar que las historias clínicas tengan pacientes válidos
    for historia in historias_clinicas:
        if historia.id_paciente not in pacientes:
            errores.append(f"Historia clínica {historia.id} tiene paciente inválido: {historia.id_paciente}")
    
    return errores

def limpiar_datos():
    """Limpiar todos los datos en memoria"""
    propietarios.clear()
    pacientes.clear()
    citas_registradas.clear()
    medicamentos.clear()
    historias_clinicas.clear()
    print("🗑️ Datos limpiados correctamente")

def exportar_datos_json(archivo="backup_datos.json"):
    """Exportar todos los datos a un archivo JSON"""
    try:
        crear_directorios()
        datos = {
            "propietarios": {id: {
                "id": prop.id,
                "nombre": prop.nombre,
                "telefono": prop.telefono,
                "correo": prop.correo,
                "direccion": prop.direccion,
                "mascotas": prop.mascotas
            } for id, prop in propietarios.items()},
            
            "pacientes": {id: {
                "id": pac.id,
                "nombre": pac.nombre,
                "edad": pac.edad,
                "especie": pac.especie,
                "raza": pac.raza,
                "peso": pac.peso,
                "sexo": pac.sexo,
                "id_propietario": pac.id_propietario
            } for id, pac in pacientes.items()},
            
            "citas": [{
                "id": cita.id,
                "fecha": cita.fecha,
                "hora": cita.hora,
                "motivo": cita.motivo,
                "id_paciente": cita.id_paciente,
                "id_veterinario": cita.id_veterinario,
                "estado": cita.estado
            } for cita in citas_registradas],
            
            "medicamentos": {id: {
                "id": med.id,
                "nombre": med.nombre,
                "descripcion": med.descripcion,
                "stock": med.stock,
                "fecha_vencimiento": med.fecha_vencimiento,
                "precio": med.precio
            } for id, med in medicamentos.items()},
            
            "historias_clinicas": [{
                "id": hist.id,
                "id_paciente": hist.id_paciente,
                "diagnostico": hist.diagnostico,
                "tratamiento": hist.tratamiento,
                "vacunas": hist.vacunas,
                "observaciones": hist.observaciones,
                "fecha": hist.fecha_actualizacion
            } for hist in historias_clinicas],
            
            "metadata": {
                "fecha_exportacion": datetime.now().isoformat(),
                "version": "1.0",
                "estadisticas": obtener_estadisticas()
            }
        }
        
        archivo_path = os.path.join(BACKUP_DIR, archivo)
        with open(archivo_path, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Datos exportados exitosamente a: {archivo_path}")
        return archivo_path
    
    except Exception as e:
        print(f"❌ Error al exportar datos: {e}")
        return None

def mostrar_resumen_sistema():
    """Mostrar un resumen completo del estado del sistema"""
    stats = obtener_estadisticas()
    errores = validar_integridad_datos()
    
    print("\n" + "="*50)
    print("📊 RESUMEN DEL SISTEMA")
    print("="*50)
    print(f"👥 Propietarios: {stats['propietarios']}")
    print(f"🐾 Pacientes: {stats['pacientes']}")
    print("📅 Citas:")
    print(f"   • Total: {stats['citas_total']}")
    print(f"   • Agendadas: {stats['citas_agendadas']}")
    print(f"   • Realizadas: {stats['citas_realizadas']}")
    print(f"   • Canceladas: {stats['citas_canceladas']}")
    print("💊 Inventario:")
    print(f"   • Medicamentos: {stats['medicamentos']}")
    print(f"   • Stock bajo: {stats['stock_bajo']}")
    print(f"📋 Historias clínicas: {stats['historias_clinicas']}")
    print(f"🕒 Última actualización: {stats['ultima_actualizacion']}")
    
    if errores:
        print("\n⚠️ ERRORES DE INTEGRIDAD:")
        for error in errores:
            print(f"   • {error}")
    else:
        print("\n✅ Integridad de datos: OK")
    
    print("="*50)

def obtener_nombre_backup_sesion():
    """Obtiene el nombre del backup de la sesión actual"""
    global BACKUP_SESION_ACTUAL, FECHA_SESION_ACTUAL
    
    fecha_hoy = datetime.now().strftime("%Y%m%d")
    
    # Si es un nuevo día o primera vez, crear nuevo nombre
    if FECHA_SESION_ACTUAL != fecha_hoy or BACKUP_SESION_ACTUAL is None:
        FECHA_SESION_ACTUAL = fecha_hoy
        hora_inicio = datetime.now().strftime("%H%M")
        BACKUP_SESION_ACTUAL = f"sesion_{fecha_hoy}_{hora_inicio}.json"
    
    return BACKUP_SESION_ACTUAL

def guardar_sesion_actual():
    """Guarda o actualiza el backup de la sesión actual"""
    try:
        crear_directorios()
        
        # Verificar si hay datos para guardar
        if not propietarios and not pacientes and not citas_registradas:
            return None
        
        nombre_backup = obtener_nombre_backup_sesion()
        
        datos = {
            "propietarios": {id: {
                "id": prop.id,
                "nombre": prop.nombre,
                "telefono": prop.telefono,
                "correo": prop.correo,
                "direccion": prop.direccion,
                "mascotas": prop.mascotas
            } for id, prop in propietarios.items()},
            
            "pacientes": {id: {
                "id": pac.id,
                "nombre": pac.nombre,
                "edad": pac.edad,
                "especie": pac.especie,
                "raza": pac.raza,
                "peso": pac.peso,
                "sexo": pac.sexo,
                "id_propietario": pac.id_propietario
            } for id, pac in pacientes.items()},
            
            "citas_registradas": [{
                "id": cita.id,
                "fecha": cita.fecha,
                "hora": cita.hora,
                "motivo": cita.motivo,
                "id_paciente": cita.id_paciente,
                "id_veterinario": cita.id_veterinario,
                "estado": cita.estado
            } for cita in citas_registradas],
            
            "medicamentos": {id: {
                "id": med.id,
                "nombre": med.nombre,
                "descripcion": med.descripcion,
                "stock": med.stock,
                "fecha_vencimiento": med.fecha_vencimiento,
                "precio": med.precio
            } for id, med in medicamentos.items()},
            
            "historias_clinicas": [{
                "id": hist.id,
                "id_paciente": hist.id_paciente,
                "diagnostico": hist.diagnostico,
                "tratamiento": hist.tratamiento,
                "vacunas": hist.vacunas,
                "observaciones": hist.observaciones,
                "fecha": hist.fecha_actualizacion
            } for hist in historias_clinicas],
            
            "metadata": {
                "fecha_exportacion": datetime.now().isoformat(),
                "version": "1.0",
                "tipo": "sesion_activa",
                "estadisticas": obtener_estadisticas()
            }
        }
        
        archivo_path = os.path.join(BACKUP_DIR, nombre_backup)
        with open(archivo_path, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        
        return archivo_path
    
    except Exception as e:
        print(f"❌ Error al guardar sesión: {e}")
        return None

def limpiar_backups_sesion_antiguos():
    """Limpia backups de sesión antiguos (más de 7 días)"""
    try:
        if not os.path.exists(BACKUP_DIR):
            return
            
        fecha_limite = datetime.now().timestamp() - (7 * 24 * 60 * 60)  # 7 días
        
        for archivo in os.listdir(BACKUP_DIR):
            if archivo.startswith('sesion_') and archivo.endswith('.json'):
                ruta_completa = os.path.join(BACKUP_DIR, archivo)
                if os.path.getmtime(ruta_completa) < fecha_limite:
                    try:
                        os.remove(ruta_completa)
                        print(f"🗑️ Backup de sesión antiguo eliminado: {archivo}")
                    except Exception as e:
                        print(f"⚠️ Error al eliminar {archivo}: {e}")
                        
    except Exception as e:
        print(f"⚠️ Error al limpiar backups de sesión: {e}")

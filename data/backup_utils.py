"""
Utilidades para manejo de backups y carga de datos
"""

import json
import os
from datetime import datetime
from utils.consola import (
    mostrar_mensaje_exito, mostrar_mensaje_error, mostrar_mensaje_info,
    MSG_ENTRADA_NO_VALIDA, pausa_para_continuar
)

JSON_EXTENSION = '.json'

def limpiar_backups_automaticos():
    """Limpia backups automáticos antiguos (mantiene backups de sesión y manuales)"""
    try:
        backup_dir = "data/backups"
        if not os.path.exists(backup_dir):
            return
            
        # Solo eliminar backups automáticos viejos, no los de sesión ni manuales
        auto_backups = []
        for archivo in os.listdir(backup_dir):
            if archivo.startswith('auto_backup_') and archivo.endswith('.json'):
                ruta_completa = os.path.join(backup_dir, archivo)
                fecha_mod = os.path.getmtime(ruta_completa)
                auto_backups.append((archivo, ruta_completa, fecha_mod))
        
        # Ordenar por fecha (más reciente primero)
        auto_backups.sort(key=lambda x: x[2], reverse=True)
        
        # Eliminar todos los backups automáticos antiguos (ya no los necesitamos)
        for archivo, ruta, _ in auto_backups:
            try:
                os.remove(ruta)
                print(f"🗑️ Backup automático obsoleto eliminado: {archivo}")
            except Exception as e:
                print(f"⚠️ Error al eliminar {archivo}: {e}")
        
        # Limpiar backups de sesión antiguos (más de 7 días)
        from data.db import limpiar_backups_sesion_antiguos
        limpiar_backups_sesion_antiguos()
                    
    except Exception as e:
        print(f"⚠️ Error al limpiar backups automáticos: {e}")

def listar_backups_disponibles():
    """Lista todos los backups disponibles (incluyendo sesiones)"""
    backup_dir = "data/backups"
    if not os.path.exists(backup_dir):
        return []
    
    backups = []
    for archivo in os.listdir(backup_dir):
        if archivo.endswith(JSON_EXTENSION):
            ruta_completa = os.path.join(backup_dir, archivo)
            fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_completa))
            
            # Determinar tipo de backup
            if archivo.startswith('sesion_'):
                tipo = "🔄 Sesión"
            elif archivo.startswith('backup_manual_'):
                tipo = "📋 Manual"
            elif archivo.startswith('auto_backup_'):
                tipo = "⚡ Auto"
            else:
                tipo = "📁 Backup"
                
            backups.append({
                'archivo': archivo,
                'ruta': ruta_completa,
                'fecha': fecha_mod,
                'tipo': tipo
            })
    
    # Ordenar por fecha (más reciente primero)
    backups.sort(key=lambda x: x['fecha'], reverse=True)
    return backups

def cargar_backup_interactivo():
    """Permite al usuario seleccionar y cargar un backup"""
    backups = listar_backups_disponibles()
    
    if not backups:
        mostrar_mensaje_error("No hay backups disponibles.")
        respuesta = input("¿Desea cargar datos de prueba en su lugar? (s/n): ")
        if respuesta.lower() == 's':
            from datos_prueba import cargar_datos_prueba
            cargar_datos_prueba()
            return True
        return False
    
    print("\n📁 BACKUPS DISPONIBLES:")
    print("="*50)
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup['tipo']} {backup['archivo']}")
        print(f"   📅 Fecha: {backup['fecha'].strftime('%Y-%m-%d %H:%M:%S')}")
        print()
    
    print("0. No cargar backup (sistema vacío)")
    print("99. Cargar datos de prueba")
    
    while True:
        try:
            seleccion = int(input("Seleccione el backup a cargar: "))
            
            if seleccion == 0:
                mostrar_mensaje_exito("Iniciando con sistema vacío.")
                return False
            elif seleccion == 99:
                from datos_prueba import cargar_datos_prueba
                cargar_datos_prueba()
                return True
            elif 1 <= seleccion <= len(backups):
                backup_seleccionado = backups[seleccion - 1]
                return cargar_backup_desde_archivo(backup_seleccionado['ruta'])
            else:
                print("⚠️ Selección fuera de rango.")
        except ValueError:
            print(MSG_ENTRADA_NO_VALIDA)

def cargar_backup_desde_archivo(ruta_backup):
    """Carga datos desde un archivo de backup específico"""
    try:
        print(f"🔄 Cargando backup: {os.path.basename(ruta_backup)}")
        
        with open(ruta_backup, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        
        # Importar las clases necesarias
        from modelos.propietario import Propietario
        from modelos.paciente import Paciente
        from modelos.cita import Cita
        from modelos.medicamento import Medicamento
        from modelos.historia_clinica import HistoriaClinica
        from data.db import propietarios, pacientes, citas_registradas, medicamentos, historias_clinicas
        
        # Limpiar datos actuales
        propietarios.clear()
        pacientes.clear()
        citas_registradas.clear()
        medicamentos.clear()
        historias_clinicas.clear()
        
        # Determinar estructura del backup (nueva vs antigua)
        if 'datos' in backup_data:
            # Estructura nueva con 'datos' wrapper
            datos = backup_data['datos']
            metadatos = backup_data.get('metadatos', {})
        else:
            # Estructura antigua - datos directamente en la raíz
            datos = backup_data
            metadatos = backup_data.get('metadata', {})
        
        # Cargar propietarios
        for prop_id, prop_data in datos['propietarios'].items():
            prop = Propietario(
                prop_data['id'],
                prop_data['nombre'],
                prop_data['telefono'],
                prop_data['correo'],
                prop_data['direccion']
            )
            prop.mascotas = prop_data['mascotas']
            propietarios[prop_id] = prop
        
        # Cargar pacientes
        for pac_id, pac_data in datos['pacientes'].items():
            pac = Paciente(
                pac_data['id'],
                pac_data['nombre'],
                pac_data['edad'],
                pac_data['especie'],
                pac_data['raza'],
                pac_data['peso'],
                pac_data['sexo'],
                pac_data['id_propietario']
            )
            pacientes[pac_id] = pac
        
        # Cargar citas (puede estar como 'citas' o 'citas_registradas')
        citas_data = datos.get('citas', datos.get('citas_registradas', []))
        for cita_data in citas_data:
            cita = Cita(
                cita_data['id'],
                cita_data['fecha'],
                cita_data['hora'],
                cita_data['motivo'],
                cita_data['id_paciente'],
                cita_data['id_veterinario'],
                cita_data['estado']
            )
            citas_registradas.append(cita)
        
        # Cargar medicamentos
        for med_id, med_data in datos['medicamentos'].items():
            med = Medicamento(
                med_data['id'],
                med_data['nombre'],
                med_data['descripcion'],
                med_data['stock'],  # Mantener como número
                med_data['fecha_vencimiento'],
                med_data['precio']
            )
            medicamentos[med_id] = med
        
        # Cargar historias clínicas
        for hist_data in datos['historias_clinicas']:
            hist = HistoriaClinica(
                hist_data['id'],
                hist_data['id_paciente'],
                hist_data['diagnostico'],
                hist_data['tratamiento'],
                hist_data['vacunas'],
                hist_data['observaciones']
            )
            # Agregar fecha si existe
            if 'fecha' in hist_data:
                hist.fecha = hist_data['fecha']
            historias_clinicas.append(hist)
        
        mostrar_mensaje_exito("Backup cargado exitosamente!")
        print("📊 Datos restaurados:")
        print(f"   • {len(propietarios)} propietarios")
        print(f"   • {len(pacientes)} pacientes") 
        print(f"   • {len(citas_registradas)} citas")
        print(f"   • {len(medicamentos)} medicamentos")
        print(f"   • {len(historias_clinicas)} historias clínicas")
        
        # Mostrar fecha del backup si está disponible
        fecha_backup = metadatos.get('fecha_exportacion') or metadatos.get('fecha_creacion', 'No disponible')
        print(f"📅 Backup del: {fecha_backup}")
        
        return True
        
    except Exception as e:
        mostrar_mensaje_error(f"Error al cargar backup: {e}")
        print(f"🔍 Detalles del error: {type(e).__name__}")
        return False

def crear_backup_manual():
    """Permite crear un backup manual con nombre personalizado"""
    from data.db import exportar_datos_json
    
    print("\n💾 --- Crear Backup Manual ---")
    
    # Sugerir nombre por defecto
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_sugerido = f"backup_manual_{fecha_actual}.json"
    
    print(f"📝 Nombre sugerido: {nombre_sugerido}")
    nombre = input("Ingrese nombre del backup (Enter para usar sugerido): ").strip()
    
    if not nombre:
        nombre = nombre_sugerido
    if not nombre.endswith(JSON_EXTENSION):
        nombre += JSON_EXTENSION
    
    try:
        exportar_datos_json(nombre)
        mostrar_mensaje_exito(f"Backup creado exitosamente: {nombre}")
        mostrar_mensaje_info("Puede cargar este backup la próxima vez usando la opción 1 del menú inicial.")
    except Exception as e:
        mostrar_mensaje_error(f"Error al crear backup: {e}")

def guardar_al_salir():
    """Pregunta si desea guardar los datos al salir"""
    from data.db import obtener_estadisticas, guardar_sesion_actual
    stats = obtener_estadisticas()
    
    # Solo ofrecer guardar si hay datos
    if stats['propietarios'] > 0 or stats['pacientes'] > 0 or stats['citas_total'] > 0:
        print("\n💾 ¿Desea crear un backup manual adicional antes de salir?")
        print(f"📊 Datos actuales: {stats['propietarios']} propietarios, {stats['pacientes']} pacientes, {stats['citas_total']} citas")
        mostrar_mensaje_info("Sus datos ya están guardados automáticamente en el archivo de sesión.")
        
        respuesta = input("Crear backup manual adicional (s/n): ").lower()
        if respuesta == 's':
            crear_backup_manual()
            mostrar_mensaje_exito("Backup manual creado exitosamente.")
        else:
            # Asegurar que la sesión esté guardada
            archivo_sesion = guardar_sesion_actual()
            if archivo_sesion:
                nombre = archivo_sesion.split('\\')[-1] if '\\' in archivo_sesion else archivo_sesion.split('/')[-1]
                mostrar_mensaje_exito(f"Datos guardados en sesión: {nombre}")
    else:
        mostrar_mensaje_info("No hay datos que guardar.")

"""
Utilidades para el manejo y gestión de datos del sistema veterinario
"""

from data.db import (
    propietarios, pacientes, citas_registradas, medicamentos, historias_clinicas,
    obtener_estadisticas 
)
from datetime import datetime, timedelta
import random

def generar_id_unico(tipo="general", longitud=5):
    """Generar un ID único para diferentes tipos de entidades"""
    prefijos = {
        "propietario": "1",
        "paciente": "10",
        "cita": "20",
        "medicamento": "30",
        "historia": "40"
    }
    
    prefijo = prefijos.get(tipo, "")
    while True:
        numero = random.randint(10**(longitud-1), 10**longitud - 1)
        nuevo_id = f"{prefijo}{numero}"
        
        # Verificar que no exista
        if tipo == "propietario" and nuevo_id not in propietarios:
            return nuevo_id
        elif tipo == "paciente" and nuevo_id not in pacientes:
            return nuevo_id
        elif tipo == "cita" and not any(c.id == nuevo_id for c in citas_registradas):
            return nuevo_id
        elif tipo == "medicamento" and nuevo_id not in medicamentos:
            return nuevo_id
        elif tipo == "historia" and not any(h.id == nuevo_id for h in historias_clinicas):
            return nuevo_id
        elif tipo == "general":
            return str(numero)

def buscar_por_criterio(entidad, campo, valor):
    """Buscar entidades por un criterio específico"""
    def filtrar_entidades(coleccion):
        return [
            obj for obj in coleccion
            if hasattr(obj, campo) and valor.lower() in str(getattr(obj, campo)).lower()
        ]

    entidades_map = {
        "propietarios": propietarios.values(),
        "pacientes": pacientes.values(),
        "citas": citas_registradas,
        "medicamentos": medicamentos.values()
    }

    coleccion = entidades_map.get(entidad)
    if coleccion is None:
        return []

    return filtrar_entidades(coleccion)

def obtener_citas_por_fecha(fecha_inicio, fecha_fin=None):
    """Obtener citas en un rango de fechas"""
    if fecha_fin is None:
        fecha_fin = fecha_inicio
    
    citas_filtradas = []
    for cita in citas_registradas:
        if fecha_inicio <= cita.fecha <= fecha_fin:
            citas_filtradas.append(cita)
    
    return sorted(citas_filtradas, key=lambda x: (x.fecha, x.hora))

def obtener_medicamentos_por_vencer(dias=30):
    """Obtener medicamentos que vencen en los próximos N días"""
    fecha_limite = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")
    medicamentos_por_vencer = []
    
    for med in medicamentos.values():
        if med.fecha_vencimiento <= fecha_limite:
            medicamentos_por_vencer.append(med)
    
    return sorted(medicamentos_por_vencer, key=lambda x: x.fecha_vencimiento)

def obtener_historias_paciente(id_paciente):
    """Obtener todas las historias clínicas de un paciente"""
    historias_paciente = [h for h in historias_clinicas if h.id_paciente == id_paciente]
    return sorted(historias_paciente, key=lambda x: x.fecha_actualizacion, reverse=True)

def calcular_edad_promedio_pacientes():
    """Calcular la edad promedio de los pacientes"""
    if not pacientes:
        return 0
    
    edades = [int(p.edad) for p in pacientes.values()]
    return sum(edades) / len(edades)

def obtener_razas_mas_comunes(especie=None):
    """Obtener las razas más comunes, opcionalmente filtradas por especie"""
    razas = {}
    
    for pac in pacientes.values():
        if especie is None or pac.especie == especie:
            raza = pac.raza
            razas[raza] = razas.get(raza, 0) + 1
    
    return sorted(razas.items(), key=lambda x: x[1], reverse=True)

def obtener_propietarios_activos():
    """Obtener propietarios que han tenido citas recientes"""
    fecha_limite = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    propietarios_activos = set()
    
    for cita in citas_registradas:
        if cita.fecha >= fecha_limite and cita.id_paciente in pacientes:
            id_propietario = pacientes[cita.id_paciente].id_propietario
            propietarios_activos.add(id_propietario)
    
    return list(propietarios_activos)

def generar_reporte_personalizado(tipo_reporte):
    """Generar diferentes tipos de reportes personalizados"""
    reportes = {
        "resumen_general": _reporte_resumen_general,
        "inventario_critico": _reporte_inventario_critico,
        "actividad_veterinarios": _reporte_actividad_veterinarios,
        "pacientes_activos": _reporte_pacientes_activos,
        "estadisticas_especies": _reporte_estadisticas_especies
    }
    
    if tipo_reporte in reportes:
        return reportes[tipo_reporte]()
    else:
        return f"❌ Tipo de reporte '{tipo_reporte}' no disponible"

def _reporte_resumen_general():
    """Reporte general del sistema"""
    stats = obtener_estadisticas()
    edad_promedio = calcular_edad_promedio_pacientes()
    
    reporte = f"""
📊 REPORTE GENERAL DEL SISTEMA
================================
• Total de propietarios: {stats['propietarios']}
• Total de pacientes: {stats['pacientes']}
• Edad promedio de pacientes: {edad_promedio:.1f} años
• Citas totales: {stats['citas_total']}
• Medicamentos en inventario: {stats['medicamentos']}
• Historias clínicas: {stats['historias_clinicas']}
• Última actualización: {stats['ultima_actualizacion']}
"""
    return reporte

def _reporte_inventario_critico():
    """Reporte de inventario crítico"""
    medicamentos_criticos = [m for m in medicamentos.values() if int(m.stock) <= 10]
    medicamentos_vencen = obtener_medicamentos_por_vencer(30)
    
    reporte = "💊 REPORTE DE INVENTARIO CRÍTICO\n"
    reporte += "==================================\n"
    reporte += f"Medicamentos con stock bajo ({len(medicamentos_criticos)}):\n"
    for med in medicamentos_criticos:
        reporte += f"  • {med.nombre}: {med.stock} unidades\n"
    
    reporte += f"\nMedicamentos próximos a vencer ({len(medicamentos_vencen)}):\n"
    for med in medicamentos_vencen:
        reporte += f"  • {med.nombre}: vence {med.fecha_vencimiento}\n"
    
    return reporte

def _reporte_actividad_veterinarios():
    """Reporte de actividad por veterinario"""
    actividad = {}
    for cita in citas_registradas:
        vet_id = cita.id_veterinario
        actividad[vet_id] = actividad.get(vet_id, 0) + 1
    
    reporte = "👨‍⚕️ REPORTE DE ACTIVIDAD VETERINARIOS\n"
    reporte += "====================================\n"
    for vet_id, cantidad in actividad.items():
        nombre_vet = "Dr. Juan Pérez" if vet_id == "1234" else "Dra. María López"
        reporte += f"• {nombre_vet} (ID: {vet_id}): {cantidad} citas\n"
    
    return reporte

def _reporte_pacientes_activos():
    """Reporte de pacientes más activos"""
    actividad_pacientes = {}
    for cita in citas_registradas:
        pac_id = cita.id_paciente
        actividad_pacientes[pac_id] = actividad_pacientes.get(pac_id, 0) + 1
    
    # Ordenar por cantidad de citas
    pacientes_ordenados = sorted(actividad_pacientes.items(), key=lambda x: x[1], reverse=True)
    
    reporte = "🐾 REPORTE DE PACIENTES MÁS ACTIVOS\n"
    reporte += "===================================\n"
    for pac_id, cantidad in pacientes_ordenados[:10]:  # Top 10
        if pac_id in pacientes:
            nombre = pacientes[pac_id].nombre
            reporte += f"• {nombre} (ID: {pac_id}): {cantidad} citas\n"
    
    return reporte

def _reporte_estadisticas_especies():
    """Reporte de estadísticas por especies"""
    razas_perros = obtener_razas_mas_comunes("Perro")
    razas_gatos = obtener_razas_mas_comunes("Gato")
    
    reporte = "🐕🐱 REPORTE DE ESTADÍSTICAS POR ESPECIES\n"
    reporte += "==========================================\n"
    reporte += "Razas de perros más comunes:\n"
    for raza, cantidad in razas_perros[:5]:
        reporte += f"  • {raza}: {cantidad} pacientes\n"
    
    reporte += "\nRazas de gatos más comunes:\n"
    for raza, cantidad in razas_gatos[:5]:
        reporte += f"  • {raza}: {cantidad} pacientes\n"
    
    return reporte

# Funciones de utilidad para validación
def validar_fecha(fecha_str):
    """Validar formato de fecha YYYY-MM-DD"""
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora_str):
    """Validar formato de hora HH:MM"""
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False

def validar_email(email):
    """Validar formato básico de email"""
    return "@" in email and "." in email.split("@")[1]

def validar_telefono(telefono):
    """Validar formato básico de teléfono"""
    return telefono.replace("-", "").replace(" ", "").isdigit()

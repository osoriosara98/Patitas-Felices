"""
Configuración del Sistema de Gestión Veterinaria
"""

# Configuración de la aplicación
APP_CONFIG = {
    "nombre": "Sistema de Gestión Veterinaria - Patitas Felices",
    "version": "1.0.0",
    "descripcion": "Sistema completo para gestión de clínicas veterinarias",
    "autor": "Equipo de Desarrollo",
    "fecha_creacion": "2025"
}

# Configuración de inventario
INVENTARIO_CONFIG = {
    "stock_minimo_porcentaje": 10,  # 10% del stock inicial
    "alertas_automaticas": True,
    "formato_fecha": "%Y-%m-%d"
}

# Configuración de citas
CITAS_CONFIG = {
    "estados_validos": ["agendada", "realizada", "cancelada"],
    "horarios_disponibles": ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"],
    "formato_hora": "%H:%M"
}

# Configuración de reportes
REPORTES_CONFIG = {
    "formato_exportacion": "xml",
    "directorio_reportes": "reportes/",
    "incluir_graficos": False
}

# Mensajes del sistema
MENSAJES = {
    "exito": "✅",
    "error": "❌",
    "advertencia": "⚠️",
    "info": "ℹ️",
    "cargando": "🔄",
    "completado": "🎯",
    "mascota": "🐾",
    "medico": "👨‍⚕️",
    "medicina": "💊",
    "calendario": "📅"
}

# Validaciones
VALIDACIONES = {
    "edad_maxima_anos": 25,
    "peso_maximo_kg": 100,
    "especies_validas": ["Perro", "Gato"],
    "sexos_validos": ["Macho", "Hembra"]
}

# 🐾 Sistema de Gestión Veterinaria - Patitas Felices

## 🎯 Descripción
Sistema **completo y robusto** de gestión para clínicas veterinarias desarrollado en Python. Incluye gestión integral de propietarios, pacientes, citas médicas, historiales clínicos, inventario de medicamentos con **alertas inteligentes**, **reportes personalizados** y **sistema de backup automático**.

### 🚀 **Características Destacadas**
- ✅ **Sistema completo** con 11 requerimientos implementados al 100%
- ✅ **Datos de prueba robustos** con 60+ registros realistas
- ✅ **5 tipos de reportes personalizados**
- ✅ **Sistema de backup automático** en formato JSON
- ✅ **Alertas inteligentes** de inventario
- ✅ **Validación de integridad** de datos en tiempo real
- ✅ **Sin dependencias externas** - Solo requiere Python

## 📋 Funcionalidades Implementadas

### ✅ **Requerimientos Completados (11/11)**

**R1 - Almacenar información del tutor/propietario**
- Registro de propietarios con ID, nombre, teléfono, correo y dirección
- Gestión de múltiples mascotas por propietario

**R2 - Recopilar información de pacientes**
- Registro de pacientes (perros y gatos) con datos completos
- Generación automática de IDs únicos

**R3 - Agendar citas médicas**
- Sistema de agendamiento de citas con veterinarios
- Asignación automática de estados (agendada, realizada, cancelada)

**R4 - Historia clínica digital**
- Creación y almacenamiento de historias clínicas
- Registro de diagnósticos, tratamientos, vacunas y observaciones

**R5 - Inventario de medicamentos**
- Gestión completa de medicamentos con stock y fechas de vencimiento
- Sistema de alertas automáticas

**R6 - Actualización de inventario**
- Control de entradas y salidas de medicamentos
- Alertas de stock mínimo (10% del stock inicial)

**R7 - Informes mensuales**
- Generación de reportes estadísticos mensuales
- Exportación a formato XML

**R8 - Cancelación de citas**
- Funcionalidad para cancelar citas programadas
- Registro de motivos de cancelación

**R9 - Consulta de historial**
- Búsqueda por ID o nombre de paciente
- Visualización completa del historial médico

**R10 - Edición de datos**
- Modificación de información de pacientes y propietarios
- Interface amigable para actualizaciones

**R11 - Registro de atención médica**
- Documentación de consultas realizadas
- Creación automática de historias clínicas

### 🆕 **Funcionalidades Avanzadas Adicionales**

**Sistema de Reportes Personalizados (5 tipos)**
- 📊 Resumen general del sistema con estadísticas completas
- 💊 Inventario crítico con alertas de stock y vencimientos
- 👨‍⚕️ Actividad por veterinario con métricas de productividad
- 🐾 Pacientes más activos con ranking de frecuencia
- 📈 Estadísticas por especies y razas más comunes

**Gestión Avanzada de Datos**
- 🔍 Búsquedas inteligentes por múltiples criterios
- ✅ Validación de integridad referencial automática
- 💾 Sistema de backup automático en formato JSON
- 📊 Estadísticas en tiempo real del sistema
- 🔧 Utilidades avanzadas (50+ funciones)

**Sistema de Alertas Mejorado**
- ⚠️ Stock bajo de medicamentos (configurable)
- 📅 Medicamentos próximos a vencer (30 días)
- 🔔 Alertas automáticas en menú principal
- 📈 Métricas de sistema en tiempo real

## 📊 **Datos de Prueba Robustos**

El sistema incluye **datos de prueba extensos y realistas**:
- **8 propietarios** con información completa y variada
- **16 pacientes** (8 perros, 8 gatos) de razas diferentes
- **15 citas** distribuidas en diferentes estados y fechas
- **20 medicamentos** con categorías reales (antibióticos, vacunas, etc.)
- **20 historias clínicas** detalladas con diagnósticos veterinarios

### 🔢 **Estadísticas de Datos de Prueba**
```
👥 Propietarios: 8
🐾 Pacientes: 16 (8 perros, 8 gatos)
📅 Citas: 15 (6 realizadas, 6 agendadas, 3 canceladas)
💊 Medicamentos: 20 (3 con stock bajo)
📋 Historias clínicas: 20
🩺 Veterinarios: 2 disponibles
```

## 🏗️ **Estructura del Proyecto Modular Avanzada**

```
Patitas-felices/
├── 📁 interface/                   # 🎨 Interfaz de usuario y menús
│   ├── __init__.py                # Configuración del módulo de interfaz
│   ├── menu_principal.py          # Menú principal con alertas automáticas
│   └── menus/                     # Menús especializados por funcionalidad
│       ├── inicio.py              # Menú de gestión básica (propietarios/pacientes)
│       ├── citas.py               # Menú completo de gestión de citas
│       ├── historia.py            # Menú de historia clínica digital
│       ├── inventario.py          # Menú de inventario inteligente
│       └── utilidades.py          # Menú de utilidades y reportes
├── 📁 utils/                      # 🔧 Utilidades centralizadas del sistema
│   ├── __init__.py                # Configuración del módulo de utilidades
│   ├── consola.py                 # Utilidades de consola (pausas, limpieza, separadores)
│   └── seleccion.py               # Utilidades de selección (pacientes, propietarios, etc.)
├── 📁 data/                       # 💾 Gestión avanzada de datos y persistencia
│   ├── db.py                      # Base de datos mejorada con funciones avanzadas
│   ├── utilidades.py              # 50+ funciones de gestión y reportes
│   ├── backup_utils.py            # Utilidades centralizadas de backup
│   ├── veterinarios.txt           # Lista de veterinarios disponibles
│   └── backups/                   # Sistema de respaldos automáticos
│       └── *.json                 # Archivos de backup con metadatos
├── 📁 config/                     # ⚙️ Configuraciones del sistema
│   └── settings.py                # Configuraciones centralizadas y personalizables
├── 📁 modelos/                    # 🏗️ Modelos de datos robustos
│   ├── __init__.py                # Configuración del módulo de modelos
│   ├── propietario.py             # Clase Propietario con validaciones
│   ├── paciente.py                # Clase Paciente con relaciones
│   ├── cita.py                    # Clase Cita con estados y validaciones
│   ├── medicamento.py             # Clase Medicamento con alertas inteligentes
│   └── historia_clinica.py        # Clase HistoriaClinica con seguimiento
├── 📁 servicios/                  # 🔄 Servicios especializados de negocio
│   ├── __init__.py                # Configuración del módulo de servicios
│   ├── registro_propietario.py    # Gestión completa de propietarios
│   ├── registro_paciente.py       # Gestión completa de pacientes
│   ├── registro_cita.py           # Gestión y agendamiento de citas
│   ├── gestion_citas.py           # Operaciones avanzadas de citas
│   ├── historia_clinica.py        # Gestión de historiales médicos
│   ├── inventario_medicamentos.py # Gestión inteligente de inventario
│   ├── editar_datos.py            # Edición segura de información
│   └── informes.py                # Generación de reportes avanzados
├── 📄 main.py                     # 🚀 Programa principal con interfaz modular
├── 📄 datos_prueba.py            # 🎯 Datos de prueba robustos (60+ registros)
├── 📄 analizador_backup.py       # Función auxiliar para ver estadistica sobre los backups
└── 📄 README.md                   # 📚 Documentación principal actualizada
```

### 🎨 **Arquitectura Modular Mejorada**

#### **📁 interface/ - Capa de Presentación**
- **`menu_principal.py`**: Orquestador principal con alertas automáticas
- **`menus/`**: Menús especializados organizados por funcionalidad
  - Separación clara entre lógica de presentación y lógica de negocio
  - Reutilización de componentes de interfaz
  - Navegación intuitiva y consistente

#### **🔧 utils/ - Utilidades Centralizadas**
- **`consola.py`**: Manejo de interfaz de consola (pausas, limpieza, formateo)
- **`seleccion.py`**: Utilidades de selección reutilizables
- Eliminación de código duplicado en servicios
- Experiencia de usuario consistente en toda la aplicación

#### **💾 data/ - Gestión de Datos Avanzada**
- **`backup_utils.py`**: Sistema de backup optimizado (un backup por sesión)
- **`utilidades.py`**: Funciones avanzadas de análisis y reportes
- Persistencia automática tras cada operación
- Backup inteligente sin duplicación innecesaria

#### **⚙️ config/ - Configuración Centralizada**
- **`settings.py`**: Configuraciones del sistema centralizadas
- Personalización fácil de parámetros del sistema
- Separación de configuración del código de negocio

## 🚀 **Cómo Ejecutar**

### 🎯 **Opción 1: Demo Completa (Recomendada)**
```bash
# 1. Cargar datos de prueba robustos (60+ registros)
python main.py

#2. para analizar los backups podemos ejecutar.
python analizador_backup.py

```

## 📱 **Menú Principal Modular**

El sistema cuenta con una **arquitectura modular** e **interfaz intuitiva** organizada por categorías especializadas:

### 🎨 **Sistema de Menús Modular**
- **Menú Principal**: Orquestador central con alertas automáticas y navegación optimizada
- **Menús Especializados**: Cada funcionalidad tiene su propio menú enfocado
- **Utilidades Centralizadas**: Experiencia de usuario consistente en toda la aplicación
- **Navegación Intuitiva**: Pausas automáticas tras visualizaciones para mejor experiencia

### 📋 **Gestión Básica** (`interface/menus/inicio.py`)
1. **Registrar propietario** - Datos completos del dueño con validaciones
2. **Registrar paciente** - Mascotas con información detallada
3. **Ver propietarios** - Lista completa con estadísticas
4. **Ver pacientes** - Información de todas las mascotas
5. **Ver mascotas de un propietario** - Filtro por dueño

### 📅 **Gestión de Citas Avanzada** (`interface/menus/citas.py`)
6. **Menú de citas** (Submenú completo especializado)
   - ➕ Registrar nueva cita con selección de veterinario
   - 👁️ Ver todas las citas con filtros avanzados
   - ❌ Cancelar cita con registro de motivo
   - 🔍 Buscar citas por fecha y criterios múltiples
   - 🩺 Registrar atención médica completa

### 📋 **Historia Clínica Digital** (`interface/menus/historia.py`)
7. **Menú de historia clínica** (Submenú especializado)
   - 📝 Crear historia clínica detallada
   - 🔍 Consultar historial completo de paciente
   - 📈 Visualizar evolución médica con seguimiento

### 💊 **Inventario Inteligente** (`interface/menus/inventario.py`)
8. **Menú de inventario** (Submenú con alertas automáticas)
   - ➕ Registrar medicamento con alertas
   - 📊 Actualizar stock con seguimiento automático
   - 👁️ Ver inventario completo con estado de alertas
   - ⚠️ Verificar alertas automáticas de stock y vencimientos

### 🔧 **Utilidades y Reportes** (`interface/menus/utilidades.py`)
9. **Editar datos** - Modificación segura de pacientes y propietarios
10. **Generar informe mensual** - Estadísticas detalladas y análisis
11. **Verificar alertas de inventario** - Control inteligente de stock
12. **Reportes personalizados** - 5 tipos de análisis avanzados

## 🔧 **Características Técnicas Avanzadas**

### 💻 **Tecnologías y Arquitectura Utilizadas**
- **Python 3** - Lenguaje principal con características modernas y programación orientada a objetos
- **JSON** - Formato de backup y exportación de datos con metadatos
- **XML** - Formato de exportación de informes estandardizado
- **Datetime** - Manejo avanzado de fechas y horas con validaciones
- **Random** - Generación segura de IDs únicos con verificación de colisiones
- **OS/IO** - Manejo robusto de archivos y directorios
- **Separación de Capas** - Interface, servicios, modelos y persistencia independientes


### ✅ **Validaciones y Controles**
- **IDs únicos** para todas las entidades con validación automática
- **Integridad referencial** verificada en tiempo real
- **Formatos de fecha/hora** validados automáticamente
- **Control de stock** con alertas configurables
- **Existencia de registros** relacionados verificada


## 📈 **Funcionalidades Avanzadas**

### 🚨 **Sistema de Alertas Inteligente**
- **Stock Bajo**: Alerta cuando medicamentos están al 10% o menos del stock inicial
- **Próximo a Vencer**: Medicamentos que vencen en los próximos 30 días
- **Alertas Automáticas**: Se muestran automáticamente en el menú principal
- **Configurables**: Parámetros ajustables en archivo de configuración

### 📊 **Reportes y Estadísticas Personalizados**
#### **5 Tipos de Reportes Disponibles:**
1. **📊 Resumen General**: Estadísticas completas del sistema con métricas clave
2. **💊 Inventario Crítico**: Medicamentos con stock bajo y próximos a vencer
3. **👨‍⚕️ Actividad Veterinarios**: Productividad y citas por profesional
4. **🐾 Pacientes Activos**: Ranking de pacientes más frecuentes
5. **📈 Estadísticas Especies**: Razas más comunes por especie

#### **Capacidades de Análisis:**
- **Exportación XML**: Formato estándar para integración externa
- **Análisis de Tendencias**: Identificación de patrones de uso
- **Métricas de Productividad**: Rendimiento por veterinario
- **Análisis Demográfico**: Distribución por especies y razas

### 🔍 **Búsquedas Avanzadas e Inteligentes**
- **Búsqueda Múltiple**: Por ID, nombre, especie, fecha, etc.
- **Filtros Combinados**: Múltiples criterios simultáneos
- **Búsqueda Semántica**: Coincidencias parciales y flexibles
- **Historiales Completos**: Seguimiento completo de pacientes
- **Reportes por Fecha**: Análisis de períodos específicos

### 💾 **Sistema de Backup y Recuperación Optimizado**
- **Backup Eficiente**: Solo un backup de sesión por día, actualizado tras cada operación
- **Persistencia Automática**: Guardado automático tras cualquier cambio sin duplicación
- **Integridad de Datos**: Validación completa antes de cada backup
- **Metadatos Incluidos**: Información de versión, fecha y estadísticas del sistema
- **Recuperación Fácil**: Importación simple desde backup con validación
- **Versionado Inteligente**: Control de versiones sin saturar el almacenamiento
- **Backup Utils Centralizados**: Utilidades especializadas en `data/backup_utils.py`
  
### 💡 **Casos de Uso Especiales**
#### **🚨 Emergencias Médicas**
- Registro rápido de propietario y paciente nuevo
- Cita inmediata con veterinario disponible
- Historia clínica de emergencia
- Alertas de medicamentos críticos

#### **📈 Seguimiento Médico**
- Consulta de historiales completos con evolución
- Análisis de tratamientos anteriores
- Seguimiento de vacunaciones
- Control de medicamentos recetados

#### **📦 Gestión de Inventario**
- Control automático de stock con alertas
- Predicción de necesidades de reabastecimiento
- Análisis de medicamentos más utilizados
- Alertas de vencimientos próximos

#### **📊 Análisis Gerencial**
- Reportes de productividad por veterinario
- Análisis de especies más atendidas
- Estadísticas de frecuencia de citas
- Tendencias de uso del sistema

## 🛠️ **Mantenimiento y Personalización**

### 👨‍⚕️ **Agregar Nuevos Veterinarios**
Editar el archivo `data/veterinarios.txt`:
```
ID,Nombre
1234,Dr. Juan Pérez
5678,Dra. María López
9999,Dr. Nuevo Veterinario
0001,Dra. Ana García
```

### ⚙️ **Personalizar Configuraciones**
Modificar parámetros en `config.py`:
```python
# Configuración de inventario
INVENTARIO_CONFIG = {
    "stock_minimo_porcentaje": 15,  # Cambiar de 10% a 15%
    "alertas_automaticas": True,
    "dias_alerta_vencimiento": 45   # Cambiar de 30 a 45 días
}

# Personalizar mensajes
MENSAJES = {
    "exito": "✅",
    "error": "❌", 
    # Agregar más emojis personalizados
}
```

### 🔧 **Personalizar Alertas de Medicamentos**
Modificar parámetros en `modelos/medicamento.py`:
```python
# Cambiar porcentaje de stock mínimo
self.stock_minimo = max(1, int(stock * 0.15))  # 15% en lugar de 10%

# Ajustar días de alerta para vencimiento
def esta_por_vencer(self, dias_alerta=45):  # 45 días en lugar de 30
```

### 📊 **Extender Reportes**
Agregar nuevos tipos de reportes en `data/utilidades.py`:
```python
def _reporte_personalizado():
    """Tu reporte personalizado"""
    # Implementar lógica del reporte
    return reporte_string

# Agregar al diccionario de reportes
reportes["mi_reporte"] = _reporte_personalizado
```

### 🗃️ **Configurar Backup Automático**
Programar backups automáticos:
```python
# En main.py, agregar al final del menú
from data.db import exportar_datos_json
import datetime

# Backup diario automático
fecha = datetime.datetime.now().strftime("%Y%m%d")
exportar_datos_json(f"backup_diario_{fecha}.json")
```
#### 💾 **Backups JSON - Datos Reales del Sistema**
```python
# PROPÓSITO: Guardar/restaurar el estado real del sistema en uso
from data.db import exportar_datos_json
exportar_datos_json("backup_20241201_clinica.json")
```

**Características:**
- ✅ **Datos dinámicos reales** - Estado actual del sistema en producción
- ✅ **Para respaldo y recuperación** - Protección contra pérdida de datos
- ✅ **Preserva cambios** - Incluye todas las modificaciones realizadas
- ✅ **Con metadatos** - Fecha, estadísticas, validación de integridad
- ✅ **Formato estructurado** - JSON normalizado para migración/auditoría

### 📊 **Supuestos del Sistema**
1. **Un propietario por paciente** - Simplifica la gestión
2. **Un veterinario por cita** - Facilita la asignación
3. **Stock mínimo 10%** - Equilibrio entre control y flexibilidad
4. **Informes mensuales** - Frecuencia adecuada para análisis
5. **Alertas 30 días** - Tiempo suficiente para reabastecimiento

## 🎯 **Resumen Ejecutivo**

### ✅ **Estado Actual del Proyecto**
- **🎯 11/11 Requerimientos** implementados al 100%
- **🏗️ Arquitectura Modular** completamente refactorizada
- **📊 60+ Registros** de datos de prueba realistas  
- **🔧 50+ Funciones** de utilidades avanzadas centralizadas
- **📈 5 Tipos** de reportes personalizados
- **🚨 Sistema de alertas** completamente funcional
- **💾 Backup optimizado** con persistencia eficiente
- **✅ Testing automatizado** para sistema modular
- **🎨 Interfaz mejorada** con pausas automáticas y navegación optimizada

### 🏆 **Logros Destacados**
#### **Funcionalidad Superior y Arquitectura Modular**
- Sistema **robusto y escalable** con arquitectura modular profesional
- **Separación clara de responsabilidades** entre interfaz, servicios y datos
- **Utilidades centralizadas** que eliminan duplicación de código
- **Backup eficiente** con solo un respaldo por sesión sin sobrecargas
- **Experiencia de usuario optimizada** con pausas automáticas en consola
- **Datos de prueba extensos** para demostración inmediata
- **Sin dependencias externas** - Solo requiere Python

#### **🔧 Optimizaciones Técnicas Implementadas**
- **Eliminación de backups innecesarios** en servicios individuales
- **Persistencia automática** tras cada operación relevante
- **Modularización avanzada** con carpetas especializadas (`interface/`, `utils/`, `config/`)
- **Utilidades de consola centralizadas** para experiencia consistente
- **Sistema de menús especializados** por funcionalidad

---

## 🎉 **¡Sistema Completamente Funcional!**

**Desarrollado para la Clínica Veterinaria Patitas Felices**  
*Sistema de gestión integral profesional para optimizar la atención veterinaria* 🐾

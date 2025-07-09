"""
Script para cargar datos de prueba en el sistema veterinario
Ejecuta este archivo para poblar la base de datos con datos de ejemplo
"""

from modelos.propietario import Propietario
from modelos.paciente import Paciente
from modelos.cita import Cita
from modelos.medicamento import Medicamento
from modelos.historia_clinica import HistoriaClinica
from data.db import propietarios, pacientes, citas_registradas, medicamentos, historias_clinicas

def cargar_datos_prueba():
    print("🔄 Cargando datos de prueba robustos...")
    
    # Limpiar datos existentes para evitar duplicados
    propietarios.clear()
    pacientes.clear()
    citas_registradas.clear()
    medicamentos.clear()
    historias_clinicas.clear()
    
    # Propietarios de ejemplo más diversos
    prop1 = Propietario("101", "Juan Pérez", "300-123-4567", "juan.perez@email.com", "Calle 10 #20-30")
    prop2 = Propietario("102", "María García", "310-987-6543", "maria.garcia@email.com", "Carrera 15 #25-40")
    prop3 = Propietario("103", "Carlos Rodríguez", "320-555-1234", "carlos.rod@email.com", "Avenida 80 #12-15")
    prop4 = Propietario("104", "Ana Martínez", "315-789-0123", "ana.martinez@email.com", "Calle 45 #67-89")
    prop5 = Propietario("105", "Luis Felipe", "301-456-7890", "luis.felipe@email.com", "Carrera 30 #45-60")
    prop6 = Propietario("106", "Carmen Silva", "318-234-5678", "carmen.silva@email.com", "Avenida 68 #23-45")
    prop7 = Propietario("107", "Roberto Castro", "302-345-6789", "roberto.castro@email.com", "Calle 85 #12-34")
    prop8 = Propietario("108", "Sandra López", "319-567-8901", "sandra.lopez@email.com", "Carrera 7 #89-12")
    
    propietarios.update({
        "101": prop1, "102": prop2, "103": prop3, "104": prop4,
        "105": prop5, "106": prop6, "107": prop7, "108": prop8
    })
    
    # Pacientes de ejemplo más variados (perros y gatos de diferentes razas y edades)
    # Perros
    pac1 = Paciente("10001", "Max", "3", "Perro", "Golden Retriever", "25", "Macho", "101")
    pac2 = Paciente("10003", "Rocky", "5", "Perro", "Pastor Alemán", "30", "Macho", "101")
    pac3 = Paciente("10005", "Buddy", "2", "Perro", "Labrador", "28", "Macho", "104")
    pac4 = Paciente("10007", "Bella", "4", "Perro", "Bulldog Francés", "12", "Hembra", "105")
    pac5 = Paciente("10009", "Zeus", "6", "Perro", "Rottweiler", "45", "Macho", "106")
    pac6 = Paciente("10011", "Lola", "1", "Perro", "Chihuahua", "3", "Hembra", "107")
    pac7 = Paciente("10013", "Thor", "7", "Perro", "Husky Siberiano", "35", "Macho", "108")
    pac8 = Paciente("10015", "Nina", "3", "Perro", "Border Collie", "22", "Hembra", "104")
    
    # Gatos
    pac9 = Paciente("10002", "Luna", "2", "Gato", "Siamés", "4", "Hembra", "102")
    pac10 = Paciente("10004", "Mimi", "1", "Gato", "Persa", "3", "Hembra", "103")
    pac11 = Paciente("10006", "Whiskers", "5", "Gato", "Maine Coon", "7", "Macho", "105")
    pac12 = Paciente("10008", "Shadow", "3", "Gato", "Angora", "5", "Macho", "106")
    pac13 = Paciente("10010", "Cleopatra", "4", "Gato", "Esfinge", "4", "Hembra", "107")
    pac14 = Paciente("10012", "Garfield", "2", "Gato", "Común Europeo", "6", "Macho", "108")
    pac15 = Paciente("10014", "Princess", "6", "Gato", "Ragdoll", "5", "Hembra", "102")
    pac16 = Paciente("10016", "Felix", "1", "Gato", "British Shorthair", "4", "Macho", "103")
    
    # Registrar todos los pacientes
    todos_pacientes = [pac1, pac2, pac3, pac4, pac5, pac6, pac7, pac8, 
                      pac9, pac10, pac11, pac12, pac13, pac14, pac15, pac16]
    
    for pac in todos_pacientes:
        pacientes[pac.id] = pac
    
    # Actualizar mascotas de propietarios de forma automática
    for propietario in propietarios.values():
        propietario.mascotas = [pac.id for pac in pacientes.values() if pac.id_propietario == propietario.id]
    
    # Citas de ejemplo más realistas con diferentes fechas y estados
    citas_ejemplo = [
        # Citas realizadas (pasadas)
        Cita("1001", "2024-12-15", "10:00", "Vacunación anual", "10001", "1234", "realizada"),
        Cita("1002", "2024-12-16", "14:30", "Control rutinario", "10002", "5678", "realizada"),
        Cita("1003", "2024-12-18", "09:00", "Revisión dental", "10003", "1234", "realizada"),
        Cita("1004", "2024-12-20", "16:00", "Desparasitación", "10004", "5678", "realizada"),
        Cita("1005", "2025-01-10", "11:00", "Cirugía menor", "10005", "1234", "realizada"),
        Cita("1006", "2025-01-12", "08:30", "Control post-operatorio", "10006", "5678", "realizada"),
        
        # Citas agendadas (futuras)
        Cita("1007", "2025-07-15", "09:00", "Vacunación", "10007", "1234", "agendada"),
        Cita("1008", "2025-07-16", "10:30", "Control general", "10008", "5678", "agendada"),
        Cita("1009", "2025-07-18", "14:00", "Revisión dermatológica", "10009", "1234", "agendada"),
        Cita("1010", "2025-07-20", "15:30", "Limpieza dental", "10010", "5678", "agendada"),
        Cita("1011", "2025-08-01", "11:00", "Control de peso", "10011", "1234", "agendada"),
        Cita("1012", "2025-08-03", "16:00", "Vacunación antirrábica", "10012", "5678", "agendada"),
        
        # Citas canceladas
        Cita("1013", "2025-06-25", "10:00", "Consulta general", "10013", "1234", "cancelada"),
        Cita("1014", "2025-06-27", "14:30", "Revisión ocular", "10014", "5678", "cancelada"),
        Cita("1015", "2025-06-30", "09:30", "Control nutricional", "10015", "1234", "cancelada")
    ]
    
    citas_registradas.extend(citas_ejemplo)
    
    # Medicamentos de ejemplo más completos y realistas
    medicamentos_ejemplo = [
        # Antibióticos
        Medicamento("101", "Amoxicilina", "Antibiótico para infecciones bacterianas", 50, "2025-06-30", 15000),
        Medicamento("102", "Doxiciclina", "Antibiótico de amplio espectro", 30, "2025-08-15", 18000),
        Medicamento("103", "Cefalexina", "Antibiótico para infecciones de piel", 25, "2025-04-20", 12000),
        
        # Vacunas
        Medicamento("104", "Vacuna Rabia", "Vacuna contra la rabia", 25, "2024-12-31", 25000),
        Medicamento("105", "Vacuna Triple", "Vacuna contra moquillo, hepatitis y parvovirus", 20, "2025-03-15", 22000),
        Medicamento("106", "Vacuna Leucemia Felina", "Vacuna específica para gatos", 15, "2025-01-30", 28000),
        
        # Antiparasitarios
        Medicamento("107", "Antiparasitario Interno", "Contra parásitos intestinales", 5, "2024-08-15", 12000),  # Stock bajo
        Medicamento("108", "Antipulgas", "Tratamiento contra pulgas y garrapatas", 40, "2025-09-10", 16000),
        Medicamento("109", "Desparasitante Tópico", "Aplicación externa", 35, "2025-05-25", 14000),
        
        # Analgésicos y antiinflamatorios
        Medicamento("110", "Meloxicam", "Antiinflamatorio para perros", 100, "2025-03-20", 8000),
        Medicamento("111", "Tramadol", "Analgésico para dolor moderado", 60, "2025-07-18", 20000),
        Medicamento("112", "Carprofeno", "Antiinflamatorio no esteroideo", 45, "2025-02-28", 15000),
        
        # Medicamentos especializados
        Medicamento("113", "Furosemida", "Diurético para problemas cardíacos", 30, "2025-10-12", 18000),
        Medicamento("114", "Omeprazol", "Protector gástrico", 50, "2025-06-08", 9000),
        Medicamento("115", "Prednisolona", "Corticoide para alergias", 25, "2025-04-15", 12000),
        
        # Medicamentos con stock crítico
        Medicamento("116", "Epinefrina", "Para emergencias alérgicas", 3, "2025-11-30", 35000),  # Stock crítico
        Medicamento("117", "Insulina Canina", "Para diabetes en perros", 8, "2025-01-20", 45000),  # Stock bajo
        
        # Suplementos
        Medicamento("118", "Omega 3", "Suplemento para pelaje y piel", 80, "2026-02-14", 25000),
        Medicamento("119", "Calcio + Vitamina D", "Suplemento óseo", 70, "2025-12-05", 15000),
        Medicamento("120", "Probióticos", "Para salud digestiva", 55, "2025-09-30", 18000)
    ]
    
    for med in medicamentos_ejemplo:
        medicamentos[med.id] = med
    
    # Historias clínicas de ejemplo más detalladas
    historias_ejemplo = [
        # Historias para perros
        HistoriaClinica("20001", "10001", "Paciente sano", "Vacuna aplicada correctamente", "Vacuna anual", "Buen estado general, peso ideal"),
        HistoriaClinica("20002", "10003", "Artritis leve", "Antiinflamatorio Meloxicam", "", "Mejoría esperada en 2 semanas"),
        HistoriaClinica("20003", "10005", "Otitis externa", "Limpieza + antibiótico tópico", "", "Control en 7 días"),
        HistoriaClinica("20004", "10007", "Displasia de cadera", "Manejo conservador con analgésicos", "", "Evitar ejercicio intenso"),
        HistoriaClinica("20005", "10009", "Torsión gástrica", "Cirugía de emergencia exitosa", "", "Recuperación completa"),
        HistoriaClinica("20006", "10011", "Luxación de rótula", "Reducción manual", "", "Reposo por 10 días"),
        HistoriaClinica("20007", "10013", "Dermatitis alérgica", "Corticoides + baños medicinales", "", "Identificar alérgeno"),
        HistoriaClinica("20008", "10015", "Obesidad", "Plan nutricional personalizado", "", "Perder 3kg en 2 meses"),
        
        # Historias para gatos
        HistoriaClinica("20009", "10002", "Conjuntivitis", "Gotas oftálmicas", "", "Mejora esperada en 5 días"),
        HistoriaClinica("20010", "10004", "Cistitis idiopática", "Antibióticos + dieta especial", "", "Aumentar consumo de agua"),
        HistoriaClinica("20011", "10006", "Gingivitis severa", "Limpieza dental bajo anestesia", "", "Higiene oral diaria"),
        HistoriaClinica("20012", "10008", "Hipertiroidismo", "Medicación metimazol", "", "Control mensual de T4"),
        HistoriaClinica("20013", "10010", "Herida por pelea", "Sutura + antibióticos", "", "Mantener en interior"),
        HistoriaClinica("20014", "10012", "Parásitos intestinales", "Desparasitante oral", "", "Repetir en 15 días"),
        HistoriaClinica("20015", "10014", "Insuficiencia renal", "Dieta renal + fluidoterapia", "", "Pronóstico reservado"),
        HistoriaClinica("20016", "10016", "Vacunación múltiple", "Triple felina + leucemia", "", "Próxima dosis en 1 año"),
        
        # Historias de seguimiento
        HistoriaClinica("20017", "10001", "Control post-vacunal", "Sin reacciones adversas", "", "Próximo control en 1 año"),
        HistoriaClinica("20018", "10005", "Revisión post-quirúrgica", "Cicatrización excelente", "", "Alta médica"),
        HistoriaClinica("20019", "10009", "Control cardiológico", "Función cardíaca normal", "", "Control anual"),
        HistoriaClinica("20020", "10002", "Seguimiento conjuntivitis", "Resolución completa", "", "Tratamiento finalizado")
    ]
    
    historias_clinicas.extend(historias_ejemplo)
    
    print("✅ Datos de prueba robustos cargados exitosamente!")
    print(f"📋 {len(propietarios)} propietarios registrados")
    print(f"🐾 {len(pacientes)} pacientes registrados ({len([p for p in pacientes.values() if p.especie == 'Perro'])} perros, {len([p for p in pacientes.values() if p.especie == 'Gato'])} gatos)")
    print(f"📅 {len(citas_registradas)} citas registradas")
    print(f"    - {len([c for c in citas_registradas if c.estado == 'realizada'])} realizadas")
    print(f"    - {len([c for c in citas_registradas if c.estado == 'agendada'])} agendadas")
    print(f"    - {len([c for c in citas_registradas if c.estado == 'cancelada'])} canceladas")
    print(f"💊 {len(medicamentos)} medicamentos en inventario")
    print(f"    - {len([m for m in medicamentos.values() if int(m.stock) <= 10])} con stock bajo")
    print(f"📋 {len(historias_clinicas)} historias clínicas registradas")
    
    # Mostrar estadísticas adicionales
    print("\n📊 Estadísticas adicionales:")
    print(f"   • Promedio de mascotas por propietario: {len(pacientes)/len(propietarios):.1f}")
    print("   • Veterinarios disponibles: 2 (Dr. Juan Pérez, Dra. María López)")
    print(f"   • Rango de edades de pacientes: {min([int(p.edad) for p in pacientes.values()])}-{max([int(p.edad) for p in pacientes.values()])} años")
    print(f"   • Medicamentos próximos a vencer: {len([m for m in medicamentos.values() if '2024' in m.fecha_vencimiento])}")

def mostrar_resumen_datos():
    """Función para mostrar un resumen completo de los datos cargados"""
    print("\n" + "="*60)
    print("📊 RESUMEN COMPLETO DE DATOS DE PRUEBA")
    print("="*60)
    
    print(f"\n👥 PROPIETARIOS ({len(propietarios)}):")
    for prop in propietarios.values():
        mascotas_count = len(prop.mascotas)
        print(f"   • {prop.nombre} (ID: {prop.id}) - {mascotas_count} mascota(s)")
    
    print("\n🐾 PACIENTES POR ESPECIE:")
    perros = [p for p in pacientes.values() if p.especie == 'Perro']
    gatos = [p for p in pacientes.values() if p.especie == 'Gato']
    print(f"   🐕 Perros: {len(perros)}")
    for perro in perros:
        print(f"      - {perro.nombre} ({perro.raza}, {perro.edad} años)")
    print(f"   🐱 Gatos: {len(gatos)}")
    for gato in gatos:
        print(f"      - {gato.nombre} ({gato.raza}, {gato.edad} años)")
    
    print("\n📅 ESTADO DE CITAS:")
    estados = {}
    for cita in citas_registradas:
        estados[cita.estado] = estados.get(cita.estado, 0) + 1
    for estado, cantidad in estados.items():
        print(f"   • {estado.capitalize()}: {cantidad}")
    
    print("\n💊 INVENTARIO CRÍTICO:")
    criticos = [m for m in medicamentos.values() if int(m.stock) <= 10]
    for med in criticos:
        print(f"   ⚠️ {med.nombre}: {med.stock} unidades")
    
    print("="*60)

if __name__ == "__main__":
    cargar_datos_prueba()
    mostrar_resumen_datos()
    print("\n🎯 Puedes importar estos datos ejecutando:")
    print("   from datos_prueba import cargar_datos_prueba")
    print("   cargar_datos_prueba()")
    print("\n🔧 Funciones adicionales disponibles:")
    print("   from datos_prueba import mostrar_resumen_datos")
    print("   mostrar_resumen_datos()")
    print("\n¡Ahora puedes probar todas las funcionalidades del sistema!") 
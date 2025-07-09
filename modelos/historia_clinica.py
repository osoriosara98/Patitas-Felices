from datetime import datetime

class HistoriaClinica:
    def __init__(self, id_historia, id_paciente, diagnostico, tratamiento, vacunas="", observaciones=""):
        self.id = id_historia
        self.id_paciente = id_paciente
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.vacunas = vacunas
        self.observaciones = observaciones
        self.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"Historia Clínica ID: {self.id} - Paciente ID: {self.id_paciente}\n"
                f"Fecha: {self.fecha_actualizacion}\n"
                f"Diagnóstico: {self.diagnostico}\n"
                f"Tratamiento: {self.tratamiento}\n"
                f"Vacunas: {self.vacunas}\n"
                f"Observaciones: {self.observaciones}\n"
                f"{'-'*50}") 
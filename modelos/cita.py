# modelos: Una "plantilla" para crear muchos objetos del mismo tipo (en este caso, citas).

class Cita:
    def __init__(self, id, fecha, hora, motivo, id_paciente, id_veterinario, estado="agendada"):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.id_paciente = id_paciente
        self.id_veterinario = id_veterinario
        self.estado = estado  # agendada, cancelada, realizada

    def __str__(self):
        return f"Cita ID: {self.id}, Fecha: {self.fecha}, Hora: {self.hora}, Paciente ID: {self.id_paciente}, Veterinario ID: {self.id_veterinario}, Motivo: {self.motivo}, Estado: {self.estado}"

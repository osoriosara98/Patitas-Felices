class Paciente:
    def __init__(self, id_paciente, nombre, edad, especie, raza, peso, sexo, id_propietario):
        self.id = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.raza = raza
        self.peso = peso
        self.sexo = sexo
        self.id_propietario = id_propietario

    def __str__(self):
        return (f"{self.nombre} ({self.especie}) - Raza: {self.raza}, Edad: {self.edad}, "
                f"Peso: {self.peso}kg, Sexo: {self.sexo}, Propietario ID: {self.id_propietario}")
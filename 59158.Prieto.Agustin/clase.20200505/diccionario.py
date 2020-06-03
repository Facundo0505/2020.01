class Persona():
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def get_documento(self, documento):
        return self.documento
    
    def set_documento(self, documento):
        self.documento = documento


if __name__ == '__main__':
    persona = Persona(23424, 'Prieto')
    persona.nombre = 'Agustin'
    print(persona.__dict__)

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        ColorPermitido = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in ColorPermitido:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if (i != None):
                contador += 1
        return contador

    def verificarIntegridad(self):
            for i in self.asientos:
                if i != None:
                    if (i.registro != self.registro) or (self.registro != self.motor.registro):
                        return "Las piezas no son originales"
                else:
                    return "Auto original"



class Motor:
    def __init__(self, numeroCilindros,tipo, registro):
        self.numeroCilindros =numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipoPermitido = ["gasolina", "electrico"]
        if tipo in tipoPermitido:
            self.tipo = tipo



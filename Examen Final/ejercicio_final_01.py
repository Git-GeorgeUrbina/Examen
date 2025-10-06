"""
1.
Escriba un programa donde tendrá los siguientes requisitos (4 ptos): Reglas:
• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad) (validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos suficientes, imprimir “Saldo insuficiente”; si hay, basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el sueldo en 30% por defecto).
"""
class persona:
    def __init__(self, nombre, edad, nacionalidad = "peruana", saldo=0.0):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def actualizar_nombre(self):
        self.nombre = self.nombre
        print("El nombre es: ".format(self.nombre))

    def actualizar_edad(self):
        if edad > 0:
            self.edad = self.edad
        else:
            print("La edad tiene que ser mayor que 0")

    def cumplir_anios(self):
        self.edad += 1
        print ("La edad cumplida es: ".format (self.edad))

    def mostrar_saldo(self):
        self.saldo = self.saldo
        print (" El saldo actual es: ".format(self.saldo))

    def transferir(self, destino, monto):
        if self.saldo < monto:
            print ( "Saldo insuficiente")
        else:
            self.saldo = self.saldo - monto
            destino.saldo = destino.saldo + monto
            print ("La transferncia se ha realizado de {} hacia {}".format (self.nombre, destino.nombre))

class empleado(persona):
    def __init__(self, nombre, edad, sueldo, nacionalidad = "peruana", saldo=0.0):
        super().__init__(nombre, edad, nacionalidad, saldo)
        self.sueldo = sueldo
        print (sueldo)

    def aumento_sueldo (self, porcentaje=0.30):
        incremento =  self.sueldo * porcentaje
        self.sueldo = self.sueldo + incremento
        print ("Para {}, el sueldo aumentó en {:.0f}%, siendo el nuevo sueldo {:.2f}".format( self.nombre, porcentaje*100, self.sueldo))

    def prediccion(self, anio_objetivo, edad_parametro=None):
        anio_actual = 2025
        anio_faltantes = anio_objetivo - anio_actual
        if edad_parametro is not None:
            if edad_parametro < self.edad:
                print ("La persona {}, en el año {} tendrá {} años". format(self.nombre, anio_objetivo, edad_parametro))
        else:
            edad_futura = self.edad + anios_faltants
            print("LA persona {}, en el año {} tendrá {} años".format(self.nombre, anio_objetivo, edad_futura))

empleado_1 = empleado("Miguel", 27, 1500, "Peruana")
empleado_2 = empleado("luis", 25, 3100, )

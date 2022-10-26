"""Crear un programa de evaluación de pago de impuestos"""

class Persona:

    # constructor
    def __init__(self, nombre, nombre2, edad):
        self.__nombre = nombre  # Definiendo como atributo privado
        self.nombre2 = nombre2
        self.edad = edad

    def datos(self):
        print("Nombre: {} \nEdad: {}".format(self.__nombre, self.edad))


# Aplicando  Herencia
class Empleado(Persona):

    def __init__(self, nombre, nombre2, edad, sueldo = 0):
        super().__init__(nombre,nombre2, edad, )
        self.sueldo = sueldo
        self.impuesto = 0

    def sueldos(self):
        self.sueldo = float(input("\nIngrese su sueldo: "))

    def impuestos(self):
        impuesto = 0.09 * self.sueldo

        if self.sueldo <= 4500:
            impuesto = 0
        self.impuesto = impuesto


persona1 = Persona("antonio", "antonio2", 55)
# da error por que es un atributo encapsuladoq no puede ser usado fuera de la clase
# print("\nLa persona1 se llama {}".format(persona1.__nombre))
print("\nLa persona1 tiene {} años".format(persona1.edad))
persona1.datos()


empleado1 = Empleado("fany","fany2", 21)
print("\nLa empleada tiene {} años".format(empleado1.edad))
empleado1.datos()

empleado1.sueldos()
empleado1.impuestos()

print("\nLa persona 1 tiene que pagar {} soles de impuesto\n".format(empleado1.impuesto))


def manejoDiccionario():
    diccionario = {"Nombre": empleado1.nombre2,"Edad": empleado1.edad, "Impuesto": empleado1.impuesto}
    return diccionario


print(manejoDiccionario())


def generarArchivoEmpleado():

    file = open("my_files/file_empleado.txt", "w")

    nombres = []
    edades = []
    impuestos = []

    for i in range(2):
        nombre = input("\nIngrese su nombre: ")
        edad = input("Ingrese su edad: ")
        sueldo = float(input("Ingrese su sueldo: "))

        if sueldo <= 4500:
            impuesto = 0
        else:
            impuesto = 0.09 * sueldo

        nombres.append(nombre)
        edades.append(edad)
        impuestos.append(impuesto)

        file.writelines("Empleado{}: {}, {}, {} ".format(i, nombres[i], edades[i], impuestos[i]))

    file = open("my_files/file_empleado.txt", "r")

    print("\n'file_empleado.txt' tiene el siguiente contenido: \n")

    for i in file.readlines():
        print(i)

    file.close()


print(generarArchivoEmpleado())



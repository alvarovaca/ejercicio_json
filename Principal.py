import json
with open("agendas.json") as fichero:
    datos=json.load(fichero)

from Funciones import *

print()
print("                                                                         MENÚ                                                                 ")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("1. .")
print("2. .")
print("3. .")
print("4. .")
print("5. .")
print("6. Salir del menú.")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print()

while True:
    opcion=int(input("Introduce una opción: "))
    while opcion<1 or opcion>6:
        opcion=int(input("La opción introducida no es válida. Vuelve a intentarlo: "))
    if opcion==1:
        print()
        print("---------------")
        print("LISTAR PERSONAS")
        print("---------------")
        print()
        nombres,apellidos,emails=ListarInformacion(datos)
        for elem, elem1, elem2 in zip(nombres,apellidos,emails):
            print(elem, elem1, "----------", elem2)
        print()
    elif opcion==2:
        print()
        print("-----------------------")
        print("CONTAR USUARIOS ACTIVOS")
        print("-----------------------")
        print()
        
        print()
    elif opcion==3:
        print()
        print("-------------------------")
        print("PERSONAS DENTRO DEL RANGO")
        print("-------------------------")
        print()
        
        print()
    elif opcion==4:
        print()
        print("--------------")
        print("AMIGO DE QUIÉN")
        print("--------------")
        print()
        
        print()
    elif opcion==5:
        print()
        print("-------------")
        print("OPENSTREETMAP")
        print("-------------")
        print()
        
        print()
    elif opcion==6:
        print()
        print("Gracias por utilizar nuestro menú.")
        print()
        break
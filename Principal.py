import json
with open("agendas.json") as fichero:
    datos=json.load(fichero)

from Funciones import *

print()
print("                                                                         MENÚ                                                                 ")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("1. Listar los nombres y apellidos de todas las personas de las que se guarda información junto con su correo electrónico.")
print("2. Contar el número de personas que se encuentran conectadas actualmente (isActive) y en caso de así quererlo, mostrar también sus nombres.")
print("3. Pedir por teclado un valor mínimo y un valor máximo y mostrar el nombre, el apellido y el balance de las personas cuyo balance se encuentre entre ambos valores, además de la persona con más balance dentro de ese rango.")
print("4. Pedir por teclado el nombre de un amigo y mostrar de quién es amigo esa persona, además del hobbie que comparten.")
print("5. Pedir por teclado nombre y apellido de personas y mostrar la URL de OpenStreetMap de su localización hasta que se introduzca un espacio.")
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
        nombres,apellidos=ContarOnline(datos)
        print(len(nombres))
        print()
        siono=input("¿Deseas ver el nombre de dichas personas? (S/N): ")
        while ValidarSioNo(siono)!=True:
            siono=input("La respuesta introducida no es válida. Vuelve a intentarlo: ")
        if siono=="S":
            print()
            for elem,elem1 in zip(nombres,apellidos):
                print(elem, elem1)
        print()
    elif opcion==3:
        print()
        print("-------------------------")
        print("PERSONAS DENTRO DEL RANGO")
        print("-------------------------")
        print()
        minimo=float(input("Introduce el valor mínimo del rango a buscar: "))
        maximo=float(input("Introduce el valor máximo del rango a buscar: "))
        while ValidarRango(minimo,maximo)!=True:
            maximo=float(input("El valor máximo introducido es menor o igual que el mínimo. Vuelve a intentarlo: "))
        print()
        nombres,apellidos,balances,personaadinerada=BalancePersonas(minimo,maximo,datos)
        if len(nombres)>0:
            for elem, elem1, elem2 in zip(nombres,apellidos,balances):
                print(elem, elem1, "----------", elem2)
            print()
            for i in personaadinerada:
                print(i)
        else:
            print("No se han encontrado personas dentro del rango introducido.")
        print()
    elif opcion==4:
        print()
        print("--------------")
        print("AMIGO DE QUIÉN")
        print("--------------")
        print()
        nombre=input("Introduce el nombre de la persona que deseas buscar: ")
        print()
        nombres,apellidos,hobbies=EncontrarAmigos(nombre,datos)
        if len(nombres)>0:
            for elem, elem1, elem2 in zip(nombres,apellidos,hobbies):
                print(nombre, "es amigo de", elem, elem1, "y el hobbie que comparten es", elem2+".")
        else:
            print("No se ha encontrado la persona introducida.")
        print()
    elif opcion==5:
        print()
        print("-------------")
        print("OPENSTREETMAP")
        print("-------------")
        while True:
            print()
            nombre=input("Introduce el nombre de la persona a buscar: ")
            if nombre==" ":
                break
            apellido=input("Introduce el apellido de la persona a buscar: ")
            zoom=input("Introduce el zoom con el que deseas ver el OpenStreetMap: ")
            print()
            if len(OpenStreetMap(nombre,apellido,zoom,datos))>0:
                print(OpenStreetMap(nombre,apellido,zoom,datos)[0])
            else:
                print("No se ha encontrado el OpenStreetMap de la persona introducida.")
        print()
    elif opcion==6:
        print()
        print("Gracias por utilizar nuestro menú.")
        print()
        break
#Ejercicio 1.

def ListarInformacion(datos):
    nombres=[]
    apellidos=[]
    emails=[]
    for i in datos:
        nombres.append(i["name"]["first"])
        apellidos.append(i["name"]["last"])
        emails.append(i["email"])
    return nombres, apellidos, emails

#Ejercicio 2.

def ContarOnline(datos):
    nombres=[]
    apellidos=[]
    for i in datos:
        if i["isActive"]==True:
            nombres.append(i["name"]["first"])
            apellidos.append(i["name"]["last"])
    return nombres,apellidos

#Ejercicio 3.

def BalancePersonas(minimo,maximo,datos):
    nombres=[]
    apellidos=[]
    balances=[]
    for i in datos:
        if float(i["balance"])>=minimo and float(i["balance"])<=maximo:
            nombres.append(i["name"]["first"])
            apellidos.append(i["name"]["last"])
            balances.append(i["balance"])
    personaconmasdinero=[]
    for elem,elem1,elem2 in zip(nombres,apellidos,balances):
        if elem2==max(balances):
            personaconmasdinero.append("La persona más adinerada es "+elem+" "+elem1+" con "+elem2+" euros.")
    return nombres,apellidos,balances,personaconmasdinero

#Ejercicio 4.

def EncontrarAmigos(nombre,datos):
    nombres=[]
    apellidos=[]
    hobbies=[]
    for i in datos:
        for elem in i["friends"]:
            if elem["name"]==nombre:
                nombres.append(i["name"]["first"])
                apellidos.append(i["name"]["last"])
                hobbies.append(i["hobbie"])
    return nombres, apellidos, hobbies

#Ejercicio 5.

def OpenStreetMap(nombre,apellido,datos):
    

#Funciones extra.

def ValidarSioNo(siono):
    if siono=="S" or siono=="N":
        return True

def ValidarRango(minimo,maximo):
    if minimo<maximo:
        return True
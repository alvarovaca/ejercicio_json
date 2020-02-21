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
        if i["balance"]>=minimo and i["balance"]<=maximo:
            nombres.append(i["name"]["first"])
            apellidos.append(i["name"]["last"])
            balances.append(i["balance"])
    personasconmasdinero=[]
    for elem,elem1,elem2 in zip(nombres,apellidos,balances):
        if elem2==max(balances):
            personaconmasdinero.append(elem,elem1,elem2)
    return nombres,apellidos,balances, personasconmasdinero
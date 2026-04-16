
#1
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [   {"nombre": "Ricky Martin", "pais": "Puerto Rico"}, {"nombre": "Chayanne", "pais": "Puerto Rico"} ]  
ciudades = { "México": ["Ciudad de México", "Guadalajara", "Cancún"], "Chile": ["Santiago", "Concepción", "Viña del Mar"] }
coordenadas = [ {"latitud": 8.2588997, "longitud": -84.9399704} ]

matriz[1][0] = 6

cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades["México"][2] = "Monterrey"

coordenadas[0]["latitud"] = 9.9355431



#2

cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


def iterarDiccionario(lista):
    for i in lista:
        pares = []
        for llave, valor in i.items():
            pares.append(f"{llave} - {valor}")

        print(", ".join(pares))

iterarDiccionario(cantantes2)

#3

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
#4

def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)
        print()  

x = int(input("Ingrese un número para ejecutar del 1 al 4: "))
if x== 1:
    print("Matriz:", matriz)
    print("Cantantes:", cantantes)
    print("Ciudades:", ciudades)
    print("Coordenadas:", coordenadas)
if x == 2:
    
    iterarDiccionario(cantantes)
if x == 3:
    
    iterarDiccionario2("nombre", cantantes2)
if x == 4:

    imprimirInformacion(ciudades)
if x < 1 or x > 4:
    print("Número no válido. Por favor, ingrese un número del 1 al 4.")

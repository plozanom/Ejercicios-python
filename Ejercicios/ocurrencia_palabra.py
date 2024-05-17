"""
Algoritmo con Python para contar las ocurrencias de una palabra en una oración
sin usar split ni count.
"""

oracion = input("Digite la frase a analizar y luego presione 'Enter': ").lower()
palabra_buscada = input("Digite la palabra a buscar: ").lower()

def separador_de_palabras(oracion):
    palabra = ""
    palabras = []

    for letras in oracion:
        if letras in (" ",".","?","¿","!","¡","*"):
            palabras.append(palabra)
            palabra = ""
        else:
            palabra += letras
        
        if "" in palabras:
            palabras.remove("")

    palabras.append(palabra)
    palabras.remove("")

    return palabras

#print(separador_de_palabras(oracion))

lista = separador_de_palabras(oracion)

def contador(buscada, lista_de_palabras):

    ocurrencias = 0

    for palabra in lista_de_palabras:
        if buscada == palabra:
            ocurrencias += 1
    
    return ocurrencias

ocurrencias = contador(palabra_buscada, lista)

print(f'La palabra: "{palabra_buscada}" se encuentra {ocurrencias} veces en el parrafo o oracion')
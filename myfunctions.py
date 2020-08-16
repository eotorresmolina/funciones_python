
__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import random

def promedio (numeros):
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    if numeros == []:
        return None
    else:
        prom = sum(numeros) / len(numeros)
        return prom


def ordenar (numeros):
    """
    Función que Recibe una lista de Nros.
    Retorna la Lista de Nros. Ordenada de Menor a Mayor
    usando la función sorted()

    """
    if numeros == []:
        return None
    else:
        return sorted(numeros)  # Retorno la Lista Ordenada.


def ordenar_2 (numeros):
    """
    Función que Recibe una lista de Nros.
    Retorna la Lista de Nros. Ordenada de Menor a Mayor
    Usando el método sort().

    """
    numeros.sort(reverse=False)  # Retorno la Lista Ordenada.



def lista_aleatoria (inicio=0, fin=1, cantidad= 1 ):
    """
    Función que Genera una Lista de "cantidad" Nros.
    Aleatorios entre el rango: [inicio, fin]
    """
    # Inicializo la Lista ==> Lista Vacía
    numeros_aleatorios = []
    i = 0

    while i < cantidad:
        numero = random.randrange(inicio, fin+1)
        numeros_aleatorios.append(numero)
        i += 1

    return numeros_aleatorios


def contar (lista_numeros, numero_repetido = 0):
    """
    Función que Recibe una lista de números y un valor
    a contar.
    Retorna la cantidad de veces que aparece dicho valor
    en la lista.
    """
    return lista_numeros.count(numero_repetido)
#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.2"

import random


def imprimir_nombre (nombre, apellido):
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    print('\n\nNombre: {}, Apellido: {}\n\n'.format(nombre, apellido))
    
    # Otra Forma:
    #name ='\n\nNombre: {}, Apellido: {}\n\n'.format(nombre, apellido)
    #print(name)



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



def ej1():
    print('Mi primera función:')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Emmanuel Oscar', 'Torres Molina')

    # Reemplazar por su nombre y apellido los textos


def ej2():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado

    '''
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    # promedio_re
    promedio_re = promedio(numeros)

    # Luego imprimir en pantalla el valor resultante, tal que:
    print('\n\nLista de Números: {}'.format(numeros))

    if promedio_re is None:
        print('\nNo se Pudo Calcular el Promedio. La Lista está Vacía.')
        print('Contiene 0 Elementos.\n\n')

    else:
        print('\nEl Promedio de los Números es: {}\n\n'.format(promedio_re))



def ej3():
    # Ejercicios de listas y métodos
    numeros = [9, 1, 6, 15, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''

    if numeros == []:
        print('\n\nLa Lista Está Vacía. ==> {}\n'.format(numeros))

    else:
        # Luego de crear la función invocarla en este lugar:
        lista_ordenada = ordenar(numeros)

        # Imprimir en pantalla "lista_ordenada" que tendrá
        # los valores retornado por la función ordenar
        print('\n\nLa Lista de Números es: {}'.format(numeros))
        print('\nLa Lista de Números Ordenada de Menor a Mayor es: {}\n'.format(lista_ordenada))


def ej3_bis():
    # Ejercicios de listas y métodos
    numeros = [9, 1, 6, 15, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''

    if numeros == []:
        print('\nLa Lista Está Vacía. ==> {}\n\n'.format(numeros))
        
    else:
        print('\nLa Lista de Números es: {}'.format(numeros))

        # Luego de crear la función invocarla en este lugar:

        # Se Observa que ahora la lista 'números' cambió por ser 
        # un Objeto de tipo 'list'. La función ahora recibe un 
        # parámetro por referencia ==> el Objeto se Modifica.
        ordenar_2(numeros)
        print('\nLa Lista de Números Ordenada de Menor a Mayor es: {}\n\n'.format(numeros))


def ej4():
    # Ejercicios con modulos del sistema

    # Inicialización de las variables
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    # numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''

    # Invocar lista_aleatoria
    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    
    print('\nLa Lista Aleatoria de Nros. dentro del rango [{}, {}] es: {}\n\n'.format(inicio, fin+1, mi_lista_aleatorio))


def ej5():
    # Ejercicios de listas y métodos

    # Inicialización de Variables:
    cantidad_numeros = 5
    inicio = 1
    fin = 9

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''
    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

    lista_numeros = lista_aleatoria(inicio, fin, cantidad_numeros)
    print('\n\nLa Lista Aleatoria Generada es: {}\n'.format(lista_numeros))

    nro_repetido = 3
    cant_veces = contar(lista_numeros, nro_repetido)

    if cant_veces == 0:
        cant_repeticiones = cant_veces
    else:
        cant_repeticiones = cant_veces - 1

    print('La Cantidad de Veces que aparece el Número {} es: {}.'.format(nro_repetido, cant_veces))
    print('La Cantidad de Veces que se Repite el Número {} es: {}\n\n'.format(nro_repetido, cant_repeticiones))


if __name__ == '__main__':
    print("\n\nBienvenidos a otra clase de Inove con Python.\n\n")
    ej1()
    ej2()
    ej3()
    ej3_bis()
    ej4()
    ej5()

#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimientos
adquiridos durante la semana
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.3"


import myfunctions as myf

def ej1():
    print('\nComencemos a crear lo Nuestro!:\n\n')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''
    # Realizo la Importación para este programa haciendo:
    #import myfunctions


def ej2():
    print("Jugando a los dados:")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''

    # Inicialización de Variables:
    min_valor_dado = 1
    max_valor_dado = 6
    cantidad_tiros = 5

    resultados = myf.lista_aleatoria(min_valor_dado, max_valor_dado, cantidad_tiros)
    
    myf.ordenar_2(resultados)
    print('\n\nLos Resultados de los Tiros Ordenados de Menor a Mayor son: {}\n\n'.format(resultados))


def ej3():
    print("Jugando a los dados:")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "contar" para contar cuantas veces aparece:
    a - Cuantas veces aparece el número 1 en su lista de dados tirados
    b - Cuantas veces aparece el número 2 en su lista de dados tirados
    c - Cuantas veces aparece el número 3 en su lista de dados tirados
    d - Cuantas veces aparece el número 4 en su lista de dados tirados
    e - Cuantas veces aparece el número 5 en su lista de dados tirados
    f - Cuantas veces aparece el número 6 en su lista de dados tirados


    2)
    Utilice la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase para ver como se implementa max con esa key

    '''

    # Inicialización de Variables:
    min_valor_dado = 1
    max_valor_dado = 6
    cantidad_tiros = 5

    resultados = myf.lista_aleatoria(min_valor_dado, max_valor_dado, cantidad_tiros)
    print('\n\nLos Resultados de los Tiros son: {}\n'.format(resultados))

    for i in range(min_valor_dado, max_valor_dado + 1):
        cantidad_veces = myf.contar(resultados, i)  # Obtengo la Cant. de Veces que aparece un Número.
        print('La Cantidad de Veces que Aparece el Número {} son: {}'.format(i, cantidad_veces))

    # max(resultados, key=resultados.count) me va a Devolver el 1er Valor que se Repite o Aparece
    #  si hay más de un Valor Máximo.
    max_nro_repetido = max(resultados, key=resultados.count)
    print('\nEl Número Mayor que Más se Repitió en los Tiros es: {}\n\n'.format(max_nro_repetido))

    


def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".
    El enunciado está armado a modo de guía, pueden resolver el problema
    de otra forma.
    Si tienen dudas sobre el enunciado o alguno de los puntos por favor
    comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
    puede haber varias interpretaciones de un mismo enunciado.

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y saca 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitió entre los 5 dados.
    Debe usar la función de Python max con la key de list.count paara
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase o el ejercicio anterior de esta guia.

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole una lista separada
    dados_guardados = [4,4,4]
    Debe realizar un bucle para recorrer la lista de dados_tirados
    y guardar los "4" en nuestra nueva lista dados_guardados
    Utilice append para ir sumando a dados_guardados los valores

    4) Debe volver a tira los dados, generar nuevos
    números aleatorios.
    Si en la lista "dados_guardados" tengo 3 dados guardados
    significa que ahora deberé tirar dos dados. Puede usar la función
    "len" para ver cuantos elementos hay en "dados_guardados"
    Es decir que en este caso debería generar dos números
    aleatorios nuevos con "lista_generica"
    Ahora tendré una nueva lista de "dados_tirados" en este caso
    de dos nuevos números aleatorios entre 1 y 6 representando a los dados
    tirados.

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''


if __name__ == '__main__':
    print("\n\nEjercicios de práctica.\n\n")
    #ej1()
    #ej2()
    ej3()
    # ej4()

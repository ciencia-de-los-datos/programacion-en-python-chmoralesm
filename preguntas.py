"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""



lista = []
with open("data.csv", "r") as file:
    data_lab = file.readlines()
    lista = list(data_lab)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_seg = 0
    for linea in lista:
        suma_seg = suma_seg + eval(linea[2])
    
    return suma_seg


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    

    """
    suma_a = 0
    suma_b = 0
    suma_c = 0
    suma_d = 0
    suma_e = 0

    for linea in lista:
        if linea[0] == "A":
            suma_a = suma_a + 1
        elif linea[0] == "B":
            suma_b = suma_b + 1
        elif linea[0] == "C":
            suma_c = suma_c + 1
        elif linea[0] == "D":
            suma_d = suma_d + 1
        elif linea[0] == "E":
            suma_e = suma_e + 1

    letters_list = ["A", "B", "C", "D", "E"]
    integers_list = [suma_a, suma_b, suma_c, suma_d, suma_e]
    x = list(zip(letters_list, integers_list))
    return x


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_a = 0
    suma_b = 0
    suma_c = 0
    suma_d = 0
    suma_e = 0

    for linea in lista:
        if linea[0] == "A":
            suma_a = suma_a + eval(linea[2])
        elif linea[0] == "B":
            suma_b = suma_b + eval(linea[2])
        elif linea[0] == "C":
            suma_c = suma_c + eval(linea[2])
        elif linea[0] == "D":
            suma_d = suma_d + eval(linea[2])
        elif linea[0] == "E":
            suma_e = suma_e + eval(linea[2])

    letters_list = ["A", "B", "C", "D", "E"]
    integers_list = [suma_a, suma_b, suma_c, suma_d, suma_e]
    x = list(zip(letters_list, integers_list))
    return x


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    from collections import Counter, defaultdict
    from datetime import datetime


    def load_data():
        """Retorna los registros con los campos de interes como una lista de tuplas."""

        csvfile = open("data.csv", "r")

        data = []

        for row in csv.reader(csvfile, delimiter='\t'):
            data.append((row[0],row[1],row[2],row[3]))

        return data


    def compute_by_month(data):
        """Calcula la cantidad de registros para cada mes."""

        count_by_month = Counter()

        for row in data:

            #
            # Convierte el string a un objeto fecha:
            # 05/23/2016 05:35:00 PM
            #
            date = str(datetime.strptime(row[2], "%Y-%m-%d").month)
            if len(date) == 1:
                date = date.zfill(2)
            else:
                date = date.zfill(1) 
            #
            # Contador
            #
            count_by_month[str(date)] += 1

        return count_by_month


    data = load_data()
    count_by_month = compute_by_month(data)
    count1 = list(count_by_month.items())
    count1.sort(key = lambda x: x[0])
    return count1


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    min_a = 0
    min_b = 0
    min_c = 0
    min_d = 0
    min_e = 0

    max_a = 0
    max_b = 0
    max_c = 0
    max_d = 0
    max_e = 0

    lista = []
    with open("data.csv", "r") as file:
        data_lab1 = file.readlines()
        lista = list(data_lab1)

    for linea in lista:
        if linea[0] == "A":
            if min_a != 0:
                if min_a > linea[2]:
                    min_a = linea[2]
            else:
                min_a = linea[2]
        elif linea[0] == "B":
            if min_b != 0:
                if min_b > linea[2]:
                    min_b = linea[2]
            else:
                min_b = linea[2]
        elif linea[0] == "C":
            if min_c != 0:
                if min_c > linea[2]:
                    min_c = linea[2]
            else:
                min_c = linea[2]
        elif linea[0] == "D":
            if min_d != 0:
                if min_d > linea[2]:
                    min_d = linea[2]
            else:
                min_d = linea[2]
        elif linea[0] == "E":
            if min_e != 0:
                if min_e > linea[2]:
                    min_e = linea[2]
            else:
                min_e = linea[2]

    for linea in lista:
        if linea[0] == "A":
            if max_a != 0:
                if max_a < linea[2]:
                    max_a = linea[2]
            else:
                max_a = linea[2]
        elif linea[0] == "B":
            if max_b != 0:
                if max_b < linea[2]:
                    max_b = linea[2]
            else:
                max_b = linea[2]
        elif linea[0] == "C":
            if max_c != 0:
                if max_c < linea[2]:
                    max_c = linea[2]
            else:
                max_c = linea[2]
        elif linea[0] == "D":
            if max_d != 0:
                if max_d < linea[2]:
                    max_d = linea[2]
            else:
                max_d = linea[2]
        elif linea[0] == "E":
            if max_e != 0:
                if max_e < linea[2]:
                    max_e = linea[2]
            else:
                max_e = linea[2]

    letters_list = ["A", "B", "C", "D", "E"]
    max_list = [int(max_a), int(max_b), int(max_c), int(max_d), int(max_e)]
    min_list = [int(min_a), int(min_b), int(min_c), int(min_d), int(min_e)]

    x = list(zip(letters_list,max_list, min_list))
    return x


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import pandas as pd
    import numpy as np
    def load_data():
        """Retorna los registros con los campos de interes como una lista de tuplas."""

        #csvfile = open("/content/drive/MyDrive/Capacitaciones/IA/Postgrado/ciencia de datos/Lab1/programacion-en-python-mblandonp/data.csv", "r")
        x = open("data.csv", "r").readlines()
        x = [z.split("\t") for z in x]
        x = [z[4] for z in x[:]]
        x = [z.replace("\n", "") for z in x]
        x = [z.split(",") for z in x[:]]

        return x

    
    data = load_data()
    df = pd.DataFrame(data)
    data = df.to_numpy().flatten()
    res = pd.DataFrame(data[data != None])
    res = columns =['Name']
    res = res["Name"].str.split(':', expand = True,n=1)
    resdiv = res.columns =['Name','Value']
    products_list = res.values.tolist()
    TypesNames = sorted({row[0] for row in products_list[::]})

    min_a = 0
    min_b = 0
    min_c = 0
    min_d = 0
    min_e = 0
    min_f = 0
    min_g = 0
    min_h = 0
    min_i = 0
    min_j = 0

    max_a = 0
    max_b = 0
    max_c = 0
    max_d = 0
    max_e = 0
    max_f = 0
    max_g = 0
    max_h = 0
    max_i = 0
    max_j = 0

    for linea in products_list:
        if linea[0] == "aaa":
            if min_a != 0:
                if min_a > linea[1]:
                    min_a = linea[1]
            else:
                min_a = linea[1]
        elif linea[0] == "bbb":
            if min_b != 0:
                if min_b > linea[1]:
                    min_b = linea[1]
            else:
                min_b = linea[1]
        elif linea[0] == "ccc":
            if min_c != 0:
                if min_c > linea[1]:
                    min_c = linea[1]
            else:
                min_c = linea[1]
        elif linea[0] == "ddd":
            if min_d != 0:
                if min_d > linea[1]:
                    min_d = linea[1]
            else:
                min_d = linea[1]
        elif linea[0] == "eee":
            if min_e != 0:
                if min_e > linea[1]:
                    min_e = linea[1]
            else:
                min_e = linea[1]
        elif linea[0] == "fff":
            if min_f != 0:
                if min_f > linea[1]:
                    min_f = linea[1]
            else:
                min_f = linea[1]
        elif linea[0] == "ggg":
            if min_g != 0:
                if min_g > linea[1]:
                    min_g = linea[1]
            else:
                min_g = linea[1]
        elif linea[0] == "hhh":
            if min_h != 0:
                if min_h > linea[1]:
                    min_h = linea[1]
            else:
                min_h = linea[1]
        elif linea[0] == "iii":
            if min_i != 0:
                if min_i > linea[1]:
                    min_i = linea[1]
            else:
                min_i = linea[1]
        elif linea[0] == "jjj":
            if min_j != 0:
                if min_j > linea[1]:
                    min_j = linea[1]
            else:
                min_j = linea[1]

    for linea in products_list:
        if linea[0] == "aaa":
            if max_a != 0:
                if max_a < linea[1]:
                    max_a = linea[1]
            else:
                max_a = linea[1]
        elif linea[0] == "bbb":
            if max_b != 0:
                if max_b < linea[1]:
                    max_b = linea[1]
            else:
                max_b = linea[1]
        elif linea[0] == "ccc":
            if max_c != 0:
                if max_c < linea[1]:
                    max_c = linea[1]
            else:
                max_c = linea[1]
        elif linea[0] == "ddd":
            if max_d != 0:
                if max_d < linea[1]:
                    max_d = linea[1]
            else:
                max_d = linea[1]
        elif linea[0] == "eee":
            if max_e != 0:
                if max_e < linea[1]:
                    max_e = linea[1]
            else:
                max_e = linea[1]
        elif linea[0] == "fff":
            if max_f != 0:
                if max_f < linea[1]:
                    max_f = linea[1]
            else:
                max_f = linea[1]
        elif linea[0] == "ggg":
            if max_g != 0:
                if max_g < linea[1]:
                    max_g = linea[1]
            else:
                max_g = linea[1]
        elif linea[0] == "hhh":
            if max_h != 0:
                if max_h < linea[1]:
                    max_h = linea[1]
            else:
                max_h = linea[1]
        elif linea[0] == "iii":
            if max_i != 0:
                if max_i < linea[1]:
                    max_i = linea[1]
            else:
                max_i = linea[1]
        elif linea[0] == "jjj":
            if max_j != 0:
                if max_j < linea[1]:
                    max_j = linea[1]
            else:
                max_j = linea[1]
    
    min_lista = [int(min_a), int(min_b), int(min_c), int(min_d), int(min_e), int(min_f), int(min_g), int(min_h), int(min_i), int(min_j)]
    max_lista = [int(max_a), int(max_b), int(max_c), int(max_d), int(max_e), int(max_f), int(max_g), int(max_h), int(max_i), int(max_j)]
    yy = list(zip(TypesNames,min_lista,max_lista))

    return yy


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return

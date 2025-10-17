from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta):
    res = []
    with open(ruta, encoding= "utf-8") as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            # año = int(año) o bien ponerlo abajo
            # censo = int(censo)
            res.append(RegistroPoblacion(pais, codigo, int(año), int(censo)))
    return res


def calcula_paises(lista):
    res = set() #conjuntos para cuando te piden que no se repitan
    regiones = {
    'Arab World', 'World', 'Europe & Central Asia', 'Euro area',
    'Sub-Saharan Africa', 'Middle East & North Africa', 'Middle East & North Africa (IDA & IBRD countries)',
    'Latin America & Caribbean', 'East Asia & Pacific', 'Middle East & North Africa (excluding high income)',
    'North America', 'South Asia', 'Central Europe and the Baltics', 'Sub-Saharan Africa (excluding high income)', 'Sub-Saharan Africa (IDA & IBRD countries)'}

    for elemento in lista:
        if elemento.pais not in regiones:
            res.add(elemento.pais) #añadir elemento a conjunto
    return sorted(res) 
"""
#o bien
    paises = {r.pais for r in poblaciones if r.pais not in regiones}
    return sorted(paises)
"""
        

def filtra_por_paises(lista, nombre_o_codigo):
    res = []
    for i in lista:
        if nombre_o_codigo == i.pais or nombre_o_codigo == i.codigo:
            res.append((i.año, i.censo))
    return res



def filtra_por_paises_y_anyo(lista, anyo, paises):
    res = []
    for registro in lista:
        if registro.año == anyo and registro.pais in paises:
            res.append((registro.pais, int(registro.censo)))
    return res





def muestra_evolucion_poblacion(lista):
    nombre_o_codigo = input("Introduce un nombre o codigo de pais: ")
    res = filtra_por_paises(lista, nombre_o_codigo)

    lista_años = [i[0] for i in res]       # todos los años
    lista_habitantes = [i[1] for i in res] # todos los censos


    titulo = f"Evolución población de {nombre_o_codigo}"
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes, marker='o')
    plt.xlabel("Año")
    plt.ylabel("Habitantes")
    plt.show()



def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    res = filtra_por_paises_y_anyo(poblaciones, anyo, paises)

    if not res:
        print("No hay datos para esos países en ese año.")
        return

    res.sort(key=lambda x: x[0])  # ordenar por nombre de país

    lista_paises = [i[0] for i in res]
    lista_habitantes = [i[1] for i in res]

    plt.title(f"Comparación de población en {anyo}")
    plt.bar(lista_paises, lista_habitantes)
    plt.xlabel("Países")
    plt.ylabel("Habitantes")
    plt.show()









if __name__ == "__main__":

    lista = lee_poblaciones("data\population.csv")
    # print(lista)

    # print(f"Países: {calcula_paises(lista)}")

    # pais_codigo = input("Introduce un nombre o codigo de pais: ") #.upper()
    # print(f"El censo y año del pais/codigo {pais_codigo} es {filtra_por_paises(lista, pais_codigo)}")

    paises = {"Spain" , "Peru"}
    año = int(1980)
    # print(f"Estos son los habitantes de los paises {paises} en el año {año}, son: {filtra_por_paises_y_anyo(lista, año, paises)}")

    # muestra_evolucion_poblacion(lista)

    muestra_comparativa_paises_anyo(lista, año, paises)

import pandas as pd
import numpy as np
import statistics as stat

"Se carga el archivo csv"
datos = pd.read_csv('cunorte2_app.csv', index_col = 0)
print(datos)

"Se separan los datos conjunto de eventos"
label_A: object = datos.loc['A']
label_B: object = datos.loc['B']
label_C: object = datos.loc['C']
label_D: object = datos.loc['D']
label_E: object = datos.loc['E']


"Se crean los vectores con los valores no vacios de cada criterio"
count_lA = label_A.count(0)
count_1B = label_B.count(0)
count_1C = label_C.count(0)
count_1D = label_D.count(0)
count_1E = label_E.count(0)

"Se calculan los porcentajes (1A,B,C,D,E) de los criterios en cada evento"

def totalesA(criterios1):
    total_a = 0
    i = 1
    for i in criterios1[i:]:
        total_a = total_a + i
    return total_a

def totalesB(criterios2):
    total_b = 0
    i = 1
    for i in criterios2[i:]:
        total_b = total_b + i
    return total_b

def totalesC(criterios3):
    total_c = 0
    i = 1
    for i in criterios3[i:]:
        total_c = total_c + i
    return total_c

def totalesD(criterios4):
    total_d = 0
    i = 1
    for i in criterios4[i:]:
        total_d = total_d + i
    return total_d

def totalesE(criterios5):
    total_e = 0
    i = 1
    for i in criterios5[i:]:
        total_e = total_e + i
    return total_e

pc1A = count_lA / totalesA(count_lA)
pc1B = count_1B / totalesB(count_1B)
pc1C = count_1C / totalesC(count_1C)
pc1D = count_1D / totalesD(count_1D)
pc1E = count_1E / totalesE(count_1E)


"Se calculan las medias geométricas de los criterios en cada evento"

med_a: object = label_A.mean()
med_b: object = label_B.mean()
med_c: object = label_C.mean()
med_d: object = label_D.mean()
med_e: object = label_E.mean()

print(med_a)


"Programa de prueba"
"Comentario de prueba número 2"

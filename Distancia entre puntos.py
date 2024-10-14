import random
import math
import time

def generar_puntos(n):
    return [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(n)]

def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def par_mas_cercano(puntos):
    min_dist = float('inf')
    punto1, punto2 = None, None
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            dist = distancia(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
                punto1, punto2 = puntos[i], puntos[j]
    return punto1, punto2, min_dist

def ejecutar_experimento(valores_n):
    for n in valores_n:
        puntos = generar_puntos(n)
        start_time = time.time()
        p1, p2, dist = par_mas_cercano(puntos)
        end_time = time.time()
        print(f"n = {n}: El par de puntos más cercano es {p1} y {p2} con una distancia de {dist:.4f}")
        print(f"Lista de coordenadas generadas: {puntos}")
        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos\n")

valores_n = [10, 100, 1000, 10000, 100000]
ejecutar_experimento(valores_n)

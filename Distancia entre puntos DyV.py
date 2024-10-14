import random
import math
import time

def generar_puntos(n):
    return [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(n)]

def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def distancia_minima_strip(strip, d):
    min_dist = d
    strip.sort(key=lambda punto: punto[1])  # Ordena por coordenada y
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            dist = distancia(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def par_mas_cercano_recursivo(puntos):
    if len(puntos) <= 3:
        min_dist = float('inf')
        for i in range(len(puntos)):
            for j in range(i + 1, len(puntos)):
                dist = distancia(puntos[i], puntos[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    mid = len(puntos) // 2
    punto_medio = puntos[mid]
    
    dl = par_mas_cercano_recursivo(puntos[:mid])
    dr = par_mas_cercano_recursivo(puntos[mid:])
    
    d = min(dl, dr)
    
    strip = [punto for punto in puntos if abs(punto[0] - punto_medio[0]) < d]
    
    return min(d, distancia_minima_strip(strip, d))

def par_mas_cercano(puntos):
    puntos.sort(key=lambda punto: punto[0])  # Ordena por coordenada x
    return par_mas_cercano_recursivo(puntos)

def ejecutar_experimento(valores_n):
    for n in valores_n:
        puntos = generar_puntos(n)
        start_time = time.time()
        dist = par_mas_cercano(puntos)
        end_time = time.time()
        print(f"n = {n}: La distancia más cercana es {dist:.4f}")
        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos\n")

valores_n = [10, 100, 1000, 10000, 100000]
ejecutar_experimento(valores_n)

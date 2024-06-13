import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))


def movimiento_valido(fila, columna, tablero):
    if fila >= 0 and fila < len(tablero) and columna >= 0 and columna < len(tablero):
        if tablero[fila][columna] != 'G': 
            return True
    return False


def distancia_gato_raton(fila_gato, columna_gato, fila_raton, columna_raton):
    return abs(fila_gato - fila_raton) + abs(columna_gato - columna_raton)

def distancia_raton_madriguera(fila_raton, columna_raton, fila_madriguera, columna_madriguera):
    return abs(fila_raton - fila_madriguera) + abs(columna_raton - columna_madriguera)


def funcion_evaluacion(fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera):
    distancia_gato_raton_valor = distancia_gato_raton(fila_gato, columna_gato, fila_raton, columna_raton)
    distancia_raton_madriguera_valor = distancia_raton_madriguera(fila_raton, columna_raton, fila_madriguera, columna_madriguera)
    return distancia_gato_raton_valor - distancia_raton_madriguera_valor


def minimax(tablero, fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera, profundidad, maximizando_raton):
    if profundidad == 0 or (fila_gato == fila_raton and columna_gato == columna_raton) or (fila_raton == fila_madriguera and columna_raton == columna_madriguera):
        return funcion_evaluacion(fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera), None

    if maximizando_raton:
        max_eval = float('-inf')
        mejor_movimiento = None
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for movimiento in movimientos:
            nueva_fila_raton = fila_raton + movimiento[0]
            nueva_columna_raton = columna_raton + movimiento[1]
            
            if movimiento_valido(nueva_fila_raton, nueva_columna_raton, tablero):
                eval, _ = minimax(tablero, fila_gato, columna_gato, nueva_fila_raton, nueva_columna_raton, fila_madriguera, columna_madriguera, profundidad - 1, False)
                if eval > max_eval:
                    max_eval = eval
                    mejor_movimiento = (nueva_fila_raton, nueva_columna_raton)
        
        return max_eval, mejor_movimiento
    
    else:
        min_eval = float('inf')
        mejor_movimiento = None
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for movimiento in movimientos:
            nueva_fila_gato = fila_gato + movimiento[0]
            nueva_columna_gato = columna_gato + movimiento[1]
            
            if movimiento_valido(nueva_fila_gato, nueva_columna_gato, tablero):
                eval, _ = minimax(tablero, nueva_fila_gato, nueva_columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera, profundidad - 1, True)
                if eval < min_eval:
                    min_eval = eval
                    mejor_movimiento = (nueva_fila_gato, nueva_columna_gato)
        
        return min_eval, mejor_movimiento
    

def mover_gato_minimax(tablero, fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera):
    _, mejor_movimiento = minimax(tablero, fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera, profundidad=3, maximizando_raton=False)
    if mejor_movimiento:
        nueva_fila_gato, nueva_columna_gato = mejor_movimiento
        tablero[fila_gato][columna_gato] = '-'
        tablero[nueva_fila_gato][nueva_columna_gato] = 'G'
        return nueva_fila_gato, nueva_columna_gato
    return fila_gato, columna_gato

def mover_raton_minimax(tablero, fila_raton, columna_raton, fila_madriguera, columna_madriguera, fila_gato, columna_gato):
    _, mejor_movimiento = minimax(tablero, fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera, profundidad=3, maximizando_raton=True)
    if mejor_movimiento:
        nueva_fila_raton, nueva_columna_raton = mejor_movimiento
        tablero[fila_raton][columna_raton] = '-'
        tablero[nueva_fila_raton][nueva_columna_raton] = 'R'
        return nueva_fila_raton, nueva_columna_raton
    return fila_raton, columna_raton


def colocar_madriguera(tablero, tamaño_tablero):
    fila_madriguera = random.randint(0, tamaño_tablero - 1)
    columna_madriguera = random.randint(0, tamaño_tablero - 1)
    while tablero[fila_madriguera][columna_madriguera] != '-': 
        fila_madriguera = random.randint(0, tamaño_tablero - 1)
        columna_madriguera = random.randint(0, tamaño_tablero - 1)
    return fila_madriguera, columna_madriguera


def juego():
    tamaño_tablero = 5
    tablero = [['-' for tcolumna in range(tamaño_tablero)] for tfila in range(tamaño_tablero)]

    fila_gato = random.randint(0, tamaño_tablero - 1)
    columna_gato = random.randint(0, tamaño_tablero - 1)
    fila_raton = random.randint(0, tamaño_tablero - 1)
    columna_raton = random.randint(0, tamaño_tablero - 1)
    fila_madriguera, columna_madriguera = colocar_madriguera(tablero, tamaño_tablero)

    tablero[fila_gato][columna_gato] = 'G'
    tablero[fila_raton][columna_raton] = 'R'
    tablero[fila_madriguera][columna_madriguera] = 'M'

    turnos = 0
    while turnos < 10:  
        turnos += 1
        print(f"Turno {turnos}")
        if turnos % 2 == 1:
            print("Turno del Ratón:")
            fila_raton, columna_raton = mover_raton_minimax(tablero, fila_raton, columna_raton, fila_madriguera, columna_madriguera, fila_gato, columna_gato)
            imprimir_tablero(tablero)
            print()
            if fila_raton == fila_madriguera and columna_raton == columna_madriguera:
                print("El ratón se escapó")
                return 
        else:
            print("Turno del Gato:")
            fila_gato, columna_gato = mover_gato_minimax(tablero, fila_gato, columna_gato, fila_raton, columna_raton, fila_madriguera, columna_madriguera)
            imprimir_tablero(tablero)
            print()
            if fila_gato == fila_raton and columna_gato == columna_raton:
                print("El gato atrapó al ratón")
                return
    print("Empate")

juego()

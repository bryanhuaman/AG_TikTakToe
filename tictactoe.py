"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


''''Implementar estas funciones'''

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = 0
    count_o = 0
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if board[i][j] == X:
                count_x = count_x + 1
            if board[i][j] == O:
                count_o = count_o + 1
    if count_x == count_o:
        return X
    else:
        return O

def actions(board):
    casilla_vacia = set()
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila): # valor : representa el valor especifico de cada casilla
            if valor == EMPTY:
                casilla_vacia.add((i,j))
    return casilla_vacia

import copy
def result(board, action):
    if action not in actions(board):
        raise Exception("Movimiento ilegal")
    i, j = action
    ficha = player(board)
    nuevo = copy.deepcopy(board)
    nuevo[i][j] = ficha
    return nuevo


def winner(board):
    """
    Returns the winner of the game, if there is one.
    se tiene que contar las posibilidades de opciones de ganar
    """
    lineas = [
        # filas
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # columnas
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonales
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for linea in lineas:
        if linea[0] == linea[1] == linea[2] and linea[0] is not None:
            return linea[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    si se puede seguir jugando, si no hat moviminetos posibles terminaria el juego
    """
    if winner(board) is not None:
        return True
    # si hay casillas_vacias retorna true, sino termina el juego
    return len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ganador = winner(board)
    if ganador is not None:
        if 'X' == ganador:
            return 1
        elif 'O' == ganador:
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # si el juego acabo = TRUE
    if terminal(board):
        return None
    # a quien le toca el turno
    turno = player(board)


    def max_valor(board):
        if terminal(board): 
            return utility(board) # si el juego termino retorna el puntaje (1 , -1, 0)
        v = -math.inf # peor valor posible para MAX
        for accion in actions(board):
            v = max(v, min_valor(result(board, accion)))
        return v

    def min_valor(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for accion in actions(board):
            v = min(v, max_valor(result(board, accion)))
        return v

    mejor_accion = None
    if turno == X:
        mejor_valor = -math.inf
        for accion in actions(board):
            v = min_valor(result(board, accion))
            if v > mejor_valor:
                mejor_valor = v
                mejor_accion = accion
    else:
        mejor_valor = math.inf
        for accion in actions(board):
            v = max_valor(result(board, accion))
            if v < mejor_valor:
                mejor_valor = v
                mejor_accion = accion

    print(mejor_valor)
    return mejor_accion

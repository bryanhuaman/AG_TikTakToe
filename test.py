import tictactoe as ttl

b2 = ttl.initial_state()
b2[0][0] = 'X'
b2[0][1] = 'O'


print(ttl.player(b2))


print("Prueba casillas libres")

b3 = [['X', 'O', None],
      [None, 'X', None],
      [None, None, None]]
print(ttl.actions(b3))

print("Resultados Tres en raya")
b5 = ttl.initial_state()
nuevo = ttl.result(b5,(0,0))
print(nuevo[0][0])

print("Saber el ganador")
print(ttl.winner(b3))

b4 = [['X', 'O', 'X'],
      ['O', 'O', 'X'],
      ['X', 'X', 'O']]

print("Prueba Terminal")
print(ttl.terminal(b4))


print("Prueba utility")
print(ttl.utility(b4))
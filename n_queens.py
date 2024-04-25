from queue import Queue
import time

class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_bfs(self):
        if self.size < 1:
            return None  # Retorna None se o tamanho for inválido

        queue = Queue()
        queue.put(([]))
        nodes_explored = 0  
        iterations = 0  

        while not queue.empty():
            solution = queue.get() #Retira-se o 1º estado(lista de coordendas das rainhas) da fila
            if self.conflict(solution): #Chama a funçao para verificar conflitos
                continue
            row = len(solution) #Número da linha e numero de rainhas posicionadas
            if row == self.size:
                
                return (solution, iterations, nodes_explored) # Retorna a solução encontrada e as informações de iteração e nós explorados

            for col in range(self.size): # Para cada coluna, posiciona 1 rainha
                queen = (row, col) #Coordenadas
                queens = solution.copy() #Copia a solução atual
                queens.append(queen) #Adiciona a rainha na solução parcial
                queue.put((queens)) #Adiciona no final da fila
                nodes_explored += 1  # Incrementa o contador de nós explorados (configurações de tabuleiro geradas)
            iterations += 1  # Incrementa o contador de iterações (Quantas vezes passou-se pelo ciclo de execução)

        return None  # Retorna None se nenhuma solução for encontrada

    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print_board(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)

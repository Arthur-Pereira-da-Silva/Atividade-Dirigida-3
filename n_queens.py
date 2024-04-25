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
        nodes_explored = 0  # Contador de nós explorados
        iterations = 0  # Contador do número de iterações

        while not queue.empty():
            solution = queue.get()
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                # Retorna a solução encontrada e as informações de iteração e nós explorados
                return (solution, iterations, nodes_explored)

            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.put((queens))
                nodes_explored += 1  # Incrementa o contador de nós explorados
            iterations += 1  # Incrementa o contador de iterações

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

from queue import Queue
import time

class NQueens:

    def __init__(self, tamanho):
        self.tamanho = tamanho

    def solucao_bfs(self):
        if self.tamanho < 1:
            return None  # Retorna None se o tamanho for inválido

        queue = Queue()
        queue.put(([]))
        nos_explorados = 0  
        iteracoes = 0  

        while not queue.empty():
            solucao = queue.get() #Retira-se o 1º estado(lista de coordendas das rainhas) da fila
            if self.verifica_conflito(solucao): #Chama a funçao para verificar conflitos
                continue
            linha = len(solucao) #Número da linha e numero de rainhas posicionadas
            if linha == self.tamanho:
                
                return (solucao, iteracoes, nos_explorados) # Retorna a solução encontrada e as informações de iteração e nós explorados

            for col in range(self.tamanho): # Para cada coluna, posiciona 1 rainha
                rainha = (linha, col) #Coordenadas
                rainhas = solucao.copy() #Copia a solução atual
                rainhas.append(rainha) #Adiciona a rainha na solução parcial
                queue.put((rainhas)) #Adiciona no final da fila
                nos_explorados += 1  # Incrementa o contador de nós explorados (configurações de tabuleiro geradas)
            iteracoes += 1  # Incrementa o contador de iterações (Quantas vezes passou-se pelo ciclo de execução)

        return None  # Retorna None se nenhuma solução for encontrada

    def verifica_conflito(self, rainhas):
        for i in range(1, len(rainhas)):
            for j in range(0, i):
                a, b = rainhas[i]
                c, d = rainhas[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def mostra_tabuleiro(self, rainhas):
        for i in range(self.tamanho):
            print(' ---' * self.tamanho)
            for j in range(self.tamanho):
                p = 'Q' if (i, j) in rainhas else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.tamanho)

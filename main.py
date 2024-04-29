from n_queens import NQueens
import time


def main():
    print('.: Problema N-Queens:.')
    tamanho = int(input('Por favor, insira o tamanho do tabuleiro: '))

    n_queens = NQueens(tamanho)
    start_time = time.time()
    bfs_solucao = n_queens.solucao_bfs()
    end_time = time.time()

    if bfs_solucao:
        solucao, iteracoes, nos_explorados = bfs_solucao
        print('Solução encontrada:')
        n_queens.mostra_tabuleiro(solucao)
        
        print('\nInformações da busca não informada:')
        print('{:<10} {:<20} {:<30} {:<20}'.format('Iteração', 'Solução encontrada', 'Número de nós (memória)', 'Tempo de processamento'))
        print('{:<10} {:<20} {:<30} {:<20}'.format(iteracoes, 'Sim', nos_explorados, '{:.4f} ms'.format((end_time - start_time) * 1000)))
    else:
        print('Nenhuma solução encontrada para o tamanho do tabuleiro fornecido.')

if __name__ == '__main__':
    main()
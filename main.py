from n_queens import NQueens
import time


def main():
    print('.: N-Queens Problem :.')
    size = int(input('Por favor, insira o tamanho do tabuleiro: '))
    print_solution = input('Deseja imprimir a solução encontrada (S/N): ').lower() == 's'

    n_queens = NQueens(size)
    start_time = time.time()
    bfs_solution = n_queens.solve_bfs()
    end_time = time.time()

    if bfs_solution:
        solution, iterations, nodes_explored = bfs_solution
        print('Solução encontrada:')
        n_queens.print_board(solution)
        
        # Imprimir informações da busca não informada
        print('\nInformações da busca não informada:')
        print('{:<10} {:<20} {:<30} {:<20}'.format('Iteração', 'Solução encontrada', 'Número de nós (memória)', 'Tempo de processamento'))
        print('{:<10} {:<20} {:<30} {:<20}'.format(iterations, 'Sim', nodes_explored, '{:.4f} ms'.format((end_time - start_time) * 1000)))
    else:
        print('Nenhuma solução encontrada para o tamanho do tabuleiro fornecido.')

if __name__ == '__main__':
    main()
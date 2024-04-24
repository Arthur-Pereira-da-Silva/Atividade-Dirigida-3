from n_queens import NQueens
import time


def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    start_time = time.time()
    bfs_solutions = n_queens.solve_bfs()
    end_time = time.time()
    bfs_solutions = n_queens.solve_bfs()
    if print_solutions:
        for i, solution in enumerate(bfs_solutions):
            print('BFS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total BFS solutions: %d' % len(bfs_solutions))
    execution_time = end_time - start_time
    print('Execution time: %.2f seconds' % execution_time)


if __name__ == '__main__':
    main()

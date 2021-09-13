from function import *



number_of_iterations = 0
number_of_moves = 0

iterations_tmp, moves_tmp = solve_queen_forword_checking(size)
number_of_iterations += iterations_tmp
number_of_moves += moves_tmp

print('number of moves: ', number_of_moves, ' number of iteration : ', number_of_iterations)

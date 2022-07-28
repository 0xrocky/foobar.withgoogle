# imports
import numpy as np
# global variables
# memoization
memo = {}
# chessboard of 8x8
chessboard = [ [ ( row*8 ) + col for col in range( 8 ) ] for row in range( 8 ) ]
# incidence matrix of chessboard of 64*64
A = [ [ 0 for col in range( 64 ) ] for row in range( 64 ) ]
# populating the A matrix of incidence
for cell in range( 64 ):
    # retrieving the coordinates of the chessboard integer number of the cell considered
    x_cell, y_cell = cell//8, cell%8
    # eight legitimate L-moves in the chessboard
    eligible_moves = [ ( x_cell + 2, y_cell + 1 ), ( x_cell + 2, y_cell - 1 ), ( x_cell + 1, y_cell + 2 ), ( x_cell + 1, y_cell - 2 ), ( x_cell - 1, y_cell + 2 ), ( x_cell - 1, y_cell - 2 ), ( x_cell - 2, y_cell + 1 ), ( x_cell - 2, y_cell - 1 ) ]
    # boundaries check in the chessboard: x-coordinate = move[ 0 ] and y-coordinate = move[ 1 ]
    eligible_moves = [ move for move in eligible_moves if move[ 0 ] in range( 8 ) and move[ 1 ] in range( 8 ) ]
    # from the eligible_moves of the chessboard, computing all the results of the eligible moves from each source to each destination in the incidence matrix A
    eligible_moves = [ ( cell, move[ 0 ]*8 + move[ 1 ] ) for move in eligible_moves ]
    # setting a move for destination from source in A
    for src, dest in eligible_moves:
        A[ src ][ dest ] = 1
    
def solution(src, dest):
    global A, chessboard, memo
    #Your code here
    # input constraints
    assert type( src ) == int and type( dest ) == int and all( [ x in range( 64 ) for x in [ src, dest ] ] )
    # if source coincides with destination, don't move
    if src == dest:
        return 0
    # solution: exponent of A_pow, i.e. number of moves
    exponent = 1
    A_pow = np.copy( A )
    memo[ 1 ] = np.copy( A_pow )
    while( True ):
        # return the minimum number of L-moves for which destination can be reached from source
        if A_pow[ src ][ dest ] > 0:
            return exponent
        # increment of exponent
        exponent += 1
        # memoization: if the result of the multiplication of the incidence matrix has not yet been computed, then calculate and store it 
        if exponent not in memo.keys():
            A_pow = np.matmul( A, A_pow )
            memo[ exponent ] = np.copy( A_pow )
        else:
            A_pow = memo[ exponent ]
       	# exit strategy because of infinite loop
        if all( [ sum( row ) == sum( [ 0 for i in range( len( A_pow[ 0 ] ) ) ] ) for row in A_pow ] ):
            return False

def solution( data, n ): 
    # Your code here
    # input checks
    if len( data ) > 100:
        print('data too long!')
        return -1
    if type( n ) != int or n < 0:
        print( 'n not valid!' )
        return -1
    sol = []
    # list comprehension to populate the solution array, considering those ID in data occuring more than n
    sol = [ ID for ID in data if data.count( ID ) >= n ]
    return sol

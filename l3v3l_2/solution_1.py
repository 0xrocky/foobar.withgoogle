########################
###### My Example ######
### "--->-><-><-->-" ###
###     A BZ CY  D   ###
###                  ###
### A: Z,Y = 2       ###
### B: Z,Y = 2       ###
### C: Y = 1         ###
###                  ###
### Z: B,A = 2       ###
### Y: A,B,C = 3     ###
########################
def solution(s):
    # Your code here
    # input costraints
    assert all( [ ch in "<->" for ch in s ] ) and len( s ) > 0 and len( s ) < 101
    
    # counter at the end of the loop will be the total number of salutes
    counter = 0
    
    # the loop iterates over the indeces of s
    for i in range( len( s ) ):
        # current character
        ch = s[ i ]
        # neutral case
        if ch == '-':
            continue
        # dx (>) and sx (<) cases
        start = i + 1 if ch == '>' else i - 1
        # if start overflows the boundaries of s, stop for this char
        if start < 0 or start > len( s ) - 1:
            continue
        # end is always a "static" point, at the start or the end of the string
        end = len( s ) - 1 if ch == '>' else 0
        # end must be always greater than start, in order to build the substring of s where the opposite chars resides
        start, end = ( end, start ) if start > end else ( start, end )
        # opposite char of ch
        opps = '<' if ch == '>' else '>'
        # starting from the substring s[ start:end +1 ], the substring of only opposite chars is considered, extracting its lenght
        counter += len( [ chss for chss in s[ start:end +1 ] if chss == opps ] )
    return counter

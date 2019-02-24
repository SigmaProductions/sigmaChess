def piecePath(x, y, boardArray, coordHorizontal, coordVert):
    if coordHorizontal - x == 0:
        return xIsZero(y, boardArray, coordHorizontal, coordVert)
    if coordVert - y == 0:
        return yIsZero(x, boardArray,coordHorizontal, coordVert)
    else:
        return linearFunction(x, y, boardArray, coordHorizontal, coordVert)


def xIsZero(y, boardArray, coordHorizontal, coordVert):
    if y >= coordVert:
        high = y
        low = coordVert
    else:
        low = y
        high = coordVert
    for squarey in range(low+1, high):
        if boardArray[coordHorizontal][squarey] is not None:
            return False
    return True


def yIsZero(x, boardArray,coordHorizontal, coordVert):
    if x >= coordHorizontal:
        high = x
        low = coordHorizontal
    else:
        low = x
        high = coordHorizontal
    for squarex in range(low+1, high):
        if boardArray[squarex][coordVert] is not None:
            return False
    return True


def linearFunction(x,y, boardArray, coordHorizontal, coordVert):
    a = int((coordHorizontal - x) / (coordVert - y))
    b = int(y - (x * a))

    if x >= coordHorizontal:
        high = x
        low = coordHorizontal
    else:
        high = coordHorizontal
        low = x

    for squarex in range(low + 1, high):
        squarey = squarex * a + b
        if squarex>7 or squarey>7 or squarex<0 or squarey<0:
            '''In case of emergency break glass'''
            '''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'''
            return 'wypierdalaj'
        '''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'''
        if boardArray[squarex][squarey] is not None:
            return False
    return True
def printBoard(N):

    myCheck = True
    for i in range(N):
        for j in range(N):
            if myCheck:
                print ("W", end=" ")
                myCheck = False
            else:
                print ("B", end=" ")
                myCheck = True
        print()
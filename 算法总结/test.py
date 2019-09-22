def findMinMoves(machines):

    if len(machines) < 1:
        return -1

    size = len(machines)
    Sum = 0

    for i in range (size):
        Sum += machines[i]
        print(Sum)

    if Sum % size != 0:
        return -1

    avg = Sum / size
    leftsum,res= 0,0
    
    for i in range (size):
        L = i * avg -leftsum
        R = (size - i - 1 ) * avg -(Sum - leftsum - machines[i])

        if L>0 and R>0 :
            res = max(L+R,res)
        else:
            res = max(max(abs(L),abs(R)),res)

        leftsum += machines[i]
    
    return res

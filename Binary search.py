def BubbleSearch(A,item):

    low =0
    high = len(A) -1
    com =0
    while low <= high:
        com +=1
        mid = (high + low) // 2
        if item == A[mid] or mid == 0:
            print 'No Of computations :',com
            return mid
        elif item > A[mid]:
            low = mid+1
        else:
            high = mid-1
    return com
A=[item for item in range(0,10000000,2)]
print BubbleSearch(A,10000000)

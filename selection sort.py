def selectionSort(A):
    total=0
    for i in range(len(A)):
        least =i
        for k in range(i+1,len(A)):
            if A[k] < A[least]:
                #swap
                total +=1
                A[i],A[k]=A[k],A[i]
    print 'No Of Swaps :',total

A=[1,2,3,4,5,6]
selectionSort(A)
print A

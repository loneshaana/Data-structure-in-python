
def Merge(a,b):
    """ Function to merge two arrays """
#    print "Left List :",a
#    print "_____________________________"
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def MergeSort(arr):
    if len(arr) == 0 or len(arr)==1:
        return arr
    else:
        mid = len(arr) // 2
        a = MergeSort(arr[:mid])
        b = MergeSort(arr[mid:])
        return Merge(a,b)
arr=range(10000,0,-1)
# 5,4,3,2,1
print MergeSort(arr)

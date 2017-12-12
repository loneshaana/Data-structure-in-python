def QuickSort(arr,start,end):
    if start < end:
        split = partition(arr,start,end)
        QuickSort(arr,start,split-1)
        QuickSort(arr,split+1,end)

def partition(arr,start,end):
    pivot = arr[start]
    leftmark =start+1
    rightmark = end
    while leftmark < rightmark:
        found = False
        if arr[leftmark] >= pivot:
            while not found and rightmark >= leftmark:
                if arr[rightmark] < pivot:
                    found = True
                    swap(arr,leftmark,rightmark)
                    rightmark = rightmark-1
                else:
                    rightmark = rightmark-1
        else:
            leftmark = leftmark + 1
        leftmark = leftmark+1
    swap(arr,start,rightmark)
    return rightmark

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = range(10000,0,-1)
l=len(arr)-1
QuickSort(arr,0,len(arr)-1)
print arr

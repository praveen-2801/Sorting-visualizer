import time
from colors import *

def quick_sort(A,low,high,drawData,timeTick):

    if(low<high):
        pindex = partition(A,low,high,drawData,timeTick)
        quick_sort(A,low,pindex-1,drawData,timeTick)
        quick_sort(A,pindex+1,high,drawData,timeTick)
        drawData(A, [PURPLE if x >= low and x < pindex else YELLOW if x == pindex else DARK_BLUE if x > pindex and x <=high else BLUE for x in range(len(A))])
        time.sleep(timeTick)
    
    drawData(A, [BLUE for x in range(len(A))])


def partition(A,low,high,drawData,timeTick):
    
    i=low+1
    pivot = A[low]
    for j in range(low+1,high+1):
        if A[j]<pivot:
            A[i],A[j] = A[j],A[i]
            i+=1
    A[low],A[i-1] = A[i-1],A[low]
    return i-1
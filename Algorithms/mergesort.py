import time

from colors import *


def merge(data,l,h,mid,drawData,timeTick):
    tempArray = []
    p=l
    q=mid+1
    
    for i in range(l, h+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > h:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1
    
    for i in range(len(tempArray)):
        data[l] = tempArray[i]
        l+=1

def merge_sort(data,low,high,drawData,timeTick):

    if low<high:
        mid = (low+high)//2
        merge_sort(data,low,mid,drawData,timeTick)
        merge_sort(data,mid+1,high,drawData,timeTick)
        merge(data,low,high,mid,drawData,timeTick)

        drawData(data, [PURPLE if x >= low and x < mid else YELLOW if x == mid else DARK_BLUE if x > mid and x <=high else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

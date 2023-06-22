def searchIter(arr, x):
    for  i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1

def searchRec(arr, curr, x):
    if curr == -1:
        return -1
    elif arr[curr] == x:
        return curr
    return searchRec(arr, curr-1, x)

arr = [1,3,5,2,6,8,4]
x = 5
print(searchIter(arr,x))
print(searchRec(arr, len(arr)-1, x))
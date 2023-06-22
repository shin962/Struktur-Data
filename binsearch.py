def searchIter(arr,x):
    awal = 0 
    tengah = 0
    akhir = len(arr)-1
    while awal <= akhir:
        tengah = (awal+akhir)//2
        if arr[tengah] < x:
            awal = tengah+1
        elif arr[tengah] > x:
            akhir = tengah-1
        else:
            return tengah
    return -1
def searchRec(arr,awal,akhir,x):
    if akhir >= awal:
        tengah = (awal+akhir)//2
        if arr[tengah] == x:
            return tengah
        elif arr[tengah] > x:
            return searchRec(arr,awal,tengah-1,x)
        else:
            return searchRec(arr,tengah+1,akhir,x)
    else:
        return -1
arr = [1,2,4,5,6,8,9,10]
x = 2
print(searchIter(arr,x))
print(searchRec(arr,0,len(arr)-1,x))
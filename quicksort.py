def partition(list, bwh, atas): #fungsi untuk meletakkan pivot pada tempat yang benar
    pivot = list[bwh]
    x = bwh + 1
    for i in range(bwh+1,atas):
        if list[i] < pivot:
            list[x], list[i] = list[i], list[x]
            x += 1
    list[x-1],list[bwh] = list[bwh],list[x-1]
    return x+1

def quicksort(list, bwh, atas): # fungsi untuk melakukan quicksort
    if bwh < atas:
        pi = partition(list, bwh, atas)
        quicksort(list, bwh, pi - 1)
        quicksort(list, pi + 1, atas)

list = [5,2,8,4,7,3,9] #inputan
print("Unsorted Array")
print(list)
size = len(list)
quicksort(list, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(list)

def inSort(angka):
    for i in range(1,len(angka)):
        key = angka[i]
        j = i-1      
        while j >= 0 and key < angka[j]:
            angka[j+1] = angka[j]
            angka[j] = key
            j -= 1
            
angka = [2,4,9,6,8,3]
inSort(angka)
print(angka)
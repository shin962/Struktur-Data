def bSort(angka):
    for i in range(len(angka)-1,0,-1):
        for j in range(i):
            if angka[j] > angka[j+1]:
                temp = angka[j]
                angka[j] = angka[j+1]
                angka[j+1] = temp
angka = [10,5,2,8,7,3]
bSort(angka)
print(angka)
def mgsort(list):
    jumlah_bilangan = len(list)
    if jumlah_bilangan > 1:
        mid = jumlah_bilangan//2
        left = list[:mid]
        right = list[mid:]
        mgsort(left)
        mgsort(right)
        jumlah_left = len(left)
        jumlah_right = len(right)
        c_kiri, c_kanan,c_all = 0,0,0
        while c_kiri < jumlah_left or c_kanan < jumlah_right:
            if c_kiri == jumlah_left: #potongan kiri habis
                list[c_all] = right[c_kanan]
                c_kanan += 1
            elif c_kanan == jumlah_right: #potongan kanan habis
                list[c_all] = left[c_kiri]
                c_kiri += 1
            #elemen kiri lebih kecil
            elif list[c_kiri] <= list[c_kanan]:
                list[c_kanan] = left[c_kiri]
                c_kiri += 1
            #jika kanan lebih kecil
            else: 
                list[c_all] = right[c_kanan]
                c_kanan += 1
            c_all += 1
            
list = [1,9,4,7,3,5,6,2,8,10]
mgsort(list)
print(list)
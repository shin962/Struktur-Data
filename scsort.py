def selsort(list):
    for pos_tujuan in range(len(list)-1,0,-1):
        pos_max = 0
        for x in range(1,pos_tujuan+1):
            temp_max = list[pos_max]
            if temp_max < list[x]:
                pos_max = x
        temp = list[pos_max]
        list[pos_max] = list[pos_tujuan]
        list[pos_tujuan] = temp
        
list = [10,5,3,7,2,8]
selsort(list)
print(list)
hash_table = [None] * 10
def hashFunc(value):
    return value % len(hash_table)

def insert(hash_table, value):
    hash_key = hashFunc(value)
    hash_table[hash_key] = value
def search(value):
    return hashFunc(value)

insert(hash_table, 5)
insert(hash_table, 11)
insert(hash_table, 17)
insert(hash_table, 29)
print(hash_table)

import hashlib
def get_hash (data):
    hash_object = hashlib.md5(data.encode())
    print (hash_object.hexdigest())

name = 'Selimira' 
tomato = 'Hello'
get_hash(name)
get_hash(tomato)
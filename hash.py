import hashlib
def get_hash (data):
    hash_object = hashlib.md5(data.encode())
    print (hash_object.hexdigest())

mystring = 'Selimira' 
tomato = 'selimira'
get_hash(mystring)
get_hash(tomato)
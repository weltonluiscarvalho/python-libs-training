import hashlib

my_hash = hashlib.sha256()
my_hash.update(b"sexo")
my_hash_digest = my_hash.digest()
my_hash_hexdigest = my_hash.hexdigest()

# print(my_hash.block_size)
# print(type(my_hash))

# print(my_hash_digest)
# print(my_hash_hexdigest)
# print(type(my_hash_digest))


my_new_hash = hashlib.new('sha256')
my_new_hash.update(b'crypto\n')
# print(my_new_hash.hexdigest())
# print(my_new_hash.hexdigest())


# print(my_new_hash.hexdigest())
# print(my_new_hash.digest_size)
# print(my_new_hash.block_size)
# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)

with open('cryptographic/file.txt', 'rb') as file:
    hash_file = hashlib.file_digest(file, 'sha-256')
    
# print(hash_file.hexdigest())

another_kind_of_hash = hashlib.pbkdf2_hmac('sha256', b'crypto', b'sal grosso', 25)
print(another_kind_of_hash.hex())

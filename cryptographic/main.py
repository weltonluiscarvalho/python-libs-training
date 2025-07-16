import hashlib

my_hash = hashlib.sha256()
my_hash.update(b"sexo")
my_hash_digest = my_hash.digest()
my_hash_hexdigest = my_hash.hexdigest()

# print(my_hash.block_size)
# print(type(my_hash))

print(my_hash_digest)
print(my_hash_hexdigest)
print(type(my_hash_digest))

nome: str = "We&&p€𔐖lton"


numero: int = 29

# print(ascii(nome))
# print(bool(nome), bool(numero))
# print(sys.float_info)

# print(numero.bit_length())
# print(bin(numero))

# print(numero.to_bytes(length=4, signed=True, byteorder='big'))

# print(int.from_bytes(b'\x00\x00\x00\x1d', byteorder='little'))
print(int.from_bytes([1, 2], byteorder='little'))


resultado = compile(source="print('caralho')", filename="<string>", mode='exec')

print(type(resultado))
print(resultado)
exec(resultado)

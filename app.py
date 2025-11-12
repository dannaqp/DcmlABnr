# Proyecto Parcial 2
# Ariel Guerrero, Cesar Arciniegas, Camila Villagran y Danna Simaluisa
# Decimal de 2 cifras a numero binario de 8 bits

print('CONVERSOR DE DECIMAL A BINARIO DE 8 BITS')
print()
nrodec = int(input('Ingrese su numero decimal de dos cifras: '))
while nrodec <= 0 or nrodec >= 100:
    nrodec = int(input('Error: El número debe ser de 0 a 99 (2 cifras): '))    
else:
    numdec = nrodec
    resultado = ""
    valores = (128, 64, 32, 16, 8, 4, 2, 1)
    for i in range(8):
        if numdec >= valores[i]:
            resultado = resultado + "1"
            numdec = numdec - valores[i]
        else:
            resultado = resultado + "0"
    print()
    print('El equivalente binario de' , nrodec , 'es: ' , resultado)
    print()
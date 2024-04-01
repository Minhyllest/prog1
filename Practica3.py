n = int(input("Ingrese un numero mayor a cero: "))
while n != 1:
    print (n)
    if n % 2 == 0: # n es par
        n = n / 2
    else: # n es impar
        n = n * 3 + 1

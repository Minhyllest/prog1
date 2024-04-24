#ejercicio 1 a) práctica 3

# for i in range(1,5+1):
#     print(i)


#ejercicio 1 b) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print(i)



#ejercicio 2 a) práctica 3


# for i in range(4,7+1):
#     print(i)


#ejercicio 2 b) práctica 3

# m=int(input("ingrese un numero: "))
# n=int(input("ingrese otro numero: "))

# if n>m:
#     for i in range(m,n+1):
#         print (i)
# else:
#     for i in range(m,n-1,-1):
#         print (i)


#ejercicio 3 a) práctica 3

# for i in range(10,15+1):
#     print(i)

#ejercicio 3 b) práctica 3

# n=int(input("ingresa un numero: "))
# for i in range(n+1,n+6):
#     print(i)

#ejercicio 3 c) práctica 3

# n=int(input("ingrese un numero"))
# c=int(input("ingrese otro numero"))
# for i in range(n+1,c+2):
#     print(i)

#ejercicio 4 a) práctica 4

# for i in range(5,11+2,2):
#     print(i)

#ejercicio 4 b) práctica 4

# m=int(input("ingrese un numero: "))
# n=int(input("ingrese otro numero: "))

# if  m<n:
#     for i in range(m,n,3):
#         print(i)
    
#     print(n)
# else:
#     for i in range(n,m,3):
#         print(i)
    
#     print(m)

#ejercicio 4 c) práctica 4

# m=int(input("ingrese un numero: "))
# n=int(input("ingrese otro numero: "))
# p=int(input("ingrese otro numero: "))

# if  m<n:
#     for i in range(m,n,p):
#         print(i)
    
#     print(n)
# else:
#     for i in range(n,m,p):
#         print(i)
    
#     print(m)

#ejercicio 5 a) práctica 3

# for i in range(8,3-1,-1):
#     print(i)

#ejercicio 6 a) práctica 3

# for i in range(15,6-1,-3):
#     print(i)

#ejercicio 7 práctica 3 

    #ejercicio 1 a)

    # i=1
    # while i<=5:
    #     print(i)
    #     i=i+1

    #ejercicio 1 b)
    # n=int(input("ingrese un numero: "))
    # i=1
    # while i<=n:
    #     print(i)
    #     i=i+1

    #ejercicio 2 a)
    # i=4
    # while i<=7:
    #     print(i)
    #     i=i+1

    #ejercicio 2 b)

    # m=int(input("ingrese un número: "))
    # n=int(input("ingrese otro número: "))
    # i=m
    # while i<=n:
    #     print(i)
    #     i=i+1
        
    #ejercicio 3 a)
    # i=10+1
    # while i<=15:
    #     print(i)
    #     i=i+1

    #ejercicio 3 b) práctica 3

    # n=int(input("ingresa un numero: "))
    # i=n
    # while i<=n+5:
    #     print(i)
    #     i=i+1

    #ejercicio 3 c) práctica 3

    # n=int(input("ingrese un numero"))
    # c=int(input("ingrese otro numero"))
    # i=n
    # while i<=c:
    #     print(i)
    #     i=i+1
    #ejercicio 4 a) práctica 4

    # i=5
    # while i<=11:
    #     print(i)
    #     i=i+2

    #ejercicio 4 b) práctica 4

    # m=int(input("ingrese un numero: "))
    # n=int(input("ingrese otro numero: "))

    # if m<n:
    #     i=m
    #     while i<=n:
    #         print(i)
    #         i=i+3  
    # if n<m:
    #     i=n
    #     while i<=m:
    #         print(i)
    #         i=i+3
    

    #ejercicio 4 c) práctica 4

    # m=int(input("ingrese un numero: "))
    # n=int(input("ingrese otro numero: "))
    # p=int(input("ingrese otro numero: "))

    # if m<n:
    #     i=m
    #     while i<=n:
    #         print(i)
    #         i=i+p
    # if n<m:
    #     i=n
    #     while i<=m:
    #         print(i)
    #         i=i+p

    #ejercicio 5 a) 
    # i=8
    # while i>=3:
    #     print(i)
    #     i=i-1


    #ejercicio 6 a)
    # i=15
    # while i>=6:
    #     print(i)
    #     i=i-3

#ejercicio 8 práctica 3

# i=-99
# while i<=99:
#     formula=(i**(((i)+2)*((i)+3)))==1
#     if formula==True:
#         print(i, "es un solución") 
#     i=i+1

#ejercicio 9 práctica 3

# x=int(input("ingrese  un número: "))
# i=x
# contador=0
# while i!=1:
#     if i%2==0:
#         while i%2==0:
#             print(i)
#             i=i/2
#             contador=contador+1
#     else:
#         while i%2!=0:
#             print(i)
#             i=3*i+1
#             contador=contador+1
# print("se tuve que repetir el procedimiento",contador,"veces")   

#ejercicio 10 a) práctica 3

# n=int(input("introduzca un número:"))
# i=1
# contador=1
# while contador<=n:
#     print(contador)
#     contador=2**i
#     i=i+1

#ejercicio 10 b) práctica 3

# n=int(input("introduzca un número mayor a 0: "))
# i=0
# while i<=n:
#     print(2**i)
#     i=i+1

#ejercicio 10 c) práctica 3

# n=int(input("introduzca un número mayor a 0: "))
# i=1
# while i<=n:
#     print(i**i)
#     i=i+1

# ejercicio 11 a) práctica 3

# n=int(input("ingrese  un número: "))
# i=1
# while i<=n:
#     while n%i==0:
#         print(i,"es divisor de ",n)
#         i=i+1
#     else:
#         i=i+1

# ejercicio 11 b) práctica 3


# n=int(input("ingrese  un número: "))
# i=2
# while i<=n:
#     while n%i==0:
#         print(i,"es divisor de ",n)
#         i=i+2
#     else:
#         i=i+2

# ejercicio 11 c) práctica 3


# n=int(input("ingrese  un número: "))
# i=1
# contador=0
# while i<=n:
#     while n%i==0:
#         print(i,"es divisor de ",n)
#         i=i+1
#         contador=contador+1
#     else:
#         i=i+1
# print(contador)

# ejercicio 11 d) práctica 3


# n=int(input("ingrese  un número: "))
# i=1
# suma=0
# while i<=n:
#     while n%i==0:
#         print(i,"es divisor de ",n)
#         suma=suma+i
#         i=i+1
#     else:
#         i=i+1

# print(suma)

#ejercicio 11 e) práctica 3 

# c=int(input("ingrese un numero positivo: "))
# n=int(input("ingrese un numero positivo: "))
# divisores=0
# i=1
# while i<=n:
#     while n%i==0  :
#         divisores=divisores+1
#         if divisores<=c:
#             print(i,"es divisor de ",n)
#         i=i+1
#     else:
#         i=i+1

#ejercicio 11 f) práctica 3 
        
# c=int(input("ingrese un numero positivo: "))
# n=int(input("ingrese un numero positivo: "))
# divisores=0
# i=n 
# while i>=c:

#     if n%i==0  :

#         divisores=divisores+1

#         if divisores<=c:

#             print(i,"es divisor de ",n)

#     i=i-1

#ejercicio 12 práctica 3 
    
# n=int(input("ingrese un numero positivo"))
# contador=1
# resultado=1
# while contador<=n:
#     resultado=contador*resultado
#     contador=contador+1 
# print(resultado)

#ejercicio 13 práctica 3

# n=int(input("ingresa un número: "))

# contador=1
# suma=0

# while contador<=n:
#     suma=suma+contador
#     contador+=1
#     if n<suma:
#         break
# print(n,"<",suma)


#ejercicio 14 a) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print(i*2)
    
#ejercicio 14 b) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print(i*2-1)

#ejercicio 14 c) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print(i**2)

#ejercicio 14 d) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print((i**3)-(i**2))

#ejercicio 14 e) práctica 3

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     print(1/(i**2))


#ejercicio 15 a) práctica 3

# n=int(input("ingrese un numero: "))
# suma=0
# for i in range(1,n+1):
#     suma=suma+i*2
#     print(suma)

#ejercicio 15 b) práctica 3


# n=int(input("ingrese un numero: "))
# suma=0
# for i in range(1,n+1):
#     suma=suma+(i**2)
#     print(suma)

#ejercicio 15 c) práctica 3 
# suma=0

# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     suma=suma+((i**3)-(i**2))
#     print(suma)

#ejercicio 15 d) práctica 3

# suma=0
# n=int(input("ingrese un numero: "))

# for i in range(1,n+1):
#     suma=suma+(1/(i**2))
#     print(suma)

#ejercicio 15 e) práctica 3

# Se va acercando al valor 1.644

#ejercicio 16 a) práctica 3 

# n=int(input("ingrese la cantidad de términos a sumar del logaritmo: "))
# suma=0
# contador=1
# while contador<=n:
#     suma=suma+(1/contador)
#     contador+=1
#     while contador<=n:
#         suma=suma-(1/contador)
#         contador+=1
#         break

# print(suma)

#ejercicio 16 b) práctica 3
# import math

# print(math.log(2)-suma)
# Desde el término n°6 en adelante

#ejercicio 16 c) práctica 3
# Desde el término 50 en adelante 

#ejercicio 16 d) práctica 3

e=float(input("ingrese un numero decimal muy pequeño: "))
suma=0
contador=1
valorReal=0.6931471805599353
while suma!=valorReal:
    if suma<(valorReal+e) and suma>valorReal:
        break
    suma=suma+1/contador
    contador+=1
    while suma!=valorReal and suma>valorReal:
        if suma<valorReal+e:
            break
        suma=suma-1/contador
        contador+=1
print(contador)
print("el resultado es",suma)
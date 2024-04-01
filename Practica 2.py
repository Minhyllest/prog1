#ejercicio 1 Práctica 2


# a = int(input("Ingrese un numero entero: "))
# b = int(input("Ingrese un numero entero: "))
# c = int(input("Ingrese un numero entero: "))
# print("Usted ingresó los valores:, a, b, c")
# print(a, "es mayor que",b, a>b )
# print(a,"y", b, "son iguales",a==b)
# print(a, "es el mayor de todos", a>b and a>c)
# print(b, "es el menor de todos", a<b and a<c)
# print(a, "es mayor que alguno de los otros dos",a>b or a>c )
# print(a, "es menor o igual que alguno de los otros dos", a<=b or a<=c)
# print("Los tres numeros son iguales", a==b and a==c and b==a and b==c and c==a and c==b)
# print("Los tres numeros son distintos", a!=b and a!=c and b!=a and b!=c and c!=a and c!=b)
# print(a, "es par", a%2==0)
# print("alguno es par", a%2==0 or b%2==0 or c%2==0)
# print("ninguno es par", a%2>0 or b%2>0 or c%2>0)
# print("todos son pares", a%2==0 and b%2==0 and c%2==0)
# print(a, "es multiplo de 3", a%3==0)
# print(a, "es multiplo de 3 y de 5", a%3==0 and a%5==0)
# print(a, "es multiplo de 3 y par", a%3==0 and a%2==0)
# print(a,"-", b, "da un numero positivo", (a-b)>0)
# print(a,"-",b, "da un numero par positivo", (a-b)>0 and (a-b)%2==0)

#ejercicio 2 práctica 2

# edad=int(input("ingrese cuantos años tiene usted: "))
# distancia=int(input("ingrese a cuantos km se encuentra: "))

# if edad >17 and edad<70 and distancia<500:
#     print("usted puede votar")
# else:
#     print("usted está excento de votar")


#ejercicio 3 práctica 2


# # a)
# a = 10
# if a != 0 :
#     print("perro")
#     #!!! imprime la palabra perro ya que a no es igual a 0 !!!
# # b)
# a = 10
# if a > 0 :
#     print("manzana")
# else:
#     print("naranja")
#     #imprime manzana ya que a es mayor a 0
# # c)
# a = 10
# if a > 0 :
#     print("Te quiero")
# print("bien lejos.")
##imprime primero te quiero ya que a es mayor a 0 y luego imprime bien lejos ya que aunque esté fuera del if se ejecuta de igual manera
# # d)
# a = 5
# b = 3
# c = 2
# if a < b * c :
#     print("Hola!")
# else:
#     print("Chau!")
# #imprime hola ya que la condicion es si a es menor a b multiplicado por c se imprime hola y si no se cumple  la condicion se imprime chau
# # e)
# p1 = 3,14
# p2 = 3,141569
# if p1 == p2 :
#     print("p1 y p2 son iguales!")
# else:
#     print("p1 y p2 no son iguales!")
#     #imprime que p1 y p2 no son iguales ya que p2 contiene mas decimales
# f)
# a = "Hola"
# b = "hola"
# if a == b :
#     print("Python es insensible!")
# else:
#     print("Python es muy sensible!")
# #imprime python es muy sensible ya que este es sensible a las mayusculas o minusculas por lo tanto no los considera lo mismo"


# Ejercicio 4 práctica 2

# Leer el siguiente programa. ¿Para qué valores de la variable a imprime "hola!" cuando se
# ejecuta? ¿Y para cuáles "chau!"?
# a = int(input("Ingrese un valor para a"))
# if a == 0 :
#     print("hola!")
# else:
#     print("chau!")
## imprime hola para los valores iguales a 0 y chau para los valores distintos de 0


#ejercicio 5 práctica 2


# nota=int(input("ingrese una nota: "))
# if nota<4:
#     print("debe recuperar")


#ejercicio 6.a) práctica 2


# a=int(input("ingrese el primer numero: "))
# b=int(input("ingrese el segundo numero: "))

# if (a>b):
#     print(a, " es mayor a ",b )
# else:
#     print(b, " es mayor a ",a )


#ejercicio 6.b) práctica 2

# a=int(input("ingrese el primer numero: "))
# b=int(input("ingrese el segundo numero: "))

# if (a<b):
#     print(a, " es menor a ",b )
# else:
#     print(b, " es menor a ",a )


#ejercicio 7 práctica 2


# a=float(input("ingrese un numero: "))
# b= float(input("ingrese otro numero: "))
# promedio=((a+b)/2)
# print("el promedio es: ", promedio)

# if promedio>7:
#     print("aprobado")
# else:
#     print("desaprobado")


#ejercicio 8 práctica 2


# a=int(input("ingrese un numero entero positivo: "))

# if (a>9):
#     print("usted ingresó un número de mas de una sola cifra")
# else:
#     print("usted ingresó un número de una sola cifra")


#ejercicio 9 práctica 2


# dni1=30612453
# dni2=23763290
# dni3=21448503
# dni4=34582048
# dni4=15364857

# dni=int(input("ingrese su número de DNI: "))
# if dni==dni1 or dni==dni2 or dni==dni3 or dni==dni4:
#     print("su DNI se encuentra en la lista")
# else:
#     print("su DNI no se encuentra en la lista")

#ejercicio 10 práctica 2
 

# impuestos=78
# tarifaFija=480
# kiloWats=0
# excedentes=25.5
# consumo=float(input("ingrese el consumo de watts que figura en el medidor: "))

# print("usted consumio: ",consumo,"Kilowatts de electricidad\n")
# if consumo>200:
#     kiloWats=(consumo)+kiloWats
#     print("|usted debe pagar| \n")
#     print("tarifa fija: $",tarifaFija,"\n+")
#     print("Excedentes: $",(kiloWats-200)*excedentes,"\n      +")
#     print("impuestos: $",impuestos,"\n")
#     print("Total: $",tarifaFija+((kiloWats-200)*excedentes)+impuestos)
# else:
#     print("|usted debe pagar| \n")
#     print("tarifa fija: $",tarifaFija,"\n       +")
#     print("impuestos: $",impuestos,"\n")
#     print("Total: $",tarifaFija+impuestos)

#ejercicio 11 práctica 2

# a=int(input("ingrese un número: "))
# b=int(input("ingrese un número: "))
# c=int(input("ingrese un número: "))

# if a>b and a>c:
#     print("el mas grande es ",a)

# if b>a and b>c:
#     print("el mas grande es ",b)

# if c>a and c>b:
#     print("el mas grande es ",c)

#ejercicio 12 a) práctica 2 


# nota=(int(input("ingrese su nota: ")))

# if nota>0 and nota<4:
#     print("Reprobado")
# if nota>3 and nota<7:
#     print("debe rendir examen final")
# if nota>6 and nota<11:
#     print("eximido")


#ejercicio 12 b) práctica 2


# nota1=(int(input("ingrese su nota: ")))
# nota2=(int(input("ingrese su nota: ")))
# nota3=(int(input("ingrese su nota: ")))
# notaFinal=(nota1+nota2+nota3)/3

# print("su promedio es",notaFinal)

# if notaFinal>0 and notaFinal<4:
#     print("Reprobado")
# if notaFinal>3 and notaFinal<7:
#     print("debe rendir examen final")
# if notaFinal>6 and notaFinal<11:
#     print("eximido")


#Ejercicio 13 práctica 2

# numero1=int(input("ingrese un número entero: "))
# numero2=int(input("ingrese el segundo número entero: "))

# if numero1>numero2:
#     print("el primer número:",numero1,"es mayor a","el segundo número:",numero2)
# else:
#     print("el segundo número:",numero2,"es mayor a ","el primer número:",numero1)

#ejercicio 14 práctica 2

# entero1=int(input("ingrese un número entero: "))
# entero2=int(input("ingrese otro número entero: "))

# if entero1<entero2:
#     entero1,entero2=entero2,entero1
#     print(entero1,entero2)

#ejercicio 15 práctica 2

# a=int(input("ingrese un número entero: "))
# b=int(input("ingrese el segundo número entero: "))
# c=int(input("ingrese el tercer número entero: "))

# if a> b and b>c:
#     a,b,c=c,b,a
#     print(a,b,c)
# if a> c and c>b:
#     a,b,c=b,c,a
#     print(a,b,c)

# if b> a and a>c:
#     a,b,c=c,a,b
#     print(a,b,c)
# if b> c and c>a:
#     a,b,c=a,c,b
#     print(a,b,c)

# if c> a and a>b:
#     a,b,c=b,a,c
#     print(a,b,c)
# if c> b and b>a:
#     a,b,c=a,b,c
#     print(a,b,c)


#ejercicio 16 practica 2


# anio=int(input("ingrese un año: "))
# if anio%4==0:
#     if  (anio%100==0 and anio%400!=0):
#         print("este año no es bisiesto")
#     else:
#         print("este año es bisiesto")
# else:
#     print("este año no es bisiesto")

#ejercicio 17 practica 2 



# a=int(input("ingrese el coeficiente a: "))
# b=int(input("ingrese el coeficiente b: "))
# if a==0:
#     if b==0:
#         print("la ecuacion tiene infinitas soluciones")
#     else:
#         print("la ecuación no tiene solución")
# else: 
#      x=-(b/a)
#      print(a,"x +",b,"=0")
#      print("la solución de x es:{", x,"}")


# #ejercicio 18 practica 2
# a=float(input("ingrese el  coeficiente a : "))
# b=float(input("ingrese el  coeficiente b : "))
# c=float(input("ingrese el  coeficiente c: "))

# discriminante=(b**2)-(-4*a*c)

# if discriminante<0:
#     print("no hay raices reales")
# if discriminante==0:
#     raizunica=(b/(2*a))
#     print("hay una raiz real", raizunica)
# if discriminante>0:
#     raiz1= (-b + (discriminante**0.5)) / (2*a)
#     raiz2 = (-b - (discriminante**0.5)) / (2*a)
#     print("hay dos raices reales: ",raiz1, "y" ,raiz2)

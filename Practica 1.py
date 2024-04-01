
# #ejercicio 4

# z =int(input("ingrese un número: "))
# m=(z+1)
# print (m)

# ejercicio 6 
# print ("Mi primer programa en Python")

#ejercicio 7
# print ("v\ne\nr\nt\ni\nc\na\nl")

#ejercicio 8 
# print("*****\n*   *\n*   *\n*   *\n*****")

#ejercicio 9 
#print ("*\n***\n*****\n*******\n*********")

#ejercicio 10

# nombre=input("ingrese su nombre: ")
# print (nombre)

#ejercicio 11
# valor = input("ingrese el valor: ")
# print (("******************************\n* El resultado es:"),valor ,("\n******************************"))}

#ejercicio 12
   
    # ejercicio 2 
        # print (4/2+1)
        # print ((4+2)/(4-2))
        # print ((5+4/2)/(5-4/2))

    # #ejercicio 3 
        # x=int(input("ingrese un número: "))
        # y=int(input("ingrese otro número: "))
        # r= (x+y)
        # print(r)
    # ejercicio 5
        # r =int(input("ingrese un numero: "))
        # s =int(input("ingrese un numero: "))
        # t= (r+s)/2
        # print (t)

#ejercicio 13
# capital=int(input("ingrese el capital a invertir: "))
# meses=int(input("ingrese la cantidad de meses: "))
# dinero= (capital*0.06)*meses
# print (dinero+capital)

#ejercicio 14
# cantllamadas=int(input("ingrese la cantidad de llamadas: "))
# x =1
# contador=0
# while x <= cantllamadas:
#     cantseg=int(input("ingrese la cantidad de segundos de la llamada: "))
#     x+=1
#     contador+=12
#     contador+=cantseg
# print(contador)

#ejercicio 15

# cantventas=int(input("ingrese la cantidad de ventas: "))
# sueldoBase=42000
# x=1
# contadorVentas=0
# while x<= cantventas:
#     valorVentas=int(input("ingrese el valor de las ventas: "))
#     x+=1
#     contadorVentas+=valorVentas
# print("el sueldo final es de: ",sueldoBase+((contadorVentas*10)/100))

#ejercicio 16

# cantseg=int(input("ingrese la cantidad de segundos: "))
# resultado=0
# if cantseg>=60:
#      resultado=cantseg/60
#      print ("usted tiene:",resultado,"minuto/s")

# if cantseg>=3600:
#      resultado=cantseg/3600
#      print("el resultado es",resultado,"hora/s")
# if cantseg>=86400:
#      resultado=cantseg/86400
#      print("el resultado es: ",resultado,"día/s")

# ejercicio 17

# dinero= int(input("ingrese la cantidad de dinero a depositar: "))
# billetes2000=0
# billetes1000=0
# billetes500=0
# billetes200=0
# billetes100=0
# billetes50=0
# billetes20=0
# resto=0
# if dinero/2000>0:
#     billetes2000=dinero//2000
#     print("usted tiene",billetes2000,"billete/s de 2000")
#     resto=dinero%2000
    
# if resto/1000 >0 and resto/1000<2:
#         billetes1000=resto//1000
#         print("usted tiene",billetes1000,"billete/s de 1000")
#         resto=resto%1000
    
# if resto/500>0:
#     billetes500=resto//500
#     print("usted tiene",billetes500,"billetes/s de 500")
#     resto=resto%500
    
# if resto/200>0:
#     billetes200=resto//200
#     print("usted tiene",billetes200,"billetes/s de 200")
#     resto=resto%200
# if resto/100>0:
#     billetes100=resto//100
#     print("usted tiene",billetes100,"billetes/s de 100")
#     resto=resto%100
# if resto/50>0:
#     billetes50=resto//50
#     print("usted tiene",billetes50,"billetes/s de 50")
#     resto=resto%50
# if resto/20>0:
#     billetes20=resto//20
#     print("usted tiene",billetes20,"billetes/s de 20")
#     resto=resto%20
# if resto/10>0:
#     billetes10=resto//10
#     print("usted tiene",billetes10,"billetes/s de 10")
#     resto=resto%10

#ejercicio 18


# cantsegundos= int(input("ingrese la cantidad de segundos: "))
# segundos=0
# minutos=0
# horas=0
# dias=0
# resto=0
# if cantsegundos/86400>0:
#     dias=cantsegundos//86400
#     resto=cantsegundos%86400  
# if resto/84600>0:
#     horas=resto//3600
#     resto=resto%3600
# if resto/60>0:
#     minutos=resto//60
#     resto=resto%60
# if resto/1>0:
#     segundos=resto//1
#     resto=resto&1

# print(dias, " día/s ",horas, " hora/s " ,minutos, " minuto/s ",segundos," segundo/s.")


#ejercicio 19

# x=int(input("ingrese el valor de la variable x: "))
# y=int(input("ingrese el valor de la variable y: "))

# x,y = y,x

# print("el valor de x es :",x)

# print("el valor de y es :",y)

#ejercicio 20


# x=int(input("ingrese el valor de la variable x: "))
# y=int(input("ingrese el valor de la variable y: "))
# z=int(input("ingrese el valor de la variable z: "))
# x,y,z = y,z,x

# print("el valor de x es :",x)

# print("el valor de y es :",y)

# print("el valor de z es: ",z)

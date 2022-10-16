#Ejercicio1:asigno tres variables a acada número que se va a pedir por teclado, en el siguiente paso mediante la función if consigo q si el primer número = 0 el programa de devuelva ERROR,sin esto no se cumple pasará al siguiente paso y mediante la compararción de las tres variables me dirá si está en orden ascendente y si no se cumple ninguna de laas anteriores me devolverá el programa que los números están desordenados.

a=int(input("Dígame el primer número:"))
b=int(input("Dígame el segundo número:"))
c=int(input("Dígame el tercer número:"))

if a==0:
  print("ERROR")
elif a<b and b<c:    
  print("Los números están ordenados de manera ascendente")
else:
  print("Los números no están ordenados")
#Ejercicio2:En este apartado realizo unos pasos muy similares al anterior solo que en vez de comparar las variables al estar en una lista tengo que comparar las posiciones en la lista.
num=[int(input("Dígame el primer número:")),int(input("Dígame el segundo número:")),int(input("Dígame el tercer número:"))]

if num[0]==0:
  print("ERROR")
elif num[0] < num[1] < num[2]:
  print("Los números están ordenados de manera ascendente")
else:
  print("Los números están desordenados")
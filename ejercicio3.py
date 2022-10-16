#Ejercicio3:Este ejercicio consiste en contar las "a" que se introducen por teclado y para eelo lo hacemos mediante un bucle while el cual hará que se nos pidan letras por teclado y las letras "a" las irá contando mediante la variable contador y la función if,para que este programa finalice se usa otra condición que si se introduce un . por teclado el programa para.
contador=0

while True:
  frase=input("Introduzca aquí una letra:")
  if letra == "a":
    contador=contador+1
  elif letra == ".":
    break

print(f"El programa tiene {contador} letras a")

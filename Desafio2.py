
texto = input("\n ingrese un texto cualquiera: ")
texto_m = texto.lower()

letra1 = input("\nIngrese una letra: ")
letra2 = input("Ingrese una letra: ")
letra3 = input("Ingrese una letra: ")

letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

letras =[letra1,letra2,letra3]


print(f"\nla cantidad de veces que {letra1} aparece en {texto} es {texto.count(letra1)}")
print(f"la cantidad de veces que {letra2} aparece en {texto} es {texto.count(letra2)}")
print(f"la cantidad de veces que {letra3} aparece en {texto} es {texto.count(letra3)}")

#2
cantidad = texto.split()
contador_palabras = len(cantidad)

print(f"La cantidad de palabras que hay en el texto son: {contador_palabras}")

#3
primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"La primera letra es: {primera_letra} y la ultima letra es: {ultima_letra}")

#4
texto_al_reves = texto[::-1]
print(texto_al_reves)

#5
buscar_palabra = "python" in texto_m
result = {True: "Esta la palabra python en el texto", False: "No se encuentra la palabra python en el texto"}

print(result[buscar_palabra])

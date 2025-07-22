def palindromo(palabra: str) -> bool:
    palabra = palabra.lower().replace(" "," ")
    return palabra == palabra[::-1]
# entrada de la palabra que me permite interactuar si es o no con una función que lleva a describir el fragmento de codigo simple
out = input("Escribe una palabra: ")
if palindromo(out):
    print("es palindromo.")
else:
    print(" no lo es.")

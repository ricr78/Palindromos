def palindromo(palabra: str) -> bool:
    palabra = palabra.lower().replace(" "," ")
    return palabra == palabra[::-1]

out = input("Escribe una palabra: ")
if palindromo(out):
    print("es palindromo.")
else:
    print(" no lo es.")
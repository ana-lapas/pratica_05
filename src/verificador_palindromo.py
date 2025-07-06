def verificar_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

texto = input("Digite uma palavra ou frase: ")
if verificar_palindromo(texto):
    print("Sim")
else:
    print("Não")
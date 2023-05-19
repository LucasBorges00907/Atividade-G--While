#Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
def main():
    numero = int(input("Digite um número : "))
    contador = 0
    soma=0

    while contador<=numero:
        soma = contador+soma
        contador = contador+1

    media = soma/numero

    print(f"A soma de todos os número até {numero} é de: {soma} e a média entre eles é de {media}")
        








main()
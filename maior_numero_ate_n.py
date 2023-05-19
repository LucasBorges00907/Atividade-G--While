#Leia N e uma lista de N números e escreva o maior número da lista.

def main():
    n = int(input("Digite N: "))
    contador = 1
    maiornumero = 0

    while contador<=n:
        numero = int(input("Digite um número: "))
        if numero>maiornumero:
            maiornumero = numero
        contador = contador+1
         

    print(f"O maior número digitado é {maiornumero}")

main()
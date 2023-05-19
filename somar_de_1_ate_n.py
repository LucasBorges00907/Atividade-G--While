#Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def main():
    numero = int(input("Digite um número inteiro: "))
    soma = 0
    contador = 1

    while contador <= numero:
     soma = soma + contador
     contador = contador + 1

    print(f"A soma de todos os números entre 1 e {numero} é: {soma}")

main()
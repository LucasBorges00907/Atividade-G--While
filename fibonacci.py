# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
#(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

def main():
    n = int(input("Digite N: "))
    termo1 = 0
    termo2= 1

    print(f"Sequência: \n {termo1} \n {termo2}")
    contador = 2


    while contador<n:
        novo_termo = termo1+termo2
        print({novo_termo})
        termo1 = termo2
        termo2 = novo_termo

        contador = contador+1

main()
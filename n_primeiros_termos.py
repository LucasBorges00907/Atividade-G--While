#Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def main():
    n = int(input("Digite N: "))
    termo = 1
    contador = 1
    razao = 2

    while contador<=n:
        print({termo})
        termo = termo + razao
        razao = razao + 1
        contador = contador + 1 
    



main()

#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
#Aritmética que tem por valor inicial A0 e razão R.

def main():
    a0 = int(input("Digite o valor inicial (A0) da Progressão Aritmética: "))
    limite = int(input("Digite o limite dos valores a serem gerados: "))
    razao = int(input("Digite a razão (R) da Progressão Aritmética: "))

    valor = a0
    while valor<limite:
        print({valor})
        valor = valor+razao
    
main()
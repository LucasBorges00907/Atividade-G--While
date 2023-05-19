#Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
#maior quadrado menor que 38 é 36 (quadrado de 6).

def main():
    n = int(input("Digite N: "))
    maior_quadradox = maior_quadrado(n)
    print(f"O maior quadrado é: {maior_quadradox}")
   
def maior_quadrado(n):

    x = int((n**1/2))

  
    while x > 0:
        quadrado = x ** 2
        if quadrado <= n:
            return quadrado
        x = x-1

    return 0



        




   
main()
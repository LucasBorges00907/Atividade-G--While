#Leia um número, calcule e escreva seu fatorial.
#5! = 5 x 4 x 3 x 2 x 1 = 120

def main():
    valor = int(input("Digite um número positivo: "))

    
    fatorial = valor
    produto = valor

    
    

    while valor>1:
        produto = produto*(valor-1)
        valor = valor-1


    print(f"Fatorial de {fatorial} = {produto}")
    



main()


    
 
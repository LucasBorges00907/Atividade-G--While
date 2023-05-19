#Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.
def main():
    
    LimiteInferior = int(input("Digite o limite inferior: "))
    LimiteSuperior = int(input("Digite o limite superior: "))

    contador = LimiteInferior

    while contador<=LimiteSuperior:
        if contador%2==0:
            print({contador})
        contador = contador+1





main()
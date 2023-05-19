#Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
def main():

    numero = int(input("Digite o número: "))
    LimiteInferior = int(input("Digite o limite inferior: "))
    LimiteSuperior = int(input("Digite o limite superior: "))
    contador = LimiteInferior
  

    while contador<=LimiteSuperior:
        if contador%numero==0:
            print({contador})
        contador= contador+1


    








main()
#Leia N e escreva todos os números inteiros pares de 1 a N.

def main():
      n = int(input("Digite N: "))
      contador = 1

      while contador<=n:
            if contador%2==0:
                  print(f"Existem {contador} numeros pares de 1 a N")
                  contador = contador+1
                

main()

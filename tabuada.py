def main():
    numero = 1

    while numero <=10:
        print(f"Tabuada do {numero}:")
        contador = 1
        while contador<=10:
            resultado = numero*contador
            print(f"{numero} x {contador} = {resultado}")
            contador = contador+1
        print()
        numero = numero+1
            




main()



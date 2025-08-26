def comparar_numeros():
    """
    Este programa lê dois números inteiros e informa se eles são iguais ou diferentes.
    """
    try:
        # Pede os dois números ao usuário
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        
        # Compara os dois números
        if num1 == num2:
            print("Os números são iguais.")
        else:
            print("Os números são diferentes.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

comparar_numeros()
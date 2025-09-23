import math  # Importa a biblioteca matemática

# Variável para controlar se é a primeira operação
primeira_operacao = True

# Loop principal da calculadora
while True:
    # Exibe o menu de operações
    print('Calculadora Simples do Daniel da Silva Azevedo')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exponenciação (e^x)')
    print('6 - Raiz quadrada')
    print('7 - Potenciação (x^y)')
    # Só mostra a opção de sair após a primeira operação
    if not primeira_operacao:
        print('0 - Sair')
    # Solicita ao usuário a escolha da operação
    op = input('Escolha a operação: ')

    # Se não for a primeira operação e o usuário escolher sair, encerra o programa
    if not primeira_operacao and op == '0':
        print('Saindo da calculadora. Até logo!')
        break
    # Operação de soma
    elif op == '1':
        numero1 = float(input('Digite o primeiro número: '))  
        numero2 = float(input('Digite o segundo número: '))   
        print('Resultado:', numero1 + numero2)                
    # Operação de subtração
    elif op == '2':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        print('Resultado:', numero1 - numero2)
    # Operação de multiplicação
    elif op == '3':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        print('Resultado:', numero1 * numero2)
    # Operação de divisão
    elif op == '4':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        if numero2 == 0:
            print('Erro: divisão por zero') 
        else:
            print('Resultado:', numero1 / numero2)
    # Exponenciação (e^x)
    elif op == '5':
        x = float(input('Digite o valor de x para e^x: '))
        print('Resultado:', math.exp(x))  
    # Raiz quadrada
    elif op == '6':
        x = float(input('Digite o número para raiz quadrada: '))
        if x < 0:
            print('Erro: número negativo não possui raiz real')  
        else:
            print('Resultado:', math.sqrt(x))  
    # Potenciação (x^y)
    elif op == '7':
        x = float(input('Digite o valor de x: '))
        y = float(input('Digite o valor de y: '))
        print('Resultado:', x ** y)  
    # Caso o usuário digite uma opção inválida
    else:
        print('Opção inválida')
        print()
        continue
    # Após a primeira operação, permite exibir a opção de sair
    primeira_operacao = False
    print()  
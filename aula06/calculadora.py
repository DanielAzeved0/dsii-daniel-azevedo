
import math
print('Calculadora Simples do Daniel da Silva Azevedo')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Exponenciação (e^x)')
print('6 - Raiz quadrada')
print('7 - Potenciação (x^y)')
op = input('Escolha a operação: ')

if op == '1':
    # Soma 
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    print('Resultado:', numero1 + numero2)
elif op == '2':
    # Subtração 
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    print('Resultado:', numero1 - numero2)
elif op == '3':
    # Multiplicação 
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    print('Resultado:', numero1 * numero2)
elif op == '4':
    # Dividisão
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    if numero2 == 0:
        print('Erro: divisão por zero')
    else:
        print('Resultado:', numero1 / numero2)
elif op == '5':
    # Calcula exponenciação: e^x
    x = float(input('Digite o valor de x para e^x: '))
    print('Resultado:', math.exp(x))
elif op == '6':
    # Raiz quadrada 
    x = float(input('Digite o número para raiz quadrada: '))
    if x < 0:
        print('Erro: número negativo não possui raiz real')
    else:
        print('Resultado:', math.sqrt(x))
elif op == '7':
    # Calcula potenciação: x^y
    x = float(input('Digite o valor de x: '))
    y = float(input('Digite o valor de y: '))
    print('Resultado:', x ** y)
else:
    print('Opção inválida')
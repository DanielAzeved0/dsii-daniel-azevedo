def soma(x, y)
    #Retorna a soma de dois numeros
return x + y
    
def subtracao(x, y)
    #Retorna a subtração de dois numeros 
return x - y
    
def multiplicacao (x, y)
    #Retorna a multiplicação de dois numeros 
return x * y
    
def divisao(x, y)
    #Retorna a  quociente da divisão de dois numeros
return x / y
    
def expoente(x, )
    #Retorna o expoentre numeros
return x ** 2
    
def raiz(x, y)
    #Retorna o expoentre numeros
return x ** 0,5

def memoria(resultado):
    #Armagena o resultafo da ultima operação na memoria 
    global ulitma_operacao
    ulitma_operacao = resultado

def mostrar_memoria():
    #Exibe o valor armagenado na memoria  
    global ulitma_operacao
    print(f"Valor na memoria: {ulitma_operacao}")

def main()
    #Executa a calculadora
    while True
    #Exibe as opções de operação
    print("-" * 20)
    print("**   Calculadora  **")
    print("-" * 20)
    print("| 1.  Soma         |")
    print("| 2.  Subtração    |")
    print("| 3.  Multiplicação|")
    print("| 4.  Divisão      |")
    print("| 5.  Expoente     |")
    print("| 6.  Raiz         |")
    print("| 7.  Memória      |")
    print("| 0.  Sair         |")

    #Solicitar a opção do usuário
    opcao = int(input("Digite a opção desejada: "))

    #Valida a opção digitada 
    if opcao not in range(0, 7):
        print("Opção invalida! ")
        continue

    #Executa a operação escolhida
    if opcao == 1:
        x = float(input("Digite o primeiro numero: "))
        y = float(input("Digite o segundo numero: "))
        resultado = soma(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)

    elif opcao == 2:
        x = float(input("Digite o primeiro numero: "))
        y = float(input("Digite o segundo numero: "))
        resultado = subtracao(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)
    
    elif opcao == 3:
        x = float(input("Digite o primeiro numero: "))
        y = float(input("Digite o segundo numero: "))
        resultado = multiplicacao(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)
    
    elif opcao == 4:
        x = float(input("Digite o primeiro numero: "))
        y = float(input("Digite o segundo numero: "))
        resultado = divisao(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)
    
    elif opcao == 5:
        x = float(input("Digite o primeiro numero: "))
        # y = float(input("Digite o segundo numero: "))
        resultado = expoente(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)
    
    elif opcao == 6:
        x = float(input("Digite o primeiro numero: "))
        # y = float(input("Digite o segundo numero: "))
        resultado = raiz(x, y)
        print(f"Resultado: {resultado}")
        memoria(resultado)
    
    elif opcao == 7:
        mostrar_memoria()
    
    elif opcao == 0:
        break

if __name__ == "__main__"
main()

_____________________________________________________________________
#tratamento de except

def soma(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Erro: valor invalido. ")

def subtracao(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Erro: valor invalido. ")

def multiplicacao(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Erro: valor invalido. ")

def divisao(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        print("Erro: valor invalido. ")
    except ZeroDivisionError:
        print("Erro: divisão por zero")

_____________________________________________________________________

def main():

    while True:
    #Codigo na função main...

        #Executa a operação escolhidaa
        if opcao == 1:
            try:
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            resultado = soma(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)
        
        elif opcao == 2:
            try:
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            resultado = subtracao(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)
        
        elif opcao == 3:
            try:
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            resultado = multiplicacao(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)
        
        elif opcao == 4:
            try:
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            resultado = divisao(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)
        
        elif opcao == 5:
            try:
            x = float(input("Digite o primeiro numero: "))
            # y = float(input("Digite o segundo numero: "))
            resultado = expoente(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)
        
        elif opcao == 6:
            try:
            x = float(input("Digite o primeiro numero: "))
            # y = float(input("Digite o segundo numero: "))
            resultado = raiz(x, y)
            except ValueError: 
                continue
            print(f"Resultafo: {resultado}")
            memoria(resultado)

        elif opcao 0:
            break 

        if __name__ == "__main__":
            main()
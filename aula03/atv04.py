from datetime import date

def verificar_idade():
    """
    Este programa solicita o ano de nascimento do usuário e determina
    se a pessoa é maior ou menor de idade.
    """
    try:
        ano_nascimento = int(input("Em que ano você nasceu? "))
        
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
        
        if idade >= 18:
            print(f"Você tem {idade} anos. Você é maior de idade.")
        else:
            print(f"Você tem {idade} anos. Você é menor de idade.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um ano válido (ex: 1995).")

verificar_idade()
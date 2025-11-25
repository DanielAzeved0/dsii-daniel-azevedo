# dsii-daniel-azevedo
Aulas de Desenvolvimento de Sistemas II com o professor Roberto Itai

## **Aula 01 – Introdução ao Python e Variáveis**
**Impressão de texto:**

```
print('       * ')
print('      *** ')
print('     ***** ')
print('    ******* ')
print('   ********* ')
print('  *********** ')
print(' ************* ')
print('      ***\n      ***\n      ***\n')
```

**Variáveis e tipos:**

```
x = 3
print(x)
print(type(x))
```

**Entrada de dados:**

```
x = int(input('Digite um numero: '))
print(x)
```

## **Aula 02 – Operações e Entrada de Dados**
**Cálculo do quadrado:**

```
num = int(input('Digite um numero: '))
x = num ** 2
print('O quadrado do numero', num, 'é: ', x)
```

**Média de notas:**

```
nota01 = int(input('Digite a nota do Aluno: '))
nota02 = int(input('Digite a nota do Aluno: '))
nota03 = int(input('Digite a nota do Aluno: '))
notasSomadas = nota01 + nota02 + nota03
notaFinal = notasSomadas / 3
print('A nota final é: ', notaFinal)
```

**Concatenação e soma:**

```
a = 5
b = 3
soma = a + b
print(soma)
c = "4"
d = "7"
concatenar = c + d
print(concatenar)
```

## **Aula 03 – Estruturas Condicionais**
**Verificação de média:**

```
media01 = float(input('Digite a média do aluno do primeiro semestre: '))
media02 = float(input('Digite a média do aluno do segundo semestre: '))
mediasSomadas = media01 + media02
mediaFinal = mediasSomadas / 2
if mediaFinal > 6:
    print ('A média informada é: ', mediaFinal, 'Aluno foi aprovado')
elif mediaFinal >= 4 and mediaFinal <= 4.5:
    print ('A média informada é:', mediaFinal, 'Aluno ficou de recuperação')
else:
    print (f'A média informada é:  {mediaFinal}, Aluno foi reprovado')
```

**Comparação de números:**

```
Numero01 = int(input('Digite o primeiro numero: '))
Numero02 = int(input('Digite o segundo numero: '))
if Numero01 > Numero02:
    print (Numero01, 'é maior que', Numero02)
else:
    print (Numero02, 'é maior que', Numero01)
```

**Paridade:**

```
numero = int(input('Digite um numero: '))
if numero %2 == 0:
    print('esse numero é par')
else:
    print('esse numero é impar')
```

## **Aula 04 – Exercícios de Condicionais**
**Futebol:**

```
golsTime01 = float(input('Quantos gols o time 1 fez ? '))
golsTime02 = float(input('quantos gols o time 2 fez ? '))
if golsTime01 > golsTime02:
    print('Time 1 fez mais gols que o time 2')
elif golsTime01 == golsTime02:
    print ('Os times empataram')
else:
    print('Time 2 fez mais gols que o time 1')
```

**Finanças:**

```
valorPrestacao = int(input('Valor das prestações? '))
parcelas = int(input('Quantidade de parcelas? '))
valorSemJuros = valorPrestacao / parcelas
print('O valor sem juros é: ', valorSemJuros)
```

**Natação:**

```
idade = int(input("Digite a idade do nadador: "))
if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 11:
    print("Categoria: Infantil B")
elif idade >= 12 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Não tem idade para competir.")
```

## **Aula 05 – Estruturas de Repetição e Listas**
**For e listas:**

```
for lista in [1,2,3,4,5,6]:
    print(lista)
```

**Range:**

```
for lista in range(10):
    print(lista)
```

**Criação e manipulação de listas:**

```
lista_vazia = []
numero = [1,2,3,4,5]
lista_mista = [1, "dois", 3.0]
lista_aninhada = [[1,2], [3,4], [5,6]]
```

**Adição e remoção de elementos:**

```
lista = [1,2,3]
lista.append(4)
lista.insert(0,7)
lista.remove(2)
print(lista)
```

## **Aula 06 – Projeto de calculadora**

Criar uma calculadora funcional em Python que permite ao usuário realizar diversas operações matemáticas, repetidamente, até decidir sair do programa.

🧩 Funcionalidades

A calculadora implementa as seguintes operações:

➕ Soma
➖ Subtração
✖️ Multiplicação
➗ Divisão
🔺 Exponenciação (e^x)
✅ Potenciação com número personalizado (x^y)
📐 Raiz quadrada

🔁 Lógica do Programa

A calculadora exibe um menu de operações.
O usuário escolhe uma opção e informa os valores.
A operação é realizada e o resultado é exibido.
O programa permanece em execução até que o usuário escolha sair.
A opção de "sair" é exibida somente após a primeira operação.
Tratamento de erros incluído para casos como:

Divisão por zero.
Raiz quadrada de número negativo.
🖥️ Exemplo de Código da Calculadora (real do projeto)

```
import math
primeira_operacao = True
while True:
    print('Calculadora Simples do Daniel da Silva Azevedo')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Exponenciação (e^x)')
    print('6 - Raiz quadrada')
    print('7 - Potenciação (x^y)')
    if not primeira_operacao:
        print('0 - Sair')
    op = input('Escolha a operação: ')
    if not primeira_operacao and op == '0':
        print('Saindo da calculadora. Até logo!')
        break
    elif op == '1':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        print('Resultado:', numero1 + numero2)
    elif op == '2':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        print('Resultado:', numero1 - numero2)
    elif op == '3':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        print('Resultado:', numero1 * numero2)
    elif op == '4':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        if numero2 == 0:
            print('Erro: divisão por zero')
        else:
            print('Resultado:', numero1 / numero2)
    elif op == '5':
        x = float(input('Digite o valor de x para e^x: '))
        print('Resultado:', math.exp(x))
    elif op == '6':
        x = float(input('Digite o número para raiz quadrada: '))
        if x < 0:
            print('Erro: número negativo não possui raiz real')
        else:
            print('Resultado:', math.sqrt(x))
    elif op == '7':
        x = float(input('Digite o valor de x: '))
        y = float(input('Digite o valor de y: '))
        print('Resultado:', x ** y)
    else:
        print('Opção inválida')
        print()
        continue
    primeira_operacao = False
    print()
```

**Conclusão:**
O projeto permitiu a aplicação prática de diversos conceitos essenciais da linguagem Python, como estruturas condicionais, entrada e saída de dados, manipulação de listas e laços de repetição. A construção da calculadora serviu como um exercício integrador, consolidando o aprendizado adquirido nas aulas anteriores.

## **Aula 07 – Funções em Python**

Nesta aula, aprendemos sobre a definição, chamada e utilidade das funções em Python. Funções permitem organizar o código em blocos reutilizáveis, facilitando a manutenção e a legibilidade.

**Exemplo de função simples:**

```
def saudacao():
    print("Olá, bem-vindo à aula de funções!")

saudacao()
```

**Função com parâmetros e retorno:**

```
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("O resultado da soma é:", resultado)
```

**Função para verificar se um número é par:**

```
def eh_par(numero):
    return numero % 2 == 0

num = int(input("Digite um número: "))
if eh_par(num):
    print("O número é par.")
else:
    print("O número é ímpar.")
```

**Principais tópicos abordados:**
- Definição de funções com `def`
- Parâmetros e argumentos
- Retorno de valores com `return`
- Escopo de variáveis
- Reutilização de código

**Conclusão:**  
O uso de funções torna o código mais organizado, modular e fácil de entender. Elas são fundamentais para projetos maiores e para evitar repetição de código.

## **Aula 08 – Conexão com Banco de Dados MySQL**

Nesta aula, aprendemos como conectar um programa Python a um banco de dados MySQL, realizar inserções e consultas, e tratar possíveis erros de conexão ou operação.

**Principais tópicos abordados:**
- Instalação do driver MySQL para Python (`mysql-connector-python`)
- Estabelecimento de conexão com o banco de dados
- Inserção de dados usando comandos SQL parametrizados
- Consulta e exibição de registros do banco
- Tratamento de exceções e fechamento seguro da conexão

**Exemplo de código:**

```python
import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        database="senaisql",
        user="root",
        password="senai",
        port=3306,
        auth_plugin='mysql_native_password'
    )
    cursor = conexao.cursor()

    while True:
        nome = input("Digite o Nome: ")
        sobrenome = input("Digite o Sobrenome: ")
        idade = int(input("Digite a Idade: "))
        sexo = input("Digite o Sexo (M/F): ").upper()

        try:
            cursor.execute(
                "INSERT INTO Cadastro (Nome, Sobrenome, Idade, Sexo) VALUES (%s, %s, %s, %s)",
                (nome, sobrenome, idade, sexo)
            )
            conexao.commit()
            print("Dados inseridos com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados: {e}")
            conexao.rollback()

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == "n":
            break

    cursor.execute("SELECT * FROM Cadastro")
    registros = cursor.fetchall()
    for row in registros:
        print("Nome = ", row[0])
        print("Sobrenome = ", row[1])
        print("Idade = ", row[2])
        print("Sexo  = ", row[3], "\n")

except mysql.connector.Error as e:
    print(f"Erro de conexão/operação com o banco de dados: {e}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
```

**Resumo:**  
O código acima permite inserir novos registros em uma tabela chamada `Cadastro` e, ao final, exibe todos os registros cadastrados. O tratamento de exceções garante que erros de conexão ou operação sejam informados ao usuário e que a conexão com o banco seja fechada corretamente.

**Dica:**  
Para usar o MySQL com Python, instale o driver com:
```
pip install mysql-connector-python
```
## **Aula 10 – Python com MongoDB**

Nesta aula vimos na prática como usar MongoDB com Python

usamos o `prompt` comando para roda o a pasta "mongosh-1.9.0-win32-x64" e roda o arquivo "mongosh.exe" (tudo isso no terminal prompt), lá usamos o bando de dados usando o comando 
```sh
use nome-do-bando
```

depois abrimos o arquivo `index.py`, mas antes baixamos a extenção `pymong` com o comando
```sh
pip install pymongo
```

após isso rodamos o `index.py` no terminal e assim o programa roda 


## **Aula 11 - # Sistema de Cadastro - Python

## Descrição
Sistema simples e funcional de cadastro de pessoas desenvolvido em Python com interface gráfica usando tkinter.

## Funcionalidades
- ✅ Cadastro de pessoas com nome, sobrenome, idade e sexo
- ✅ Validação de dados de entrada
- ✅ Armazenamento persistente em arquivo JSON
- ✅ Interface gráfica intuitiva
- ✅ Listagem de cadastros
- ✅ Relatório detalhado
- ✅ Limpeza de campos
- ✅ Data e hora do cadastro

## Campos do Cadastro
- **Nome**: Campo obrigatório (texto)
- **Sobrenome**: Campo obrigatório (texto)
- **Idade**: Campo obrigatório (número entre 0 e 150)
- **Sexo**: Campo obrigatório (seleção: Masculino, Feminino, Outro)

## Como Executar
1. Execute o arquivo `cadastro.py`
2. A interface gráfica será aberta
3. Preencha os campos solicitados
4. Clique em "Cadastrar" para salvar

## Botões Disponíveis
- **Cadastrar**: Salva os dados inseridos
- **Limpar**: Limpa todos os campos
- **Listar**: Exibe relatório completo em nova janela

## Validações Implementadas
- Campos obrigatórios não podem ficar vazios
- Idade deve ser um número válido entre 0 e 150
- Nomes são formatados automaticamente (primeira letra maiúscula)
- Sexo deve ser selecionado da lista

## Armazenamento
Os dados são salvos automaticamente no arquivo `cadastros.json` na mesma pasta do programa.

## Requisitos
- Python 3.x
- tkinter (geralmente incluído com Python)
- Bibliotecas padrão: json, os, datetime

## Estrutura do Projeto
```
aula11/
├── cadastro.py          # Arquivo principal do sistema
├── README.md           # Documentação
└── cadastros.json      # Arquivo de dados (criado automaticamente)
```

## Características Técnicas
- Arquitetura orientada a objetos
- Interface responsiva
- Tratamento de exceções
- Validação de entrada
- Persistência de dados
- Código limpo e documentado

## Exemplo de Uso
1. Abra o programa
2. Digite "João" no campo Nome
3. Digite "Silva" no campo Sobrenome  
4. Digite "25" no campo Idade
5. Selecione "Masculino" no campo Sexo
6. Clique em "Cadastrar"
7. O sistema confirmará o cadastro e limpará os campos

---
*Desenvolvido seguindo as boas práticas de programação e normas de ética da área.
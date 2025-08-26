media01 = float(input('Digite a média do aluno do primeiro semestre: '))
media02 = float(input('Digite a média do aluno do segundo semestre: '))

mediasSomadas = media01 + media02 
mediaFinal = mediasSomadas / 2

if mediaFinal > 6:
    print ('A média informada é: ', mediaFinal, 'Aluno foi aprovado')
elif mediaFinal >= 4 and mediaFinal <= 4.5:
    print ('A média informada é:', mediaFinal, 'Aluno ficou de recuperção')
else:
    print (f'A média informada é:  {mediaFinal}, Aluno foi reprovado')

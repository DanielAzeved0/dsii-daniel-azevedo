media = float(input('Digite a média do aluno: '))
if media > 5:
    print ('A média informada é: ', media, 'Aluno foi aprovado')
elif media >= 4 and media <= 4.5:
    print ('A média informada é:', media, 'Aluno ficou de recuperção')
else:
    print (f'A média informada é:  {media}, Aluno foi aprovado')

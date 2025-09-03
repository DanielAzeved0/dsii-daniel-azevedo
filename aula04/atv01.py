golsTime01 = float(input('Quantos gols o time 1 fez ? '))
golsTime02 = float(input('quantos gols o time 2 fez ? '))

if golsTime01 > golsTime02 : 
    print('Time 1 fez mais gols que o time 2')
elif golsTime01 == golsTime02 :
    print ('Os times empataram')
else :
    print('Time 2 fez mais gols que o time 1')
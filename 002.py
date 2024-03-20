from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior.')
        totmaior += 1
    else:
        print('Essa pessoa é menor.')
        totmenor += + 1

print('São maiores de idade: {} \nSão menores de idade: {}'.format(totmaior, totmenor))

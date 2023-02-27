# f String
altura =  1.85
peso = 95
nome = 'Davi Miguel'
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f}m de altura, pesa {peso} quilos e seu imc é de {imc:.2f}'


print(linha_1)

# format
a = 'Alfa 1 2'
b = 22450.450
c = True
formato = 'a={nome1}, b={nome3}, c={nome2:,.2f} '.format(nome1 = a,nome2 = b,nome3 = c)
print(formato)
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

# c = float(input('Digite quando dinheiro você tem na carteira: '))
# print(f'Com {c} é possivel comprar {c / 3.27 :.4f}')

real = float(input('Quanto você tem na carteira: R$'))
dolar = real / 3.27
print(f'Com R${real :.2f} você pode comprar US${dolar :.2f}')
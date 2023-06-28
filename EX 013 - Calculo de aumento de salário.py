# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu valor R$$ '))
aumento = salario + (salario * 15/100)

print(f'Seu salário com aumento é R${aumento}')
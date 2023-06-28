# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto R$ '))
pdesc = preço - (preço * 5/100)

print(f'O valor do produto com desconto é R${pdesc}')
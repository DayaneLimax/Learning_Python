# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
litro = area / 2
print(f'sua parete tem a dimensão de {larg}x{alt} e sua área é de {area}m²')
print(f'Será necessario {litro} de tinta')


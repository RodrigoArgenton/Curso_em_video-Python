larg = float(input('A largura da parede é: '))
alt = float(input('A altura da sua parede é: '))
area = larg*alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Precisará de {:.2f}L para pintar toda a aparede.'.format(tinta))
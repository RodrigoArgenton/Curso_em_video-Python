#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Bota fogo', 
        'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 
        'EC Victória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-Go'
)

print(f"Os 5 primeiros colocados são: {times[:5]}")
print(f"Os 4 ultimos colocados são: {times[-4:]}")
print(f"Segue times em ordem alfabetica: {sorted(times)}")
print(f"O time da chapecoense está na posição: {times.index('Chapecoense')+1}")
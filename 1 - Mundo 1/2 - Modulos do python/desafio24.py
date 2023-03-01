# algoritmo para verificar se existe a palavra "santo" no nome da cidade
cidade = str(input('Digite o nome da sua cidade: ')).strip()

# processo para deixar toda a str minuscula
cidade = cidade.lower()

print(cidade[:5] == 'santo')
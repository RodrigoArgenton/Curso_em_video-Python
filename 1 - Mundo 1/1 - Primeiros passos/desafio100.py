n = int(input())
arr = map(int, input().split())
lista = list(arr)

print(sorted(set(lista), reverse=True)[1])
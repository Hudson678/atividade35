#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
mostre-os na ordem inversa
lista = []
for n in range(10):
    num = int(input('digite um numero'))
    lista.append(num)
lista.reverse()
print (lista)

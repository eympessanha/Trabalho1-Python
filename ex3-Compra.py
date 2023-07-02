# Programa que lê o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda

n = str(input("Informe o nome do produto: "))
q = int(input("Informe a quantidade comprada do produto: "))
v = float(input("Informe o valor unitário do produto: "))
p = float(input("Informe o percentual de desconto: "))

l= v*q
m = (l*p)/100
t = l-m

print(n)
print("Valor Total: R$",t)

#Programa que lê o valor em reais e exibe o equivalente em dólar. O usuário deve informar o valor da cotação

real = float(input("Informe a quantidade de reais para a conversão: "))
c = float(input(“Informe o valor da cotação do dólar atualmente: “))
e = c*real
print("Valor convertido em dólar: {:2.2f}".format(e))

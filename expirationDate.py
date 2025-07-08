from functionsDate import *

print('Olá! Qual a data de vencimento? Formato: DD-MM-AAAA.')

expirationDate = input('')

if len(expirationDate) == 10:
    print(verifyExpiration(expirationDate))
else:
    print('Entrada inválida')

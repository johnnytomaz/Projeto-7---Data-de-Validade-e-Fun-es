from datetime import datetime

def today():
    today = datetime.now()
    return today

def verifyDate(date):
    try:
        dateFormat = datetime.strptime(date, '%d-%m-%Y')
        return dateFormat
    except:
        raise Exception('Entrada válida. Formato correto: DD-MM-AAAA.')

def verifyExpiration(dataRef):
    expirationDate = verifyDate(date=dataRef)
    if today() > expirationDate:
        print('Está vencido!')
        return True
    else:
        print('Não está vencido!')
        return False
    
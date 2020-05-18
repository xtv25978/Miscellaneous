import datetime

def getDate():
    print('Enter date in format DD/MM/YYYY: ')
    rawDate = input()
    formattedDate = datetime.datetime.strptime(rawDate, '%d/%m/%Y')
    return formattedDate

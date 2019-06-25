#! python3
"""This program was made to calculate how much money you'll bring home per month (2019 calendar).  It can easily be replaced by a calculator or by excel
but it's decent practice with dictionaries for me.  After entering payPerHour and hours expected to work per day it should calculate the year
and each month's pay  (I realized after this should be updated to per week, but that can be another change for the future)"""


def amountPaid(payPerHour, hours):
#Dictionaries and tax data taken from online, assumed otherTaxes or rather other fees to be around 2%
    months = {'July': {'Days':31, 'WorkingDays':21}, 'August': {'Days':31, 'WorkingDays':22},'September': {'Days':30, 'WorkingDays':20},
    'October': {'Days':31, 'WorkingDays':22},'November': {'Days':30, 'WorkingDays':19},'December': {'Days':31, 'WorkingDays':21},
    'January': {'Days':31, 'WorkingDays':21},'February': {'Days':28, 'WorkingDays':19},'March': {'Days':31, 'WorkingDays':21},
    'April': {'Days':30, 'WorkingDays':22},'May': {'Days':31, 'WorkingDays':22},'June': {'Days':30, 'WorkingDays':20}}

    federalTaxes = {'1': {'Rate': 0.10, 'From':0, 'To': 9525}, '2': {'Rate': 0.12, 'From': 9525, 'To': 38700}, '3' : {'Rate': 0.22, 'From': 38701,
    'To': 82500}, '4' : {'Rate': 0.24, 'From':82501, 'To':157500}}

    illinoisTaxes = 0.05
    otherTaxes = 0.02

    total = 0
    taxes = []
    workingDays = 0
    #Calculates total net Salary and returns value to total.  Net is set to total for future calculations
    for month in months:
        workingDays = workingDays + months[month]['WorkingDays']
        months[month]['payPerMonth'] = (payPerHour * months[month]['WorkingDays']) * hours
        total += months[month]['payPerMonth']
    net = total
    #Pooling from the net amount, the net will by subtracted by the length of the appropriate tax bracket and fed into a list, seperating the totals
    for brackets in federalTaxes:
        if net <= 0:
            break
        elif net < (federalTaxes[brackets]['To'] - federalTaxes[brackets]['From']):
            taxes.append(net)
            break

        else:
            less = (federalTaxes[brackets]['To'] - federalTaxes[brackets]['From'])
            net = net - less
            taxes.append(less)

    #This needs to be reworked in the future, but this will multiply the tax totals in the taxes list by the appropriate tax bracket percent
    #in the federal tax dictionary
    taxFed = 0
    fedTaxes = taxes[0] * federalTaxes['1']['Rate'] + taxes[1] * federalTaxes['2']['Rate'] + taxes[2] * federalTaxes['3']['Rate']

    taxRest = total * illinoisTaxes + total * otherTaxes
    taxTotal = fedTaxes + taxRest
    totalPay = total - taxTotal
    perDay = totalPay/12/workingDays

    perMonth = 0
    for month in months:
        addMonth = totalPay / months[month]['WorkingDays'] * perDay
        perMonth = perMonth + addMonth
        print('In ' + str(month) + ' you will make ' + str(round(addMonth)) + '.' + ' That makes ' + str(round(perMonth)) + ' so far.')
    print('You\'ll earn ' + str(round(perMonth)) + ' this year')
    k = input('Please press enter to close ')

par1 = int(input('How much do you get paid an hour? ' ))
par2 = int(input('How many hours do you work a day? '))

amountPaid(par1,par2)

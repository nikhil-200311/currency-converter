print("      CURRENCY CONVERTER      ")

print(''' The currencies can be conveterted from and to: 
"USD-United States Dollar",
"DKK-Danish krone"
"GBP-Pound sterling"
"CAD-Canadian Dollar"
"IDR-ndonesian Rupiah"
"INR-Indian rupee"
"KRW-South Korean won"
"PHP-Philippine peso"
"SGD-Singapore dollar"''')

amount = int(input("Please enter the amount you want to convert: "))

from_currency = input("Please enter the currency code that has to be converted: ").upper()

to_currency = input("Please enter the currency code to convert: ").upper()

rate=1

if from_currency=='USD':
    if to_currency=='DKK':
        rate=amount*7.14
        print("The Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.83
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*1.34
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*15683.9
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*81.6
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*1325.21
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*56.69
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*1.37
        print("the Amount Coneverted is",rate)

        
elif from_currency=='DKK':
    if to_currency=='USD':
        rate=amount*0.14
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.12
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*.19
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*2197.89
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*11.42
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*185.69
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*7.94
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*0.19
        print("the Amount Coneverted is",rate)


elif from_currency=='GBP':
    if to_currency=='DKK':
        rate=amount*8.64
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*1.21
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*1.62
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*189884.9
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*98.65
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*1604.13
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*68.64
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*1.66
        print("the Amount Coneverted is",rate)
elif from_currency=='CAD':
    if to_currency=='DKK':
        rate=amount*5.35
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.62
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.75
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*11748
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*61.06
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*992.35
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*42.48
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*1.03
        print("the Amount Coneverted is",rate)


elif from_currency=='IDR':
    if to_currency=='DKK':
        rate=amount*0.00046
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.000053
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*0.0000085
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.000064
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*0.0052
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*0.084
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*0.36
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*0.0088
        print("the Amount Coneverted is",rate)
elif from_currency=='INR':
    if to_currency=='DKK':
        rate=amount*0.88
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.010
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*0.016
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*192.42
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.012
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*16.26
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*0.70
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*0.017
        print("the Amount Coneverted is",rate)
elif from_currency=='KRW':
    if to_currency=='DKK':
        rate=amount*0.0054
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.00062
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*0.0010
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*11.83
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*0.061
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.00075
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*0.043
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*0.0010
        print("the Amount Coneverted is",rate)


elif from_currency=='PHP':
    if to_currency=='DKK':
        rate=amount*0.13
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.015
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*0.024
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*276.63
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*1.44
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*23.38
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.018
        print("the Amount Coneverted is",rate)
    if to_currency=='SGD':
        rate=amount*0.024
        print("the Amount Coneverted is",rate)


elif from_currency=='SGD':
    if to_currency=='DKK':
        rate=amount*5.20
        print("the Amount Coneverted is",rate)
    if to_currency=='GBP':
        rate=amount*0.60
        print("the Amount Coneverted is",rate)
    if to_currency=='CAD':
        rate=amount*0.97
        print("the Amount Coneverted is",rate)
    if to_currency=='IDR':
        rate=amount*11428.27
        print("the Amount Coneverted is",rate)
    if to_currency=='INR':
        rate=amount*59.40
        print("the Amount Coneverted is",rate)
    if to_currency=='KRW':
        rate=amount*965.53
        print("the Amount Coneverted is",rate)
    if to_currency=='PHP':
        rate=amount*41.32
        print("the Amount Coneverted is",rate)
    if to_currency=='USD':
        rate=amount*0.73
        print("the Amount Coneverted is",rate)

else:
    print('Enter a valid Currency')



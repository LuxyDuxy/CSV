CSV_file = input('csv file: ')

import csv
from datetime import datetime

dates = []
dates_time_dates = []

fees = []
fee = 0
total_fee = 0

with open(f'{CSV_file}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        fees += [row[10]]
    fees.remove(fees[0])
     
fees_between_dates = []

with open(f'{CSV_file}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        row[3] = row[3].replace("-", "/")
        row[3] = row[3][2:]
        dates += [row[3]]

dates.remove(dates[0])

for date in dates:
    dates_time_date = datetime.strptime(date, '%y/%m/%d %H:%M:%S')
    dates_time_dates.append(dates_time_date)

print('\nCalculate the sum of all transaction fees in the period:')

from_date = str(input('from: '))
if int(from_date[:2]) == 20 and not from_date[3] == '/':
    from_date = from_date[2:]
from_date = from_date.replace("-", "/")
from_date = datetime.strptime(from_date, "%y/%m/%d %H:%M:%S")

to_date = str(input('to: '))
if int(to_date[:2]) == 20 and not to_date[3] == '/':
    to_date = to_date[2:]
to_date = to_date.replace("-", "/")
to_date = datetime.strptime(to_date, "%y/%m/%d %H:%M:%S")

print('\nAll dates on which the transactions took place:')

for date in dates_time_dates:
    if date > from_date and date < to_date:
        print(date)
        fees_between_dates += [fees[fee]]

    fee += 1

for fee in fees_between_dates:
    total_fee += float(fee)
    
print('\nTotal fee:',total_fee,'eth')

copy_to_clipboard = input('\nWould you like to copy the total fee to your clipboard? y/n\n')

if copy_to_clipboard == 'y':
    import pyperclip
    pyperclip.copy(total_fee)
    print('\nDONE')

elif copy_to_clipboard == 'n':
    print('\nOK')

Exit = input()
exit()
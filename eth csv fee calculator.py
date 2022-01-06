import pyautogui as auto
import time
import webbrowser
import pyperclip

address = input('Address: ')

webbrowser.open(f'https://etherscan.io/txs?a={address}&f=2')

auto.moveTo(1285, 720)

time.sleep(1)

stop_scrolling = 0

while stop_scrolling < 70:
    auto.keyDown('down')
    stop_scrolling += 1
    time.sleep(0.0003)

auto.moveTo(2050, 890)
auto.click()

time.sleep(1.5)

auto.keyUp('down')
auto.moveTo(1111, 700)
auto.click()

time.sleep(3)

auto.moveTo(1265, 790)
auto.click()

time.sleep(1)

def export_file():
    auto.hotkey('ctrl', 'c')
    return pyperclip.paste()

print(export_file())

CSV_file = export_file()

time.sleep(1)

auto.keyDown('enter')

import csv
from datetime import datetime

dates = []
dates_time_dates = []

fees = []
fee = 0
total_fee = 0

time.sleep(1)

with open(f'{CSV_file}') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        fees += [row[10]]
    fees.remove(fees[0])
     
fees_between_dates = []

with open(f'{CSV_file}') as csv_file:
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
    pyperclip.copy(total_fee)
    print('\nDONE')

elif copy_to_clipboard == 'n':
    print('\nOK')

Exit = input()
exit()
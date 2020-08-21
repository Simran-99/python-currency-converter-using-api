import requests
url='https://api.exchangerate-api.com/v4/latest/eur'
data=requests.get(url)
exchange_api=data.json()
print(data)
rates=exchange_api['rates']
print(rates)
usr_amt=int(input('How much do you want to convert'))
user_curr=input('Which currency do you want to convert into').upper()

if user_curr in rates.keys():
    print('Currency exists')
    conv_curr=usr_amt*rates[f'{user_curr}']
    print(f'{usr_amt} in euros is {conv_curr}{user_curr}')
else:
    print(f'{user_curr} Does not exist')


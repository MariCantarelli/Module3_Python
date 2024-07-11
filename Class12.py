#Creating conditions with while loop 

value = int(input('Enter the value of your product in R$:'))

while value > 20:
    value = (value * 0.10) + value
    print(f'The final value of your product will be R$ {value}')
    break
#While loop
#Excelente para loops dependentes de uma condição 

value = 100
day = 0
while value >= 20:
    day +=1
    print(f' In the day {day} the product will be sold for R${value}')
    value -= 5
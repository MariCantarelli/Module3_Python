#For loop - creating a rectangle

'''
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

lines = 6
columns = 6
symbol = "@"

for l in range(lines):
    for c in range(columns):
        print(symbol, end="")
    print()    
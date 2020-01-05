# Book Selling in Python
stock = int(input('Enter the number of books available to sell: '))
books = stock

# Checking if stock is 0
if stock == 0:
    print('\nNo books available for sale!')
else:
    print(f'\nNumber of Available Books is {books}\n')

# While loop starts
while stock >= 1:
    if stock % 5 == 0:
        print(f'\n{stock} books left!\n')

    print(f"Book number {stock} is sold!")
    stock -= 1

# When stock is totally 0
if stock == 0:
    print(f'\n{stock} books are left. {books} were sold.')

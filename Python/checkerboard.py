

for i in range (8):
    row = ' '.join ('* ' * 8)
    print ( row [1 + (i % 2 * 2):] [:17] )

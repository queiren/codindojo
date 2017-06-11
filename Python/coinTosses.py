import random
def coin():
    count = 0
    t_count = 1
    flips = 0
    x = .23945593
    y = .798839238
    headx = round(x)
    taily = round(y)
    while flips < 5000:
        if random.randint(0.0, 1.0) == 0.0:
            count += 1
            print('Attempt #', count, "Throwing a coin ... It's head! ... Got ", t_count, " head(s) so far and ",  "tail(s) so far")
            headx += 1

        else:
            t_count += 1
            count += 1
            print("Attempt #", count, "Throwing a coin ... It's tail! ... Got ", count, " head(s) so far and ",  "head(s) so far")
            taily += 1
        flips +=1

    print ("Attempt #", count, "you got ", headx, " heads, and ", taily, " tails!")
    print "Ending the program, thank you!"



coin()

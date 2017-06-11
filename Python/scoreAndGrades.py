import random
def score(n):
    for i in range(n):
        grades = random.randint(60, 101)
        if grades >= 60 and grades < 70:
            print "Score: ", grades,"; Your grade is D"
        elif grades >= 70 and grades < 80:
            print "Score: ", grades,"; Your grade is C"
        elif grades >= 80 and grades < 90:
            print "Score: ", grades,"; Your grade is B"
        elif grades >= 90 and grades < 101:
            print "Score: ", grades,"; Your grade is A"
        else:
            print "Oh Nooo!"


score(70)

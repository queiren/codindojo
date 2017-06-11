l = ['magical unicorns', 19, 'hello', 99.98, 'world']

if isinstance(l, str):
    print "false"
else:
    print "Your list is multi data type"
    stringList = [x for x in l if isinstance(x, str)]
    print "your string type are :", stringList
    num = [a for a in l if isinstance(a, int)]
    flt = [f for f in l if isinstance(f, float)]
    res = num + flt
    total = sum(res)
    print "count the numbers: ", total


l = ['one', 'two', 'three']
a = [2,3,1,7,4,12]
if isinstance(len(a), int):
    print "You entered a list type integer \n", sum(a)
else:
    print "It's no a lis of integer"


b = ["magical", "unicorns"]
string = " ".join(b)
if isinstance(string, str):
    print "The array you entered is of string type \n", string

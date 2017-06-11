# '''  odd_even  '''
#
# def odd_even():
#     for i in range(1, 2001):
#         if i % 2 != 0:
#             print "Number is ", i, ". This is and odd number"
#         else:
#             print "Number is ", i, ". This is and even number"
#
# odd_even()
#
# print ("-")*45
#
# ''' Multiply '''
def multiply(arr, n):
    for i in range(len(arr)):
        arr[i] *= n
    return arr
# a = [2,4,10,16]
# c = multiply(a, 5)
# print c
#
# print ("-")*45
#
#
#
# ''' Hacker Challenge'''
# def layered_multiples(arr):
#     print arr
#     new_array = []
#     for i in arr:
#         data = []
#         for i in range(0,i):
#             data.append(1)
#         new_array.append(data)
#     return new_array
#
# x= layered_multiples(multiply([2,4,5],3))

#
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
         val_arr = []
         for i in range(0,x):
            val_arr.append(1)
         new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

#
# # print only odd number 1 to 100
# for num in range(1, 100):
#     if num % 2 == 0:
#         continue
#     print num
# #
# #print 5 to 1000000 incremented by 5
# num = 5
# while num <= 1000000:
#     print(num)
#     num +=5
#
# # print 5 to 1000000 incremented by 5
#
# for count in range(5,1000000,5):
#     print (count)
#
# # sum of all values
# a = [1, 2, 5, 10, 255, 3]
# print sum(a)
#
# #average of the value
# a = [1, 2, 5, 10, 255, 3]
# print reduce(lambda x, y: x+y, a) / len(a)

print sum/len(a)


my_numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in my_numbers:
    sum += i
print sum

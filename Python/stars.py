# def draw_stars (arr):
#     # x = [4,6,1,3,5,7,25]
#     print arr
#     new_arr = []
#     for j in arr:
#         value_arr = []
#         for x in range(j):
#             value_arr.append("*")
#         new_arr.append(value_arr)
#
#     return new_arr
#
#
#
#
# draw = draw_stars([4,6,1,3,5,7,25])
# print draw


def star(arr):
    for i in arr:
        print "x" * i


star([6,2,3])

def partII(arr):
    for j in arr:
        if isinstance(j, int):
            print "x" * j
        elif isinstance(j, str):
            l = len(j)
            word = j[0].lower()
            print word * l
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
partII(x)

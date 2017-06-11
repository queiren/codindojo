def make_dict( arr1, arr2):
    if len(arr1) == len(arr2):
        new_dict_tuple = zip(arr1, arr2)
        new_dict = dict(new_dict_tuple)
        print new_dict
    elif len(arr1) > len(arr2):
        new_dict_tuple = zip(arr1, arr2)
        new_dict = dict(new_dict_tuple)
        print new_dict
        print "array one is bigger"
    elif len(arr1) < len(arr2):
        new_dict_tuple = zip(arr2, arr1)
        new_dict = dict(new_dict_tuple)
        print new_dict
        print "array two is bigger "




name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
make_dict(name, favorite_animal)

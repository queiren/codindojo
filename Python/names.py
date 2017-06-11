def showStd():
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    for data in students:
        print data["first_name"]+" "+data["last_name"]

showStd()

print ("-")* 5, "Part II", ("-")*5

def showinfo():
    users = {
     'Students': [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
      ],
     'Instructors': [
         {'first_name' : 'Michael', 'last_name' : 'Choi'},
         {'first_name' : 'Martin', 'last_name' : 'Puryear'}
      ]
     }
    for keys in users:
         print keys
         numStd = 1
         for data in users[keys]:
             wordsCount = len(data["first_name"]) + len(data["last_name"])
             print numStd, "-", data["first_name"], data["last_name"], "-", wordsCount
             numStd +=1
showinfo()

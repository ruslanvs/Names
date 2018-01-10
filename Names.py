students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]

def printStudents( incomingList ):
    for item in students:
        print item["first_name"], item["last_name"]

printStudents( students )

print"        -         "
print"----separation----"
print"        -         "

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

def userListPrint( incomingList ):
    for key in incomingList:
        print key
        counter = 0
        for item in incomingList[key]:
            counter += 1
            fnLength = len( item["first_name"])
            lnLendth = len( item["last_name"])
            print counter, "-", item["first_name"], item["last_name"], "-", fnLength + lnLendth

userListPrint( users )
    
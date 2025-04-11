# Dictionary
student={
    "first_name":"amir",
    "last_name":"hajitabar",
    "age":23,
    "languages":["English","Persian","French"],
    "is_pass":True
}

# print(student["first_name"])
# print(student.items())

# for key,value in student.items():
#     print(f"{key}---->{value}")

# for key in student.keys():
#     print(f"{key}")

# for key in student.keys():
#     print(f"{key}--->{student[key]}")

# "first_name"
# print(student["first_name"])

# for value in student.values():
#     print(f"{value}")

# student["age"]

'''
user={
    "username":'admin',
    "password":'admin'
}
'''

# user={
#     "username":'admin',
#     "password":'admin'
# }

# username=input("please enter username: ")
# password=input("please enter password: ")

# if username==user["username"] and password==user["password"]:
#     print("Login")
# else:
#     print("cant login")


# users=[
#    {
#     "username":"amir",
#     "password":"amir123"
#    },
#    {
#     "username":"mhmd",
#     "password":"mhm12"
#    },
#    {
#     "username":"javad",
#     "password":"js22"    
#    } 
# ]

# username=input("please enter username: ")
# password=input("please enter password: ")

#EXCERSICE 1


'''
amir:
    cpp
    c#
    js
jafar:
    c#
    php
mamreza:
    python
    GO
'''
programmers={
    "amir":["cpp","c#","js"],
    "jafar":["c#","php"],
    "mamreza":["python","GO"]
}

for name,languages in programmers.items():
    print(f"{name}:")
    for language in languages:
        print(f"\t{language}")

'''
EXCERSICE 2
amir:
    1-cpp
    2-c#
    3-js
jafar:
    1-c#
    2-php
mamreza:
    1-python
    2-GO
'''

'''
EXCERSICE 3
bia bar asas horof alefba be tartib asami ra neshon bdh
'''

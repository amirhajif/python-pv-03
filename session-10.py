# {} 

# user={
#     "username":"amirhossein",
#     "password":"amir123",
#     "age":24,
#     "isAdmin":True,
#     "programmingLanguages":["js","python"]
# }

# print(type(user))
# print(user)

# print(user["password"])

# update keys value
# user["age"]=25
# print(user)

# create new Key-Value
# user["city"]="babol"
# print(user)

# print(user["fatherName"])
# print(user.get("fatherName","we dont have this key"))

# delete key-values
# del user["programmingLanguages"]
# print(user)

user={
    "username":"amirhossein",
    "password":"amir123",
    "age":24,
    "isAdmin":True,
    "programmingLanguages":["js","python"]
}

# print(user.items())

# dict_items([('username', 'amirhossein'), ('password', 'amir123'),
#  ('age', 24), ('isAdmin', True), ('programmingLanguages',
#  ['js', 'python'])])

# for key,value in user.items():
#     print(f"{key}----->{value}")

# print(user.values())
# print(user.keys())

# for value in user.values():
#     print(value)

# for key in user.keys():
#     print(key)

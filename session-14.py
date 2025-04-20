# Type Cast
# number=int(input(""))

# number='123'
# number=int(number)
# print(type(number))

myDict={
    'amir':'python',
    'homan':'c#'
}

dictionary_items=list(myDict.items())
print(dictionary_items)

degrees=(180,360,540)
print(type(degrees))
degrees=list(degrees)
print(type(degrees))

cars={"bmw","pride","Benz"}
cars=list(cars)
print(cars)


students=["amir","ali","reza"]

students_tuple=tuple(students)
print(type(students_tuple))


students_set=set(students)
print(type(students_set))

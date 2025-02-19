# a,b=int(input("please enter a: ")),int(input("please enter b: "))
# print(f"before change values:a={a},b={b}")
# c=a
# a=b
# b=c
# print(f"after change values:a={a},b={b}")

# a=int(input("please enter a: "))
# b=int(input("please enter b: "))
# c=int(input("please enter c: "))
# x=int(input("please enter x: "))

# # ax2+bx+c
# result=(a*x**2)+b*x+c
# print(result)

'''
5 Topics:
List - Dictionary - Functions - condition - oop
'''

'''
Python Collections:
1. List []
2. Tuple ()
3. Set {}
4. Dictionary {}
'''

# List
# scores=[20,10,12,16,18]
# print(scores)
# print(type(scores))
# names=["amir","ali","reza"]
# print(names)


#index
# print(scores[2])
# print(scores[1:3])

# Update Element
# names=["amir","ali","rezzza"]
# names[2]="reza"
# print(names)

# # Add Element
# #append
# names.append("hooman")
# print(names)

# #insert
# names.insert(1,"mohammad")
# print(names)

# # delete
# del names[3]
# print(names)

# # pop
# removedItem=names.pop()
# print(removedItem)
# print(names)

# # pop in each index
# newRemovedItem=names.pop(0)
# print(newRemovedItem)
# print(names)

# cars =["benz","bmw","toyota","kia","bmw"]
# cars.remove("bmw")
# print(cars)

# SORT
# scores=[20,10,12,16,18]
# scores.sort()
# print(scores)

# cars =["benz","bmw","toyota","kia","bmw"]
# cars.sort()
# print(cars)

# scores.sort(reverse=True)
# print(scores)

#reverse
scores=[20,10,12,16,18]
# scores.reverse()
# print(scores)

print(len(scores))
print(max(scores))
print(min(scores))
print(sum(scores))

print(sum(scores)/len(scores))




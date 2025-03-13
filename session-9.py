#Excercise 1
# n=int(input("Enter a number: "))
# digit_count=0
# while n>0:
#     digit_count+=1
#     n=n//10
# print(digit_count)


'''
Collection:
1. List + []
2. Tuple + ()
3. Dictionary + {}
4. Set + {}

'''

# Tuple ()

cars=('BMW','Audi','Mercedes','Toyota')
print(cars)

print(cars[0])

# Cant Update , Change , Add , Remove
# cars[1]="pride"

for car in cars:
    print(car)

#Convert Tuple to List
carsList=list(cars)
print(carsList)

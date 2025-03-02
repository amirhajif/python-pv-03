'''Exc.1'''
# numbers=[1,2,3,4]

# countEven,countOdd=0,0 
# for number in numbers:
#     if number%2==0:
#         countEven+=1
#     else:
#         countOdd+=1
# print(f"Even Count:{countEven} odd Count:{countOdd}")

'''
1->countEven=0,countdd=0--> countEven=0,countOdd=1
2->countEven=0,countdd=0--> countEven=1,countOdd=1
3->countEven=0,countdd=0--> countEven=1,countOdd=2
4->countEven=0,countdd=0--> countEven=2,countOdd=2

'''


'''Exc.2'''
numbers=[1,2,3,4,5,6,7,8,9,10]
# miangin adad zoj va fard(haseljam / tedad)
sumEven,sumOdd,countEven,countOdd=0,0,0,0
for number in numbers:
    if number%2==0:
        countEven+=1
        sumEven+=number
    else:
        countOdd+=1
        sumOdd+=number

print(f"miangin adad zoj:{sumEven/countEven} miangin adad fard:{sumOdd/countOdd}")

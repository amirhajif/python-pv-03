seasson=int(input("please enter seasson: "))
if seasson==1:
    print("bahar")
elif seasson==2:
    print("tabestan")
elif seasson==3:
    print("paiiz")
elif seasson==4:
    print("zemestan")
else:
    print("input invalid")

match seasson:
    case 1:
        print("bahar")

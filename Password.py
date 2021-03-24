
i = 0
while True:
    print("What is your name")
    myname = input()

    i = i + 1

    print(i)

    if i == 3:
        print("Account Locked")
        break
    elif myname != "Ashok":
        continue
    else:
        print("Access Granted")
        print("Thank You")
        break
numstr = "123456788"

def exceed(number):
    if len(number) > 9:
        return False

def numcheck(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if i != j:
                if number[i] == number[j]:
                    return False

if exceed(numstr) == False:
    print("Number exceeded its length!")
else:
    if numcheck(numstr) == False:
        print("Your number is not sudokued")
    else:
        print(True)
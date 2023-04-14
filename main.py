numstr = "12345389"

def exceed(number):
    if len(number) > 9:
        return False

def numcheck(number):
    n=""
    for i in range(len(number)):
        if i == 0:
            n += number[0]
        else:
            for j in range(len(n)):
                if number[i] == n[j]:
                    return False
            n+=number[i]

if exceed(numstr) == False:
    print("Number exceeded its length!")
else:
    if numcheck(numstr) == False:
        print("Your number is not sudokued")
    else:
        print(True)
num=int(input(f"Please Enter a number:\n"))
print("Here you go !!")
l=[num*i for i in range(1,11)] #multiply num with i when the value of i is in the range 1 to 10
for index,val in enumerate(l,1):

    print(f"{num}*{index} is {val}")
    
import array as arr
jerNo=arr.array('i',[45,77,18,96,1])
print(jerNo)

for element in jerNo:
    if element%2==0:
        print(element,"Even JerNo")
    else:
        print(element,"Odd jerNo")




import array  as arr
data= arr.array('i',[10,20,30,40,50])

#append()
data.append(60)
print(data)#array('i', [10, 20, 30, 40, 50, 60])




#buffer_info()
print(data.buffer_info())#(139669199813632, 6)




#count()
print(data.count(30))#1


#extend()

data.extend({70,80})
print(data)#array('i', [10, 20, 30, 40, 50, 60, 70, 80])



#fromlist
listdata=[11,22,33,44,55]
data.fromlist(listdata)
print(data)#array('i', [10, 20, 30, 40, 50, 60, 70, 80, 11, 22, 33, 44, 55])



#index
print(data.index(40))#3



#insert()

data.insert(5,100)
print(data)#array('i', [10, 20, 30, 40, 50, 100, 60, 70, 80, 11, 22, 33, 44, 55])



#pop()

data.pop()
print(data)#delete last data




#remove()

data.remove(30)
print(data)#Remover 30 object


#reverse()
data.reverse()
print(data)



#tolist
copy=data.tolist()
print(copy)



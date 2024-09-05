# Tuples:

tuple2 = 43
print(tuple2)       #43
print(type(tuple2)) #<class 'int'>

# single value tuple
tuple3 = 43
print(type(tuple3))  #<class 'int'>

tuple1 = (32,5.6, 'python', [11, 12, 13])
print(tuple1[2])         #python
print(tuple1[0:3])       #(32, 5.6, 'python')

tuple2 = (32, 5.6, 'python', [11, 12, 13], 'django', (21, 22, 23))
print(tuple2[1:6])        #(5.6, 'python', [11, 12, 13], 'django', (21, 22, 23))
print(tuple2[1:7:2])      #(5.6,[11, 12, 13], 'django')

#nested indexing
print(tuple2[4][1])          #j

#concatetion & repetition
a= (1,2,3)
b=('python', 4, 'django')
print(a+b)    #(1, 2, 3, 'python', 4, 'django')
print(a)      #(1, 2, 3)
print(b)      #('python', 4, 'django')

# index & count
tuple2  = (32, 5.6, 'python',[11, 12, 13], 75, 'django',(21, 22, 23),43,32)
print(tuple2.index(43))   #7
print(tuple2.count(32))   #2










#contains all in-built data structures of python namely list, dictionary,tuple set..

list = [1,2,3,4,5.5,'xcv',[7,8,9]]
print(list)
print(list[6][1])
print(list[-2])

dictionary = {'name' : 'shubham','lastname':'singh'}
print(dictionary)
print(dictionary['lastname'])
print(dictionary.get('name'))
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)
print(Tuple)

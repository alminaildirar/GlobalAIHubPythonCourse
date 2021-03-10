#create two lists the first list should consist of odd numbers.The second list is also of even numbers
#merge these two lists.Multiply all values in the new list by 2.
#use a loop to print data type of the values in the new list.

numbers = list(range(20))

listofEvens = [i for i in numbers if i % 2 == 0 ]
listofOdds =  [i for i in numbers if i % 2 == 1 ]

listofEvens.extend(listofOdds)
listofEvens.sort()

mergeList = listofEvens.copy()

mergeList = [i*2 for i in mergeList]

for i in numbers:
    print(type(mergeList[i]))
    



# find and replace
myString = "If monkeys like bananas, then I must be a monkey!"
print myString.find("monkey")
print myString.replace ("monkey", "alligator", 1)

# min and max
x = [2,54,-2,7,2,98]
print min(x)
print max(x)

# first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]

# new list. sort list, split in half, push list created from first half to position 0 from second half
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
list_1 = x[0:len(x)/2]
print list_1
list_2 = x[len(x)/2:len(x)]
print list_2
list_2.insert(0, list_1)
print list_2




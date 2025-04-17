##python list operations.
#version1
#@auth Ziyad Jenkin
#7/3/25 2:41pm

#create a list of numbers 1-10 numlist = []

number_list = [1,2,3,4,5,6,7,8,9,10]
#print all elements of the list using a FOR loop
for i in number_list:
    print(i)
    continue
#continue from usual break into nl.append, add as per instructions 11,12,13 and remove 5, then reprint list.
number_list.append(11)
number_list.append(12)
number_list.append(13)
number_list.remove(5)
print(number_list)
   
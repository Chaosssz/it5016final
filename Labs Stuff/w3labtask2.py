##Python dictionary operations.
# version2
# @auth Ziyad Jenkin
# 7/3/25 3:04pm

#create a dictionary with the following key:value pairs name:alice age:25 city: auckland

dictionary = {
    "name": "Alice",
    "age": 25,
    "city": "Auckland"

}
#append dictionary to update and include email key val pair, then print.
dictionary.update({"Email":"alice99@gmail.com"})
print(dictionary)
#dictionary.update({"age:26})
dictionary.update({"age":26})
print(dictionary)

#END 3.15pm
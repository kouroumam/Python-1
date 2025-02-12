

#Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,]

result = common_elements(list1, list2)
print(result)

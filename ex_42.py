def intersection(list1,list2):
	list3 = [value for value in list1 if value in list2]
	return list3

def intersection_set(list1,list2):
	#list3 = set(list1) & set(list2)
	#return list3
	return list(set(list1) & set(list2))

def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


list1=[4,9,1,17,11,26,28,54,69]
list2=[9,9,74,21,45,11,63,28,26]
print(intersection(list1,list2))
print(intersection_set(list1,list2))
print(Intersection(list1,list2))
engineers=set(["John","Jane","Jack","Janice"])
programmers=set(["Jack","Sam","Susan","Janice"])
employees=engineers | programmers
print(employees)
print(type(employees))
engineers.add('Marvin')
print(engineers)
print(employees)
employees.update(engineers)
print(employees)
managers=set(['Jane','Jack','Susan','zack'])
engineering_management=engineers & managers
print(engineering_management)

for group in [engineers,programmers,employees,managers]:
	group.discard('Susan')
	print(group)

for group in [engineers,programmers,employees,managers]:
	print(type(group))
	group.discard('Susan')
	print(group)

	
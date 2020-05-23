# BRIEF
# Take list of names and convert them to Employee object

import people

employees = []

with open('./Miscellaneous/Names.txt', 'r') as names:
    for name in names.read().split('\n'):
        first, last = name.split(' ')
        emp = people.Employee(first, last)
        employees.append(emp)

print(employees)
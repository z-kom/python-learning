name = 'Someone'
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)


age = str(age)
print(age)
print(str(age))

age += '1'
age = str(age)
print(age)

name = bool(name)
print(name)

name = ''
name = bool(name)
print(name)

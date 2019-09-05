course = "'python's course for Beginners'"
multi_line = '''hi jhon
this is the support team
thank you for support'''
print(course)
print(multi_line[0])
print(multi_line[-1]) #index from last
print(multi_line[0:3])#all index from 0 to 2 exclude 3
print(multi_line[0:])# all index from 0 to end
print(multi_line[:])#all from start to end

name='jennifer'
print(name[1:-1]) #all values from 1 to last but one "ennife"

first='Gautham'
last='Smith'
msg=f'{first}[{last}] is a coder'
print(msg)
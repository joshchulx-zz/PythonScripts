"""Method number 1"""
import os
path = r"C:\Users\JoshPC\Desktop"

file_name = os.path.join(path, "binds.cgi")
my_file = open(file_name)
my_file_contents = my_file.read()

print(my_file_contents)


"""This is another other way. Simpler"""


import os
f =open('C:\\Users\\JoshPC\\Desktop\\test.txt', 'r')

file_data = f.read()

print(file_data)

f.close()

"""Once we are finished with the file f we should close it. 
This will free up any system resources taken up by the file"""

""" open a file, perform the operations in the block below the with statement (in this case read from the file) and afterwards Python closes it for us.
No need to call f.close()!"""

with open('C:\\Users\\JoshPC\\Desktop\\test.txt', 'r') as f:
    file_data = f.read()
print(file_data)
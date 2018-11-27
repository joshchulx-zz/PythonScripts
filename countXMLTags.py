"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""


#  Define the tag_count function
def tag_count(xml_count):
    count = 0
    for xml in xml_count:
        if xml[0] == '<' and xml[-1] == '>':
            count += 1
    return count

#or use this

def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
# put your code here.
text = open('test.txt')

list_of_lines = []

for line in text:
    line = line.rstrip()
    line = line.split(' ')
    list_of_lines.append(line)

print list_of_lines
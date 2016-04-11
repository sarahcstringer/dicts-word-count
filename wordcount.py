# put your code here.
text = open('test.txt')

list_of_lines = []

for line in text:
    line = line.rstrip()
    line = line.split(' ')
    list_of_lines.append(line)

# return list_of_lines

# print list_of_lines

word_dict = {}

for line in list_of_lines:
    for word in line:
        value = word_dict.get(word, 0)
        if value == 0:
            word_dict[word] = 1
        else:
            word_dict[word] = value + 1

for word, count in word_dict.items():
    print "%s %d" % (word, count)


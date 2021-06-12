print("Deepshikha 1803010075")
l1 = ['a', 'b', 'c', 'd']
with open('file1.txt', "w") as textfile:
        for c in l1:
                textfile.write("%s\n" % c)

content = open('file1.txt')
print(content.read())

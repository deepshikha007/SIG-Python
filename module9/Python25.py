print("Deepshikha 1803010075")
file =  open("file2.txt", "a")
file.write("Guido van Rossum\n")
file.close()

appended_file = open("file2.txt", "r")
print(appended_file.read())
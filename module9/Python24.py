print("Deepshikha 1803010075")
def file_read(fname,n,mode='r+'):
	with open(fname) as f:
		for i in range(n):
			print(f.readline())

file_read('file2.txt',2)
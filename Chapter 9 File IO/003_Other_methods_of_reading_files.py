file = open("Prachi.txt", 'r')
a = file.readline()  # Reads one line at a time from the file
print(a)
b = file.readlines()  # Reads complete file and returns a list when printed
print(b)
file.close()
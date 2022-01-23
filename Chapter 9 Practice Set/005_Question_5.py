file = open("log.txt", 'r')
a = file.read()

if 'python' in a:
    print("'python' word is present in the file")
else:
    print("'python' word is not present in the file")
file.close()
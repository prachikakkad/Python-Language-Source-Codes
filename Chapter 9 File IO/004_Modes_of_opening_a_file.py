file1 = open('Prachi.txt', 'r')
a = file1.read()
print(a)
file1.close()

file2 = open('Prachi.txt', 'w')
b = file2.write("I want to become a successful programmer in my life.")
print(b)  # will print the number of characters written
file2.close()

# file3 = open('Prachi_Intro.txt', 'x')
# c = file3.write("My name is Prachi.\nMy hobby is coding and programming.")
# print(c)

file4 = open('Prachi.txt', 'a')
d = file4.write("My name is Prachi")
print(d)

file5 = open('Prachi.txt', 'rb')
e = file5.read()
print(e)

file6 = open('Prachi.txt', 'rt')
f = file6.read()
print(f)

file7 = open('Prachi.txt', 'r+')
h = file7.write("Prachi")
g = file7.read()
print(g)


file1.close()
file2.close()
file4.close()
file5.close()
file6.close()
file7.close()
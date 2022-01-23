file = open("Prachi.txt", 'r')
text = file.read()
print(text)
file.close()

# We can also specify the number of characters in read() function :-

file = open("Prachi.txt", 'r')
text_extra = file.read(2)  # Reads first 2 characters
print(text_extra)
file.close()
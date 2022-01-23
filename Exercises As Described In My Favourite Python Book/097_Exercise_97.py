# Question :-
"""You can use the replace() method to replace any word in a string with a different word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'

Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as Java. Printeach modified line to the screen."""

with open("Extra_file_for_Exercise_97.txt" , "r") as mode:
    content = mode.readlines()
for line in content:
    line = line.rstrip()
    print(line.replace("Python" , "Java"))
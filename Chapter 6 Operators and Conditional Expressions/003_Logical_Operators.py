a = False
b = True

print(a and a)  # Returns false as both operands are false
print(b and b)  # Returns true as both operands are true
print(a and b)  # Returns false as one operand is true and one operand is false
print(b or a)  # Returns true as one operand is true and one operand is false
print(a or a)  # Returns false as both operands are false
print(b or b)  # Returns true as both operands are true
print(not b)  # Returns false as it reverses the correct state
print(not a)  # Returns true as it reverses the correct state
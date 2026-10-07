import re
text = (input("Enter the text:"))
word = (input("Enter the word to split:"))

s = re.split(rf"{word}", text)
print(s)
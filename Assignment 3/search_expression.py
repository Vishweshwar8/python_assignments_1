import re
text = (input("Enter the text:"))

x = re.search(r"\d+",text)
print(x.group())


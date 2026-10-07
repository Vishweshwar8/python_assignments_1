import re
text=(input("Enter the text: "))

num = re.findall(r"\d+", text)
print(num)
word = re.findall(r"[A-Z][a-z]+", text)
print(word)

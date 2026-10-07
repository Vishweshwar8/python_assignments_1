import re 
text=(input("Enter the text: "))
start = (input("Enter the starting word: "))
match = re.match(rf"{start}", text)

if match:
    print("Match found:", match.group())
else:
    print("word not found.")

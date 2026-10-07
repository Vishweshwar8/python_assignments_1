import re
text=(input("Enter the date: "))
date = r"(\d{2})/(\d{2})/(\d{4})"
m = re.search(date, text)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))






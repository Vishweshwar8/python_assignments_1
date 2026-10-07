import re
text=(input("Enter the email: "))
e = re.match(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}",text) 
if e:
    print(e.group())
else:
    print("your email id is not valid")
    

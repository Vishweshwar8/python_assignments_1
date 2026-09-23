def convert(celsius):
    return (celsius*9/5)+32

celsius = float(input("enter the temp. in celsius: "))
print("temperature in celsius ", celsius, "C")

f = convert(celsius)
print("temperature in fahrenheit", f, "F")
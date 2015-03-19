print("Welcome to Fahrenheit to Celsius Program")
fah = float(input("Please give us a temperature in Fahrenheit. "))
cel = round((fah - 32) * 5 / 9, 1)
print("The temperature in Celsius is {}".format(cel))
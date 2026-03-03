# add 2 lists, one for each measurement option Celsius and Fahrenheit

celsius_temperatures = []
fahrenheit_temperatures = []

# get 3 values from user input

for i in range(3):   # modify this for more inputs
    value = float(input("Enter Celsius: "))
    celsius_temperatures.append(value)

# convert values from Celsius to Fahrenheit

for celsius in celsius_temperatures:   # reverse according to your needs
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temperatures.append(fahrenheit)

# print the results for both measurements

print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)

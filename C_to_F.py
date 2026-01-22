celsius_temperatures = []
fahrenheit_temperatures = []

# get values from user
for i in range(3):
    value = float(input("Enter Celsius: "))
    celsius_temperatures.append(value)

# convert values
for celsius in celsius_temperatures:
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_temperatures.append(fahrenheit)

print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)

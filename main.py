import math


def temperature_converter():
    question = str(input("Do you want to convert Celsius to Fahrenheit or Fahrenheit to Celsius? : "))
    if question == "Celsius to Fahrenheit" or "celsius to fehrenheit":
        Celsius = float(input("Enter a temperature in Celsius: "))
        Fahrenheit = ((9.0/5.0 * Celsius) + 32)
        print("Temperature in Fahrenheit is: ", Fahrenheit)
    elif question == "Fahrenheit to Celsius" or "fahrenheit to celsius":
        Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
        Celsius = ((Fahrenheit - 32) / 1.8)
        print("Temperature in Celsius is: ", Celsius)
    

temperature_converter()

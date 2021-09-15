#super simple temperature converter

def converter():

    question = str(input("Do you want to convert Celsius to Fahrenheit or Fahrenheit to Celsius? : ")).upper()

    if question == "CELSIUS TO FAHRENHEIT":
        Celsius = float(input("Enter a temperature in Celsius: "))
        Fahrenheit = ((9.0/5.0 * Celsius) + 32)
        print("Temperature in Fahrenheit is: ", Fahrenheit)

    elif question == "FAHRENHEIT TO CELSIUS":
        Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
        Celsius = ((Fahrenheit - 32) / 1.8)
        print("Temperature in Celsius is: ", Celsius)

    else:
        print("Invalid input, aborting.")

    quit()

converter()

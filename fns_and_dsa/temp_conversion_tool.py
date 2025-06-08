# Global variables 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert temperature from Fahrenheit to Celcius
def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius


def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
 

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip()

        if choice == "F":
            celcius = convert_to_celcius(temperature)
            print(f"{temperature}°F is {celcius}°C")

        elif choice == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")

        else:
            print("Invalid choice. Please enter 'C' for Celcius or 'F' for Fahrenheit")
        
    except ValueError:        
        print("Invalid temperature. Please enter a numeric value.")


# Run the program
if __name__ == "__main__":
    main()

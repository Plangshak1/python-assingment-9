# ===== TASK 3: Temperature Converter =====
# Create a custom TemperatureError exception
# The function should convert Celsius to Fahrenheit and raise TemperatureError if:
# - Temperature is below absolute zero (-273.15°C)
# - Temperature is above the surface of the sun (5500°C)
# If input is not a number, raise ValueError with message "Error: invalid temperature"
# Keep asking until a valid temperature is entered

print("=== Task 3: Temperature Converter ===")
print("Enter temperature in Celsius (must be between -273.15°C and 5500°C)\n")


class TemperatureError(Exception):   #our custom exception
    """Custom exception for invalid temperature ranges."""
    pass

def convert_temperature(prompt):
    while True:
        try:
            value = input(prompt).strip()
            
            if not value:            # Check for empty input
                raise ValueError("Error: invalid temperature")
            
            celsius = float(value)   # converting to float
            
            
            if celsius < -273.15:    # Validate range
                raise TemperatureError("Error: temperature cannot be below absolute zero (-273.15°C)")
            if celsius > 5500:
                raise TemperatureError("Error: temperature cannot be above the surface of the sun (5500°C)")
            
            return celsius
        
        except ValueError as e:
            print(e)
        except TemperatureError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")

# Using our function
celsius = convert_temperature("Enter your temperature in Celsius: ")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F\n")


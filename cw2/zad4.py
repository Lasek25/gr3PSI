def temp_converter(temperature_type, temperature):
    temperature_type = str.capitalize(temperature_type)
    if temperature_type == "Fahrenheit":
        return round(32.00 + 1.8 * temperature, 2)
    elif temperature_type == "Rankine":
        return round(1.8 * (temperature + 273.15), 2)
    elif temperature_type == "Kelvin":
        return temperature + 273.15
    else:
        return "Incorrect temperature type, you can convert degree Celsius only for Fahrenheit, Rankine and Kelvin."


print(temp_converter("fahrenheit", 2.6))

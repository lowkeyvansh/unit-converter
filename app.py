def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "km_to_miles": 0.621371,
        "miles_to_km": 1.60934,
        "kg_to_lbs": 2.20462,
        "lbs_to_kg": 0.453592,
        "c_to_f": lambda c: (c * 9/5) + 32,
        "f_to_c": lambda f: (f - 32) * 5/9
    }
    
    key = f"{from_unit}_to_{to_unit}"
    factor = conversion_factors.get(key)
    
    if isinstance(factor, float):
        return value * factor
    elif callable(factor):
        return factor(value)
    else:
        return None

value = float(input("Enter value: "))
from_unit = input("Enter from unit (km, miles, kg, lbs, c, f): ")
to_unit = input("Enter to unit (km, miles, kg, lbs, c, f): ")
result = convert_units(value, from_unit, to_unit)
if result is not None:
    print(f"Converted value: {result}")
else:
    print("Invalid conversion")

import unittest
from conversions import (convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToCelsius, convertFahrenheitToKelvin, convertKelvinToCelsius, convertKelvinToFahrenheit)

# Step 01 Create Tests for Celsius Conversion
class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)
        self.assertEqual(convertCelsiusToKelvin(100.0), 373.15)
        self.assertEqual(convertCelsiusToKelvin(-40.0), 233.15)
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)
        self.assertEqual(convertCelsiusToKelvin(-273.15), 0.0)

    def test_convertCelsiusToFahrenheit(self):
        self.assertEqual(convertCelsiusToFahrenheit(0.0), 32.0)
        self.assertEqual(convertCelsiusToFahrenheit(100.0), 212.0)
        self.assertEqual(convertCelsiusToFahrenheit(-40.0), -40.0)
        self.assertEqual(convertCelsiusToFahrenheit(300.0), 512.0)
        self.assertEqual(convertCelsiusToFahrenheit(-273.15), -459.67)

# Step 03  Repeat
    def test_convertFahrenheitToCelsius(self):
        self.assertEqual(convertFahrenheitToCelsius(32.0), 0.0)
        self.assertEqual(convertFahrenheitToCelsius(212.0), 100.0)
        self.assertEqual(convertFahrenheitToCelsius(-40.0), -40.0)
        self.assertEqual(convertFahrenheitToCelsius(572.0), 300.0)
        self.assertEqual(convertFahrenheitToCelsius(-459.67), -273.15)
    
    def test_convertFahrenheitToKelvin(self):
        self.assertEqual(convertFahrenheitToKelvin(32.0), 0.0)
        self.assertEqual(convertFahrenheitToKelvin(212.0), 373.15)
        self.assertEqual(convertFahrenheitToKelvin(-40.0), 233.15)
        self.assertEqual(convertFahrenheitToKelvin(300.0), 512.0)
        self.assertEqual(convertFahrenheitToKelvin(572.0), 573.15)
        self.assertEqual(convertFahrenheitToKelvin(-459.67), 0.0)
    
    def test_convertKelvinToCelsius(self):
        self.assertEqual(convertKelvinToCelsius(273.15), 0.0)
        self.assertEqual(convertKelvinToCelsius(373.15), 100.0)
        self.assertEqual(convertKelvinToCelsius(233.15), -40.0)
        self.assertEqual(convertKelvinToCelsius(573.15), 300.0)
        self.assertEqual(convertKelvinToCelsius(0.0), -273.15)

    def test_convertKelvinToFahrenheit(self):
        self.assertEqual(convertKelvinToFahrenheit(273.15), 32.0)
        self.assertEqual(convertKelvinToFahrenheit(373.15), 212.0)
        self.assertEqual(convertKelvinToFahrenheit(233.15), -40.0)
        self.assertEqual(convertKelvinToFahrenheit(300.0), 512.0)
        self.assertEqual(convertKelvinToFahrenheit(573.15), 572.0)
        self.assertEqual(convertKelvinToFahrenheit(0.0), -459.67)

# Step 04 Refactor
class ConversionNotPossible(Exception):
    pass

def convert(value, from_unit, to_unit):
    conversions = {
        'celsius': {'kelvin': lambda x: x + 273.15, 'fahrenheit': lambda x: (x * 9/5) + 32},
        'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15},
        'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32},
        'meters': {'miles': lambda x: x / 1609.34, 'yards': lambda x: x * 0.9144},
        'yards': {'miles': lambda x: x / 1760, 'meters': lambda x: x * 0.9144},
        'miles': {'yards': lambda x: x / 1760, 'meters': lambda x: x * 1609.34}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        raise ConversionNotPossible("Conversion not possible")

    return conversions[from_unit][to_unit](value)

if __name__ == '__main__':
    unittest.main()

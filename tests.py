# Step 02 Implement the Celsius Conversion Functions
def convertCelsiustoKelvin(celsius):
    return celsius + 273.15

def convertCelsiustoFahrenheit(celsius):
    return (celsius * 9/5) + 32

def test_convert(self):
    self.assertEstimateConversion(convert(0, 'celsius', 'kelvin'), 273.15)
    self.assertEstimateConversion(convert(100, 'celsius', 'fahrenheit'), 212.0)
    self.assertEstimateConversion(convert(32, 'fahrenheit', 'celsius'), 0.0)
    self.assertEstimateConversion(convert(273.15, 'kelvin', 'celsius'), 0.0)
    self.assertEstimateConversion(convert(1, 'meters', 'miles'), 0.000621371)
    self.assertEstimateConversion(convert(1, 'yards', 'meters'), 0.9144)
    self.assertEstimateConversion(convert(1, 'miles', 'yards'), 1760.0)

    with self.assertRaises(ConversionNotPossible):
        convert(1, 'celsius', 'miles')
let tempFi = input.temperature(TemperatureUnit.Fahrenheit)
let tempF = 80
// while True:
// print("Temperature (F): " + input.temperature(TemperatureUnit.FAHRENHEIT) + " - Temperature (C): " + input.temperature(TemperatureUnit.CELSIUS))
// print("Current Room Temperature: " + input.temperature(TemperatureUnit.FAHRENHEIT) + "°F - " + input.temperature(TemperatureUnit.CELSIUS) + "°C")
// if tempF > 60:
// light.set_pixel_color(5, light.rgb(0, 255, 0))
if (tempFi > 90) {
    light.setPixelColor(5, light.rgb(255, 0, 0))
} else if (tempFi > 40) {
    light.setPixelColor(5, light.rgb(0, 255, 0))
} else {
    light.setPixelColor(5, light.rgb(0, 0, 255))
}


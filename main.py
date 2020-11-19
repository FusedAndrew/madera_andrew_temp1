tempFi = input.temperature(TemperatureUnit.FAHRENHEIT)
tempF = 80
#while True:
    #print("Temperature (F): " + input.temperature(TemperatureUnit.FAHRENHEIT) + " - Temperature (C): " + input.temperature(TemperatureUnit.CELSIUS))
    #print("Current Room Temperature: " + input.temperature(TemperatureUnit.FAHRENHEIT) + "°F - " + input.temperature(TemperatureUnit.CELSIUS) + "°C")


#if tempF > 60:
    #light.set_pixel_color(5, light.rgb(0, 255, 0))

if tempFi > 90:
    light.set_pixel_color(5, light.rgb(255, 0, 0))
elif tempFi > 40:
    light.set_pixel_color(5, light.rgb(0, 255, 0))
else:
    light.set_pixel_color(5, light.rgb(0, 0, 255))

#if tempF > 70:
    #light.set_all(light.rgb(255,0,0))
#elif tempF > 40:
    #light.set_all(light.rgb(0,255,0))
#else:
    #ight.set_all(light.rgb(0,0,255))


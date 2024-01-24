# Importing requests library to send HTTP requests
import os
import requests

while True:
    # Taking user input for city or pincode
    user_input = input("Enter City\\PinCode (or 'exit' to quit):\n")

    os.system("cls")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break


    # Sending GET request to OpenWeatherMap API
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID=ea852292d5ebc4f430074425f5cff957")



    if (weather_data.status_code == 200):
        # Extracting city name from the response
        city_name = weather_data.json()['name']

        # Extracting country code from the response
        country = weather_data.json()['sys']['country']

        # Extracting longitude and latitude from the response
        Location_lon = weather_data.json()['coord']['lon']
        Location_lat = weather_data.json()['coord']['lat']

        # Extracting weather type from the response
        weather = weather_data.json()['weather'][0]['main']

        # Extracting temperature from the response
        temp = str(weather_data.json()['main']['temp']) + " °C"

        # Extracting maximum temperature from the response
        temp_max = str(weather_data.json()['main']['temp_max']) + " °C"

        # Extracting minimum temperature from the response
        temp_min = str(weather_data.json()['main']['temp_min']) + " °C"

        # Extracting atmospheric pressure from the response
        pressure = str((weather_data.json()['main']['pressure'])/1000) + " bar"

        # Extracting humidity from the response
        humidity = str(weather_data.json()["main"]["humidity"]) + " %"

        # Extracting wind speed from the response
        wind_speed = str(weather_data.json()['wind']['speed']) +" m/s"

        # Printing the weather information
        print("\nWeather Information for "+city_name+","+country+":- \nLongitude: ", Location_lon, "\nLatitude: ", Location_lat,"\nWeather Type:",weather,"\nTemperature: ", temp,"\nMaximum Temperation: ", temp_max,"\nMinimum Temperature: ", temp_min,"\nAtmospheric Pressure: ", pressure,"\nHumidity: ", humidity ,"\nWind Speed: ", wind_speed,"\n\n" )

    else:
        print("City not found! Please enter a valid city\\PinCode.\n\n")
import requests, json, time
import threading

api_key = "YOUR_OPENWEATHERMAP_API_KEY"

base_url = "http://api.openweathermap.org/data/2.5/weather?"



city_name = "Tuy, Batangas"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
#response = requests.get(complete_url)
#x = response.json()

nas_town = "sydney"
second_url = base_url + "appid=" + api_key + "&q=" + nas_town + "&units=metric"


bal_town = "Balayan, Batangas"
bal_url = base_url + "appid=" + api_key + "&q=" + bal_town + "&units=metric"

cal_town = "Calatagan, Batangas"
cal_url = base_url + "appid=" + api_key + "&q=" + cal_town + "&units=metric"

lian_town = "Lian, Batangas"
lian_url = base_url + "appid=" + api_key + "&q=" + lian_town + "&units=metric"


def refresher():
    global x, y, current_temperature, current_humidity, winddddd, feeling, z, weather_description, po
    global nas_x, nas_y, nas_current_temperature, nas_current_humidity, nas_winddddd, nas_z, nas_po, nas_weather_description, nas_feel
    global bal_x, bal_y, bal_current_temperature, bal_current_humidity, bal_winddddd, bal_z, bal_po, bal_weather_description, bal_feeling
    global cal_x, cal_y, cal_current_temperature, cal_current_humidity, cal_winddddd, cal_z, cal_po, cal_weather_description, cal_feeling
    global lian_x, lian_y, lian_current_temperature, lian_current_humidity, lian_winddddd, lian_z, lian_po, lian_weather_description, lian_feeling

    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":   
        y = x["main"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        winddddd = x["wind"]
        feeling = y["feels_like"]

        z = x["weather"]

        weather_description = z[0]["description"]
        test = winddddd["speed"]
        po = test * 3.6
        po = round(po, 2)
    else:
        print("City not found")



    nas = requests.get(second_url)
    nas_x = nas.json()

    if nas_x["cod"] != "404":   
        nas_y = nas_x["main"]
        nas_current_temperature = nas_y["temp"] 
        #nas_current_pressure = nas_y["pressure"]
        nas_current_humidity = nas_y["humidity"]
        nas_winddddd = nas_x["wind"]
        nas_feel = nas_y["feels_like"]
        nas_z = nas_x["weather"]
        
        #windy = winddddd[0]

        nas_weather_description = nas_z[0]["description"]

        nas_test = nas_winddddd["speed"]
        nas_po = nas_test * 3.6
        nas_po = round(nas_po, 2)
        #print("wind = " + str(nas_po))
    else:
        print("City not found")


    cal_response = requests.get(cal_url)
    cal_x = cal_response.json()
    if cal_x["cod"] != "404":   
        cal_y = cal_x["main"]
        cal_current_temperature = cal_y["temp"]
        cal_current_humidity = cal_y["humidity"]
        cal_winddddd = cal_x["wind"]
        cal_feeling = cal_y["feels_like"]

        cal_z = cal_x["weather"]

        cal_weather_description = cal_z[0]["description"]
        cal_test = cal_winddddd["speed"]
        cal_po = cal_test * 3.6
        cal_po = round(cal_po, 2)
    else:
        print("City not found")




    lian_response = requests.get(lian_url)
    lian_x = lian_response.json()
    if lian_x["cod"] != "404":   
        lian_y = lian_x["main"]
        lian_current_temperature = lian_y["temp"]
        lian_current_humidity = lian_y["humidity"]
        lian_winddddd = lian_x["wind"]
        lian_feeling = lian_y["feels_like"]

        lian_z = lian_x["weather"]

        lian_weather_description = lian_z[0]["description"]
        lian_test = lian_winddddd["speed"]
        lian_po = lian_test * 3.6
        lian_po = round(lian_po, 2)
    else:
        print("City not found")


    bal_response = requests.get(bal_url)
    bal_x = bal_response.json()
    if bal_x["cod"] != "404":   
        bal_y = bal_x["main"]
        bal_current_temperature = bal_y["temp"]
        bal_current_humidity = bal_y["humidity"]
        bal_winddddd = bal_x["wind"]
        bal_feeling = bal_y["feels_like"]

        bal_z = bal_x["weather"]

        bal_weather_description = bal_z[0]["description"]
        bal_test = bal_winddddd["speed"]
        bal_po = bal_test * 3.6
        bal_po = round(bal_po, 2)
    else:
        print("City not found")



eat_code = "https://c4.wallpaperflare.com/wallpaper/851/501/292/programming-code-minimalism-wallpaper-preview.jpg"
broken_clouds = "https://live.staticflickr.com/1828/28636482297_bd428f26e8_b.jpg"
misted = "https://www.mistmedia.com/wp-content/uploads/revslider/hero_1/hero_bg.jpg"
thunderstorm = "https://www.farmersalmanac.com/wp-content/uploads/2015/06/Best-Places-Cities-Lightning-A193502306.jpg"
raining = "https://www.wkbn.com/wp-content/uploads/sites/48/2020/02/rain-drops-umbrella-raining-storm-weather-generic.jpg"
shower_rain = "https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/images/weather/learn-about/weather/rain-storm.jpg"
scattered_cloud = "https://thegreekobserver.com/home/wp-content/uploads/2017/09/greece-weather-clouds.jpg"
few_cloud = "https://photo-cdn.icons8.com/assets/previews/719/f52db576-41d8-4851-821d-cb443055099e1x.jpg"
clear_sky = "https://www.softwareheritage.org/wp-content/uploads/2017/12/clearsky.png"
over_cast = "https://motionarray.imgix.net/preview-2552HDatpQAczN_0006.jpg"
moderate_rain = "https://gulfbusiness.com/wp-content/uploads/2019/03/rain-Dubai-6.jpg"


def weather_image(coord):
    if globals()['{}_weather_description'.format(coord)] == "broken clouds":
        final_result = broken_clouds
    elif globals()['{}_weather_description'.format(coord)] == "clear sky":
        final_result = clear_sky
    elif globals()['{}_weather_description'.format(coord)] == "few clouds":
        final_result = few_cloud
    elif globals()['{}_weather_description'.format(coord)] == "scattered clouds":
        final_result = scattered_cloud
    elif globals()['{}_weather_description'.format(coord)] == "shower rain":
        final_result = shower_rain
    elif globals()['{}_weather_description'.format(coord)] == "rain":
        final_result = raining
    elif globals()['{}_weather_description'.format(coord)] == "thunderstorm":
        final_result = thunderstorm
    elif globals()['{}_weather_description'.format(coord)] == "mist":
        final_result = misted
    elif globals()['{}_weather_description'.format(coord)] == "overcast clouds":
        final_result = over_cast
    elif globals()['{}_weather_description'.format(coord)] == "moderate rain":
        final_result = moderate_rain
    else:
        final_result = eat_code

    return final_result
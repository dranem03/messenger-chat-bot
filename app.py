import os
import random
import speedtest
from flask import Flask, request
from pymessenger.bot import Bot
import modules.hackermode as ghack
import json
import weather
from time import sleep
from cachetools import TTLCache

app = Flask(__name__)
ACCESS_TOKEN = 'YOUR_FACEBOOK_PAGE_ACCESS_TOKEN'
VERIFY_TOKEN = 'YOUR_VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

cache = TTLCache(maxsize=256, ttl=120)

sms_na = []



quicks = [
    {
        "content_type":"text",
        "title":"👌 Yes",
        "payload":"quick_yes",
    },{
        "content_type":"text",
        "title":"✋🏻 No",
        "payload":"quick_no"
    }
]

hour_loc = [
    {
        "content_type":"text",
        "title":"Tuy",
        "payload":"hour_tuy"
    },{
        "content_type":"text",
        "title":"Nasugbu",
        "payload":"hour_nasugbu"
    },{
        "content_type":"text",
        "title":"Balayan",
        "payload":"hour_balayan"
    },{
        "content_type":"text",
        "title":"Calatagan",
        "payload":"hour_calatagan"
    },{
        "content_type":"text",
        "title":"Lian",
        "payload":"hour_lian"
    }
]


daily_loc = [
    {
        "content_type":"text",
        "title":"Tuy",
        "payload":"daily_tuy"
    },{
        "content_type":"text",
        "title":"Nasugbu",
        "payload":"daily_nasugbu"
    },{
        "content_type":"text",
        "title":"Balayan",
        "payload":"daily_balayan"
    },{
        "content_type":"text",
        "title":"Calatagan",
        "payload":"daily_calatagan"
    },{
        "content_type":"text",
        "title":"Lian",
        "payload":"daily_lian"
    }
]



for_type = [
    {
        "content_type":"text",
        "title":"🕰 Hourly",
        "payload":"type_hour"
    },{
        "content_type":"text",
        "title":"🌅 Daily Forecast",
        "payload":"type_daily"
    },{
        "content_type":"text",
        "title":"Maybe Later",
        "payload":"type_maybe"
    }
]


button1 = [
    {
        "type": "postback",
        "title": "Yes",
        "payload": "button1_yes"
    },
    {
        "type": "postback",
        "title": "No",
        "payload": "button1_no"
    }
]


greets = [
    {
        "greeting":[
            {
                "locale":"default",
                "text":"Hello {{user_first_name}}, I'm always at your service"
            }
        ]
    }
]




@app.route('/', methods=['GET', 'POST'])

def receive_message():
    datos = {
        "persistent_menu":[
        {
        "locale":"default",
        "call_to_actions":[
            {
              "title": "💻 Hacker Mode",
              "type": "nested",
              "call_to_actions": [
                  {
                      "title": "✍️ SMS Mode",
                      "type": "postback",
                      "payload": "sms_mode"
                  },
                  {
                      "title": "🌤 Weather",
                      "type": "postback",
                      "payload": "daily_dose"
                  },
                  {
                      "title": "✈️ Dream",
                      "type": "postback",
                      "payload": "get_your_dream"
                  }
              ]
            },
            {
                "title": "💻 Server Speed Test",
                "type": "postback",
                "payload": "test_mode"
            }
        ]
    }
    ]
    }

    gs_data = {
    "get_started":{
        "payload": "get_started"
    }
    }

    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        data = request.get_json()
        print(data)
        if data["object"] == "page":
            for entry in data['entry']:
                for messaging_event in entry['messaging']:
                    mypayload = (messaging_event.get("message", {}).get("quick_reply", {}).get("payload"))

                    recipient_id = messaging_event['sender']['id']
                    #message_id = messaging_event['message'].get('id')
                    bot.set_get_started(gs_data)
                    bot.send_raw(greets)
                    bot.set_persistent_menu(datos)
        
                    if mypayload == "quick_yes":
                        send_message(recipient_id, "Running speedtest . . .")
                        server_speed(recipient_id)
                        send_message(recipient_id, "Server speedtest done.")
                    elif mypayload == "quick_no":
                        send_message(recipient_id, "Happy coding master.")
                    elif mypayload == "type_hour":
                        but = raw_your_boat(recipient_id, "🗺 Location:", hour_loc)
                        bot.send_raw(but)
                    elif mypayload == "type_daily":
                        but = raw_your_boat(recipient_id, "🗺 Location:", daily_loc)
                        bot.send_raw(but)
                    elif mypayload == "type_maybe":
                        send_message(recipient_id, "Happy coding👨🏼‍💻")
                    elif messaging_event.get("message"):
                        liham = messaging_event['message'].get('text')
                        #msgid = messaging_event['message'].get('mid')
                        liham_convert = str(liham)
                        sms_na.append(liham)
                        if liham == "random":
                            randmsg = judgersss()
                            tambay = "Random number: {}".format(randmsg)
                            send_message(recipient_id, tambay)
                        elif liham_convert == "load":
                            send_message(recipient_id, "this is unique")
                        elif liham_convert.split()[0] == "/img":
                            getme = cache.get('{}_cache'.format(recipient_id))
                            if len(liham_convert.split()) > 1:
                                if liham_convert.split()[-1].isdigit() == True:
                                    num_result = liham_convert.split()[-1]
                                    img_search = liham_convert.split(' ', 1)[1].rsplit(' ', 1)[0]
                                    if int(num_result) <= 20 and int(num_result) >= 1:
                                        choser = int(num_result)
                                        if choser <= 10:
                                            ghack.google_img(recipient_id, img_search, num_result)
                                        elif choser > 10 and choser <= 20:
                                            ghack.more_img(recipient_id, img_search, num_result)
                                            
                                        if ghack.cacher['{}_result_cache'.format(recipient_id)][0] != "sorry_not_found":
                                            if getme:
                                                if getme == liham_convert:
                                                    print("custom result - wait for 2 minutes")
                                                else:
                                                    print("custom result - wait for 2 minutes")
                                                    send_message(recipient_id, "Please wait 2 minutes before searching again . . .")
                                            else:
                                                cache['{}_cache'.format(recipient_id)] = liham_convert
                                                for resulta in ghack.cacher['{}_result_cache'.format(recipient_id)]:
                                                    bot.send_image_url(recipient_id, resulta)
                                        else:
                                            bot.send_image_url(recipient_id, ghack.cacher['{}_result_cache'.format(recipient_id)][1])
                                            send_message(recipient_id, "Sorry, image not found . . .")
                                    else:
                                        send_message(recipient_id, "Maximum search result is 20 and minimum search result is 1")
                                else:
                                    img_search = liham_convert.split(' ', 1)[1]
                                    ghack.google_img(recipient_id, img_search, 3)
                                    if ghack.cacher['{}_result_cache'.format(recipient_id)][0] != "sorry_not_found":                                        
                                        if getme:
                                            if getme == liham_convert:
                                                #send_message(recipient_id, "Please wait 2 minutes before searching again . . .")
                                                print("wait 2 minutes . . .")
                                            else:
                                                print("wait two minutes . . .")
                                                send_message(recipient_id, "Please wait 2 minutes before searching again . . .")
                                        else:
                                            cache['{}_cache'.format(recipient_id)] = liham_convert
                                            for resulta in ghack.cacher['{}_result_cache'.format(recipient_id)]:
                                                bot.send_image_url(recipient_id, resulta)
                                    else:
                                        bot.send_image_url(recipient_id, ghack.cacher['{}_result_cache'.format(recipient_id)][1])
                                        send_message(recipient_id, "Sorry, image not found . . .")
                            else:
                                send_message(recipient_id, "How to use:\n\n /img <image you want to find> <number of result: max 10 default is 3>\n\nExample:\n/img sports car 7\nor\n/img sports car")
                    
                        elif liham_convert.split()[0] == "/sms":
                            global sms_msg
                            if len(liham_convert.split()) > 1:                                
                                #sms_msg = "yow wassap"
                                sms_msg = liham.split(' ', 1)[1]
                                send_message(recipient_id, sms_msg)
                            else:
                                send_message(recipient_id, "wassap madlang pipsssss")
                        elif liham:
                            the_command = "python3 searcher.py text \"{}\" > searches/{}_search_result.txt".format(liham, recipient_id)
                            the_command2 = "python3 searcher.py image \"{}\" > searches/{}_image_result.txt".format(liham, recipient_id)
                            os.system(the_command)
                            os.system(the_command2)
                            im = open('searches/{}_image_result.txt'.format(recipient_id), 'r')
                            im_content = im.read()
                            bot.send_image_url(recipient_id, im_content)
                            im.close()
                            f = open('searches/{}_search_result.txt'.format(recipient_id),'r')
                            f_content = f.read()
                            send_message(recipient_id, f_content)
                            f.close()
                        elif messaging_event['message'].get('attachments'):
                            rand_num =  judgersss()
                            mess = "I will rate your picture {} out of 10.".format(rand_num)
                            send_message(recipient_id, mess)


                    if messaging_event.get("postback"):
                        hacker_msg = "you are in hacker mode"
                        #testttt = "you are in test mode"
                        payload = messaging_event["postback"]["payload"]
                        if payload == "hacker_mode":
                            send_message(recipient_id, hacker_msg)
                        elif payload == "test_mode":
                            rawme = raw_your_boat(recipient_id,"⚡️ Run the server internet speed test?",quicks)
                            bot.send_raw(rawme)
                        elif payload == "get_started":
                            send_generic(recipient_id)
                        elif payload == "sms_mode":
                            thesms = "This is what you type earlier: {}".format(sms_na)
                            send_message(recipient_id, thesms)
                        elif payload == "daily_dose":
                            forecast_message = raw_your_boat(recipient_id, "View forecast?", for_type)
                            mult_gen(recipient_id)
                            send_message(recipient_id, "That's the current weather today master🤪")
                            bot.send_raw(forecast_message)
                
    return "Message Processed"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def judgersss():
    return random.randint(1,10)

def random_photo(recipient_id):
    photos = ["https://files.wallpaperpass.com/2019/10/hacker wallpaper 128 - 1920x1080.jpg", "https://wallpaperaccess.com/full/896797.png", "https://media.gizmodo.co.uk/wp-content/uploads/2015/02/anonymous.jpg"]
    elements = [
        {
            "title": ". . . ",
            "image_url": random.choice(photos),
            "subtitle": "Master is my master."
        }
    ]
    bot.send_generic_message(recipient_id, elements)


def get_message():
    sample_responses = ["Nice", "Great job", "how are you?", "You can do it"]
    return random.choice(sample_responses)

def send_image_url(recipient_id, theimage):
    bot.send_image_url(recipient_id,theimage)
    return "success"


def server_speed(recipient_id):
    s = speedtest.Speedtest()
    servernames = []
    s.get_best_server(servernames)
    s.download()
    s.upload()
    s.results.ping
    final_result = s.results.share().rstrip()
    elements = [
        {
            "title": "Server Speedtest",
            "image_url": final_result,
            "subtitle": "This is your server current internet speed master."
        }
    ]
    bot.send_generic_message(recipient_id, elements)


def mult_gen(recipient_id):
    weather.refresher()
    #weather.relaodapi()
    #think_twice = "https://images4.alphacoders.com/587/thumb-1920-587777.png"
    eat_code = "https://c4.wallpaperflare.com/wallpaper/851/501/292/programming-code-minimalism-wallpaper-preview.jpg"
    broken_clouds = "https://live.staticflickr.com/1828/28636482297_bd428f26e8_b.jpg"
    misted = "https://www.mistmedia.com/wp-content/uploads/revslider/hero_1/hero_bg.jpg"
    thunderstorm = "https://www.farmersalmanac.com/wp-content/uploads/2015/06/Best-Places-Cities-Lightning-A193502306.jpg"
    raining = "https://www.wkbn.com/wp-content/uploads/sites/48/2020/02/rain-drops-umbrella-raining-storm-weather-generic.jpg"
    shower_rain = "https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/images/weather/learn-about/weather/rain-storm.jpg"
    scattered_cloud = "https://thegreekobserver.com/home/wp-content/uploads/2017/09/greece-weather-clouds.jpg"
    few_cloud = "https://photo-cdn.icons8.com/assets/previews/719/f52db576-41d8-4851-821d-cb443055099e1x.jpg"
    clear_sky = "https://www.softwareheritage.org/wp-content/uploads/2017/12/clearsky.png"
    
    final_result = "https://live.staticflickr.com/1828/28636482297_bd428f26e8_b.jpg"
    another_image = "http://openweathermap.org/img/wn/10d@2x.png"

    if weather.weather_description == "broken clouds":
        final_result = broken_clouds
    elif weather.weather_description == "clear sky":
        final_result = clear_sky
    elif weather.weather_description == "few clouds":
        final_result = few_cloud
    elif weather.weather_description == "scattered clouds":
        final_result = scattered_cloud
    elif weather.weather_description == "shower rain":
        final_result = shower_rain
    elif weather.weather_description == "rain":
        final_result = raining
    elif weather.weather_description == "thunderstorm":
        final_result = thunderstorm
    elif weather.weather_description == "mist":
        final_result = misted
    else:
        final_result = eat_code

    if weather.nas_weather_description == "mist":
        another_image = misted
    elif weather.nas_weather_description == "thunderstorm":
        another_image = thunderstorm
    elif weather.nas_weather_description == "rain":
        another_image = raining
    elif weather.nas_weather_description == "shower rain":
        another_image = shower_rain
    elif weather.nas_weather_description == "scattered clouds":
        another_image = scattered_cloud
    elif weather.nas_weather_description == "few clouds":
        another_image = few_cloud
    elif weather.nas_weather_description == "clear sky":
        another_image = clear_sky
    elif weather.nas_weather_description == "broken clouds":
        another_image = broken_clouds
    else:
        another_image = eat_code

    elements = [
        {
            "title": "Tuy, Batangas - 🌡" + str(weather.current_temperature) + "°C",
            "image_url": final_result,
            "subtitle": "☁️ Coudiness: " + weather.weather_description.title() + "\n🌫 Humidity: " + str(weather.current_humidity) + "%" + " | " + "Feel: " + str(weather.feeling) + "°C" + "\n💨 Wind: " + str(weather.po) + " km/h"
        },
        {
            "title": "Tokyo, Japan - 🌡" + str(weather.nas_current_temperature) + "°C",
            "image_url": another_image,
            "subtitle": "☁️ Coudiness: " + weather.nas_weather_description.title() + "\n🌫 Humidity: " + str(weather.nas_current_humidity) + "%" + " | " + "Feel: " + str(weather.nas_feel) + "°C" + "\n💨 Wind: " + str(weather.nas_po) + " km/h"
        },
        {
            "title": "Balayan, Batangas - 🌡" + str(weather.bal_current_temperature) + "°C",
            "image_url": weather.weather_image("bal"),
            "subtitle": "☁️ Coudiness: {}\n🌫 Humidity: {}% | Feel: {}°C\n💨 Wind: {} km/h".format(weather.bal_weather_description.title(), weather.bal_current_humidity, weather.bal_feeling, weather.bal_po)
        },
        {
            "title": "Calatagan, Batangas - 🌡" + str(weather.cal_current_temperature) + "°C",
            "image_url": weather.weather_image("cal"),
            "subtitle": "☁️ Coudiness: {}\n🌫 Humidity: {}% | Feel: {}°C\n💨 Wind: {} km/h".format(weather.cal_weather_description.title(), weather.cal_current_humidity, weather.cal_feeling, weather.cal_po)
        },
        {
            "title": "Lian, Batangas - 🌡" + str(weather.lian_current_temperature) + "°C",
            "image_url": weather.weather_image("lian"),
            "subtitle": "☁️ Coudiness: {}\n🌫 Humidity: {}% | Feel: {}°C\n💨 Wind: {} km/h".format(weather.lian_weather_description.title(), weather.lian_current_humidity, weather.lian_feeling, weather.lian_po)
        }
    ]
    bot.send_generic_message(recipient_id, elements)


def send_generic(recipient_id):
    elements = [
        {
            "title": "Hello master,",
            "image_url": "https://i.pinimg.com/474x/4c/b3/2b/4cb32b3ae14a1a9115e54bd573e9bee2.jpg",
            "subtitle": "I am your personal assistant bot. Keep coding master."
        }
    ]
    bot.send_generic_message(recipient_id, elements)


def raw_your_boat(recipient_id, text, replies):
    the_payload = {
        "recipient":{
            "id":recipient_id
        },
        "messaging_type": "RESPONSE",
        "message":{
            "text": text,
            "quick_replies": replies
        }
    }
    return the_payload





def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, threaded=True)
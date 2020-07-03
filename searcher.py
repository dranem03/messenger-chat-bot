import requests, json
import sys

base_url = "https://api.duckduckgo.com/?q="


if len(sys.argv)<2:
    print("please add some arguments")
    sys.exit()

search_keyword = sys.argv[2]
image_search = sys.argv[2]
if sys.argv[1] == "text":
    def get_text(search_text):
        global search_result
        complete_url = base_url + search_text + "&format=json&pretty=1"
        response = requests.get(complete_url)
        data = response.json()
        if data["AbstractText"] == "":
            error_message = "Sorry, I don't have any data of what you are looking . . ."
            search_result = error_message
        else:
            search_result = data["AbstractText"]
        return search_result
    print(get_text(search_keyword))
    
elif sys.argv[1] == "image":
    def get_image(search_image):
        complete_url = base_url + search_image + "&format=json&pretty=1"
        response = requests.get(complete_url)
        data = response.json()
        if data["Image"] == "":
            images = ""
        else:
            images = data["Image"]
        return images
    print(get_image(image_search))
#print(get_text("what is flower"))

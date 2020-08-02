import requests
import json
import os

API = "https://noembed.com/embed?url="
def GetInfo(video):
    try:
        video_api = API + video
        response = requests.get(video_api)
        response_json = json.loads(response.text)
        Channel = response_json['author_name']
        Title_video = response_json['title']
        Provider_name = response_json['provider_name']
        Thumbnail = response_json['thumbnail_url']
        print("----------------------------------------")
        print("Información del Video de " + Provider_name)
        print("----------------------------------------")
        print('Nombre del canal: ' + Channel)
        print('Titulo del vídeo: '+ Title_video)
        print('Proveedor: ' + Provider_name)
        print('Miniatura: ' + Thumbnail)
        print("----------------------------------------")
        print("Create by: Daniel Sarmiento Dev")
        print("----------------------------------------")
    except ValueError:
        print("Url invalida")

if __name__ == "__main__":
    try:
        
        os.system ("clear") 
        print("----------------------------------------")
        print("Display video information of Youtube,Vimeo y dailymotion")
        print("Create by: Daniel Sarmiento Dev")
        print("Video Example: https://www.youtube.com/watch?v=9KM_6EeUu_4&feature=youtu.be")
        print("----------------------------------------")
        video = input("Escribe La Url Del Video: ")
        os.system ("clear") 
        GetInfo(video)
    except ValueError: 
        print("Url invalida" + ValueError)

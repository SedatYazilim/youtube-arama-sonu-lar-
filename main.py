import os
import subprocess
import sys

required_packages = ["requests", "colorama"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import requests
from colorama import Fore, Style

API_KEY = "b4f453a8damsh90a1e6986804d79p14bad3jsn00666b588c8d"
API_HOST = "youtube-v31.p.rapidapi.com"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

url = f"https://{API_HOST}/search"

print("python ile vereceğiniz başlığa sahip videoları bulabilirsiniz *-*\n -github")
araveriyib = input(Fore.YELLOW + "Aranacak veriyi girin: " + Style.RESET_ALL)

params = {
    "q": araveriyib,
    "part": "snippet,id",
    "regionCode": "US",
    "maxResults": 50,
    "order": "date"
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    print(Fore.GREEN + "\nArama Sonuçları:" + Style.RESET_ALL)
    for item in data.get("items", []):
        video_title = item.get("snippet", {}).get("title", "Başlık bulunamadı")
        channel_title = item.get("snippet", {}).get("channelTitle", "Kanal adı bulunamadı")
        print(Fore.CYAN + f"- Video Başlığı: {Fore.YELLOW}{video_title}{Style.RESET_ALL}")
        print(Fore.CYAN + f"  Kanal: {Fore.YELLOW}{channel_title}{Style.RESET_ALL}\n")

except requests.exceptions.RequestException as e:
    print(Fore.RED + "hata oluştu lütfen bekleyin :(" + Style.RESET_ALL, e)
    import requests

bot_token = '7539626142:AAFxIIT89Wzrjh-9chJ9a2RAyF12MjgCOTM'  
chat_id = '6376628506'  
message = 'hata var lütfen kontrol eder misin admin 🥲'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

response = requests.post(url, data={
    'chat_id': chat_id,
    'text': message
})

print(response.json()) 
print(Fore.CYAN + "hata yapımcıma gönderildi lütfen düzelmesini bekleyin" + Style.RESET_ALL,)



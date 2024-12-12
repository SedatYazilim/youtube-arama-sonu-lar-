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
#apiyi rapidapi ile siz de kullanabilirsiniz 
API_KEY = "b4f453a8damsh90a1e6986804d79p14bad3jsn00666b588c8d"
API_HOST = "youtube-v31.p.rapidapi.com"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

url = f"https://{API_HOST}/search"

print("python ile vereceğiniz başlığa sahip videoları bulabilirsiniz *-*\n -github:https://github.com/SedatYazilim/")
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
    print(Fore.RED + "programı dilediğiniz gibi geliştirebilirsiniz" + Style.RESET_ALL, e)
    

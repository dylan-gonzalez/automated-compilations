from bs4 import BeautifulSoup
import requests
import urllib3 as urllib




headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

URL = "https://t.tiktok.com/"
page = requests.get(URL, headers=headers)

# print(page)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())
videos = soup.find_all("video")
body = soup.find("body")
print(body.prettify())
# print(soup.prettify())
div = soup.find("div")
# print(div)
print(videos)


# r1 = requests.get("https://www.tiktok.com/", headers=headers)
# print(BeautifulSoup(r1.content, 'html.parser'))

http = urllib.PoolManager()
page2 = http.request("GET", "https://www.tiktok.com/", headers)
soup = BeautifulSoup(page2.read())
print(soup.prettify())


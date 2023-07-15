import json
from urllib.request import urlopen
import urllib.request
import urllib
import time


class Product:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"{self.title}"


url = "https://dummyjson.com/products"

response = urlopen(url)

data_json = json.loads(response.read())

# productArray = list()
angle = 0
for product in data_json["products"]:
    index = len(product["images"]) - 1
    while index >= 0:
        image = product["images"][index]
        title = Product(product["title"]).__str__()
        urllib.request.urlretrieve(
            image, f"C:\\code-stuff\\{title}v{angle}.jpg"
        )

        index = index - 1
        angle = angle + 1
        time.sleep(10)
    angle = 0


# download all the images and a folder of all the images and python script to downlaod it all=

# for toUser in productArray:
#   print(toUser)


# productArray = data_json["products"][0]['id']
# print(data_json["products"][0]['id'])

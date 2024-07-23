import requests
path = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
file = requests.get(path).json()
print(file[0]["Rate"])
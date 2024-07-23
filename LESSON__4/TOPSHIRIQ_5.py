import requests
class Convertor:
    def __init__(self,path = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"):
        self.path = path

    def uzs_to_usd(self,uzs):
        dollar = float(requests.get(self.path).json()[0]["Rate"])

        if type(uzs) == int or type(uzs) == float:
            return uzs / dollar
        else: raise ValueError

    def usd_to_uzs(self,usd):
        dollar = float(requests.get(self.path).json()[0]["Rate"])

        if type(usd) == int or type(usd)==float:
            #somni taxmin oldim
            return usd * 1000
s = Convertor()
print(s.usd_to_uzs(12))
print(s.uzs_to_usd(15000))

# add , delete , replace , clear
from typing import Any
class Mydict:
    def __init__(self):
        self.my_dict={}
    def add(self,key:Any,value:Any):
        self.my_dict[key]=value

    def delete(self,key):
        if key in self.my_dict.keys():
            del self.my_dict[key]
        else:raise ValueError("lits ichida bor malumotni ochiring aka!")
    def replace(self,key1,key2:Any,value2:Any):
        if key1 in self.my_dict:
            self.my_dict[key1] = self.my_dict[key2]=value2
        else:raise ValueError("XATO !")
    def clear(self):
        self.my_dict.clear()

men = Mydict()
men.add("ism","Abdujabbor")
men.add("familya","Tursunov")
men.delete("ism")
men.replace("familya","ism","oti")
men.clear()


print(men.my_dict)
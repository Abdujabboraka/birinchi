from typing import Any
#add , delete , replace , clear
class  Mylist:
    def __init__(self):
        self.mylist = []
    def add(self, *index:Any):
        """bu metod list ichiga ma'lumot  qo'shadi!"""
        self.mylist.append(index)
        self.mylist = list(self.mylist[0])

    def delete(self,index:Any):
        """bu metod ko'rsatilgan elementni ochiradi!
        agar element mavjud bo'lmasa xato qaytaradi"""

        if index in self.mylist:
            self.mylist.remove(index)
        else:
            raise FileNotFoundError("object not found")
    def replace(self,index,index2:Any):
        """bu metod ko'rsailgan elementni ko'rsatilgan elementga almashtiradi!"""
        if index in self.mylist:
             self.mylist[self.mylist.index(index)] = index2

        else: raise FileNotFoundError("berligan malumot toplimadi!")
    def clear(self):
        """bu metod listni tozalaydi!"""
        self.mylist.clear()

royhat = Mylist()
royhat.add("olma","behi",4,True,False, None,4.5)
royhat.delete(4)
royhat.replace("olma","Anor")
royhat.clear()
print(royhat.mylist)



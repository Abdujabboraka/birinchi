class Convertor:
    def __init__(self):
        pass
    def sm_to_metr(self,sm):
        return sm / 100
    def km_to_metr(self,km):
        return  km *1000
met = Convertor()
print(met.km_to_metr(15))
print(met.sm_to_metr(1263000))


#temperature conversion program
class Degrees:
    def __init__(self, temperature):
        self.temperature=temperature
    def celciustofah(self):
        fahreinheit=9/5*self.temperature+32
        return fahreinheit
    def fahtocelcius(self):
        celcius=5/9*self.temperature-32
        return celcius
degrees=Degrees(40)
print("temperature in fahreinheit =", degrees.celciustofah())
print("temperature in celcius =", degrees.fahtocelcius())


from highway import Highway

class HighwayQueue:
    def __init__(self):
        self.HWhead = None
        self.HWtail = None
        
    def isEmpty(self):
        return self.HWhead == None
    
    def push(self, name):
        newHighway = Highway(name)
        
        if self.isEmpty():
            self.HWhead = newHighway
            self.HWtail = newHighway
        else:
            newHighway.nextCity = self.HWhead
            self.HWhead = newHighway
            
    def print(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            temp = self.HWhead
            while temp:
                print(f"{temp.name} ")
                temp.printCities()
                print()
                temp = temp.nextCity
            
    def pop(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            penult = self.HWhead
            last = self.HWhead
            while last.nextCity:
                penult = last
                last = last.nextCity
            penult.nextCity = None
            self.HWtail = penult
    
    #Procura uma rodovia na lista
    def searchHighway(self, highway):
        if self.isEmpty():
            print("Empty List")
        else:
            temp = self.HWhead
            while temp:
                if temp.name == highway:
                    return temp
                temp = temp.nextCity
            return None
        
    def searchCity(self, cityName):
        highways = []

        temp = self.HWhead

        while temp:
            if temp.cityExists(cityName):
                highways.append(temp.name)
            
            temp = temp.nextCity

        return highways
            

    def highwayCrossing(self, highway1, highway2):
        cities = []
        highway1 = self.searchHighway(highway1)
        highway2 = self.searchHighway(highway2)


        if not highway1 or not highway2:
            return None, None
        
        citiesHW1 = highway1.listCitys()
        citiesHW2 = highway2.listCitys()

        for i in citiesHW1:
            if i in citiesHW2:
                cities.append(i)

        
        return cities
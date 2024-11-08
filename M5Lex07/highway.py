from city import City

class Highway:
    def __init__(self, name):
        self.name = name
        self.nextCity = None
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def printCities(self):
        if self.isEmpty():
            print("Empty list")

        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        
    def append(self, cityName):
        newCity = City(cityName)

        if self.head is None:
            self.head = self.tail = newCity
        else:
            temp = self.head
            ant = None
            
            while temp and temp.data < cityName:
                ant = temp
                temp = temp.next
            
            if ant is None:
                newCity.next = self.head
                self.head.prev = newCity
                self.head = newCity
            elif temp is None:
                self.tail.next = newCity
                newCity.prev = self.tail
                self.tail = newCity
            else:
                ant.next = newCity
                newCity.prev = ant
                newCity.next = temp
                temp.prev = newCity

    # Verifica se a cidade dada existe na lista
    def cityExists(self, cityName):
        temp = self.head

        while temp:
            if temp.data == cityName:
                return True
            temp = temp.next

        return False
    
        
    def listCitys(self):
        cities = []
        temp = self.head

        while temp:
            cities.append(temp.data)
            temp = temp.next

        return cities
    
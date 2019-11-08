class Home:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.remain = 0
    
    def bring(self, **kwargs):
        self.remain = self.area - sum(kwargs.values())
        print (f"type of home: {self.name}")
        print (f"total area: {self.area}")
        print (f"remaining area: {self.area}")
        print ("ferniture names: ", ', '.join(kwargs.keys()))
        
mda = Home("болоберет", 97.5)
mda.bring(bad=4, table=1.5, wardrobe=2)

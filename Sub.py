from Sub import * 

class Sub:
    def __init__(self, name, attribute_points):
        self.name = name
        self.attribute_points = attribute_points
    
    def details(self):
        print(f"DETAILS of [{self.name}]")
        print(f"[NAME]: {self.name}")
        print(f"[ATTRIBUTE POINTS]: {self.attribute_points}\n----------")
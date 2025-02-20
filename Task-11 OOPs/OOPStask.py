class car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.speed = 0
    def accelerate(self,speedup):
        self.speed += speedup
        print(f"The acceleration of the {self.make}{self.model} is {self.speed}")
    def brake(self,speedown):
        self.speed -= speedown
        print(f"The brake of the {self.make}{self.model} is {self.speed}")
    def display(self):
        print(f"The current Speed is {self.speed}")
    
s = car("Ford","Mustang")
s.accelerate(90)
s.brake(30)
s.display()

class TemperatureConverter:
    @staticmethod
    def CtoF(C):
        return (C * 9/5) + 32
    @staticmethod
    def FtoC(F): 
        return (F - 32) * 5/9

a = TemperatureConverter()
print(a.CtoF(60))
print(a.FtoC(222))

class students:
    def __init__(self, name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = {}
    
    def add(self, subject,score):
        self.scores[subject] = score

    def average(self):
        avg =   sum(self.scores.values())/ len(self.scores)
        print("The Average is :",avg)
    
    def highest(self):
        sub = ""
        high = 0
        for i , j in self.scores.items():
            if j > high:
                high = j
                sub = i
        print(f"The highest mark is {high} in {sub}")

    def info(self):
        print(f"Name: {self.name} , Roll No: {self.roll_no}, scores: {self.scores}")

std = students("Nandan Sr", "BTRSE17")
std.add("Physics", 86)
std.add("chemistry", 90)
std.add("Maths", 60)
std.average()
std.highest()
std.info()


        
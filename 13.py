class Avenger:
    def _init_(self, name, age, gender, super_power, weapon, leader=False):
        self.name =name
        self.age =age
        self.gender =gender
        self.super_power =super_power
        self.weapon =weapon
        self.leader =leader

    def get_info(name,age,gender,super_power,weapon,leader):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"
    def is_leader(self):
        return self.leader
    
super_heroes =[
    Avenger("Captain America", 35, "Male", "Super Strength", "Shield", leader=True),
    Avenger("Iron Man", 40, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 30, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 40, "Male", "Super Energy", "Mjolnir"),
    Avenger("Hawkeye", 35, "Male", "Fighting Skills", "Bow and Arrows")
]
for hero in super_heroes:
    print(hero.get_info())
    print("Leader:", hero.is_leader())

//The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.
Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.
For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

p1=Grass_Pokemon("Belle")
p2=Pokemon("Belle")
print(p1.action())
print(p2)

Output:
Belle knows a lot of different moves!
Pokemon name: Belle, Type: Normal, Level: 5

Result	Actual Value	Expected Value	Notes
Pass	'Belle...oves!'	'Belle...oves!'	Testing that action method is correct and p1 assigned to correct value
You passed: 100.0% of the tests
    
    
    
    
//Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.
Grass is weak against Fire and strong against Water
Ghost is weak against Dark and strong against Psychic
Fire is weak against Water and strong against Grass
Flying is weak against Electric and strong against Fighting
For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')

class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)
    
    def opponent(self):
        self.update()
        if self.p_type == "Grass" :
            weak = "Fire"
            strong="Water"
        return (weak,strong)
    
        if self.p_type == "Ghost":
            weak = "Dark"
            strong="Psychic"
        return (weak,strong)

        if self.p_type == "Fire":
            weak = "Water"
            strong="Grass"
        return (weak,strong)

        if self.p_type == "Flying" :
            weak = "Electric"
            strong = "Fighting"
        return (weak,strong)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12
        
           

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3
        
    def opponent(self):
        self.update()
        if self.p_type == "Ghost":
            weak = "Dark"
            strong="Psychic"
        return (weak,strong)

class Fire_Pokemon(Pokemon):
    p_type = "Fire"
    
    def opponent(self):
        self.update()
        if self.p_type == "Fire":
            weak = "Water"
            strong="Grass"
        return (weak,strong)
    
class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    def opponent(self):
        self.update()
        if self.p_type == "Flying" :
            weak = "Electric"
            strong = "Fighting"
        return (weak,strong)

Result	Actual Value	Expected Value	Notes
Pass	"('Fir...ter')"	"('Fir...ter')"	Testing that Grass weak and strong are assigned to correct values.
Pass	"('Wat...ass')"	"('Wat...ass')"	Testing that Fire weak and strong are assigned to correct values.
Pass	"('Dar...hic')"	"('Dar...hic')"	Testing that Ghost weak and strong are assigned to correct values.
Pass	"('Ele...ing')"	"('Ele...ing')"	Testing that Flying weak and strong are assigned to correct values.
You passed: 100.0% of the tests  
      


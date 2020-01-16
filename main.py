import random

class Creature:
    

class Monster(Creature):
    pass

class Hero(Creature):
    pass

class OrkNameGenerator:
    klinkers = ['a','e','i','o','u']
    medeklinkers = ['g','b','z','k']
 
    def get_random_ork_name():
        return random.choice(OrkNameGenerator.medeklinkers) + \
        random.choice(OrkNameGenerator.klinkers) + \
        random.choice(OrkNameGenerator.medeklinkers)
    for _ in range(10):
        print(OrkNameGenerator.get_random_ork_name())


class Room(Creature):

    def __init__(self, name, aantal_monsters=3, description= ''):
        self.name = name
        self.aantal_monsters = aantal_monsters
        self.description = description
        self.monsters = []
        for i in range (aantal_monsters):
            #self.monsters.append(Monsters(OrkNameGenerator....))
        self.attached_rooms = []

    def attach(self):
        pass

    def _is_attached(self):
        pass

    def enter(self, hero:Hero):
        pass

    def _print_room_menu(self):
        pass

    def _print_monsters(self):
        pass

    def _print_attached_rooms(self):
        pass

if __name__ :: "__main__":
    hero = Hero("ImmaHero", 200, 20)

    hall = Room("hall", description="A very narrow hallway...")
    kitchen = Room("kitchen", 15, "It smells like something died in here...")
    office = Room("office", 10, "So much work to do... and monsters to kill...")
    garden = Room("frontgarden", 5, "...")
    backgarden = Room("backgarden", 5, "...")
    pool = Room("pool", 100, "This pool is infested with monsters!")

frontgarden.attach_room(hall)
hall.attach_room(kitchen)
hall.attach_room(office)
hall.attach_room(backgarden)
backgarden.attach_room(pool)
frontgarden.Enter(hero)
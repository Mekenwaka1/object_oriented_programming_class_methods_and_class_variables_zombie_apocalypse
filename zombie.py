import random

class Zombie:

    max_speed = 5
    horde = []
    plague_level = 10
    default_speed = 1
    max_strength = 8
    default_strength = 3

    def __init__(self, speed, strength):
        """Initializes zombie's speed and strength
        """
        if speed > Zombie.max_speed:
            self.speed = Zombie.default_speed
        else:
            self.speed = speed
        
        if strength > Zombie.max_strength:
            self.strength = Zombie.default_strength
        else:
            self.strength = strength
        

    def __str__(self):
        return "Speed: {} -- Strength {}".format(self.speed, self.strength)

    @classmethod
    def spawn(cls):
        """Spawns a random number of new zombies, based on the plague level,
        adding each one to the horde.  Each zombie gets a random speed.
        """
        new_zombies = random.randint(1, Zombie.plague_level)
        count = 0

        while count < new_zombies:
            speed = random.randint(1, Zombie.max_speed)
            Zombie.horde.append(Zombie(speed, 0))
            count += 1

    @classmethod
    def new_day(cls):
        """Represents the events of yet another day of the zombie apocalypse.
        Every day some zombies die off (phew!), some new ones show up,
        and sometimes the zombie plague level increases.
        """
        Zombie.spawn()
        Zombie.some_die_off()
        Zombie.increase_plague_level()

    @classmethod
    def some_die_off(cls):
        """Removes a random number (between 0 and 10) of zombies from the horde.
        """
        how_many_die = random.randint(0, 10)
        counter = 0
        while counter < how_many_die and len(Zombie.horde) > 0:
            random_zombie = random.randint(0,len(Zombie.horde) - 1)
            Zombie.horde.pop(random_zombie)
            counter += 1

    def encounter(self):
        """This instance method represents you coming across a zombie! This can end in three possible outcomes:
        1. You outrun the zombie and escape unscathed!
        2. You don't outrun the zombie. It eats your brains and you die. :(
        Returns a summary of what happened.
        3. You fight the zombie off and either win or lose the fight.
        3.1 If you lose the fight, you die.
        3.2 If you win the fight, you survive, but you catch the zombie plague.
        """
        outrun = self.chase()
        fight = self.fight()

        if outrun:
            return 'You escaped!'
        elif fight == False:   
            return 'You died.'
        elif fight == True:
            new_zombie = Zombie(self.speed, self.strength)
            Zombie.horde.append(new_zombie)
            return "You are now a zombie. Raawwwrghh"  

    def chase(self):
        """Represents you trying to outrun this particular zombie.
        Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
        """
        your_speed = random.randint(1, Zombie.max_speed)
        return your_speed > self.speed
    
    def fight(self):
        """Represents you trying to fight a zombie.
        Uses `Zombie.max_strength` to generate a random number that represents how well you are able to fight off the zombie.
        """
        your_strength = random.randint(1, Zombie.max_strength)
        if your_strength > self.strength:
            return True
        else: 
            return False
    
    @classmethod
    def increase_plague_level(cls):
        """Represents an increase in the zombie plague level.
        """
        Zombie.plague_level += random.randint(0, 2)

print(Zombie.horde) 
Zombie.new_day()
print(Zombie.horde) 
zombie1 = Zombie.horde[0]
print(zombie1) 
zombie2 = Zombie.horde[1]
print(zombie2) 
print(zombie1.encounter())
print(zombie2.encounter())
Zombie.new_day()
print(Zombie.horde)
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter())
print(zombie2.encounter())
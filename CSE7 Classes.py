#Inheritance: for Dummies
#30 Classes
#Every class must have its own method
#Every class must have a constructor
moves = 0
global(score) = 0
class Character(object):
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
    def attack(self, target):
        print "The %s attacks %s for %d damage." %(self.name, target.name, self.damage)
        target.take_damage(self.damage)
        if target.hp <= 0:
            score += 100
    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health <= 0:
                print "%s is already dead." % self.name
            else:
                print "%s has taken damage." % self.name
        
class Player(Character):
    def __init__(self, name, hp, attack, defense, current_armor, current_weapon):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.current_weapon = current_weapon
        self.current_armor = current_armor
    def kill_self(self):
        print "Suicide is never the answer.."
    def drop_item(self, Item):  
        print "You drop %s" % Item
    def inspect(self, Item):
        print Item.description
    def attack(self, target):
        print "You throw your hands at %s for %d damage." %(target.name, self.damage)
        target.take_damage(self.damage)
        print "%s now has %s health." % (target.name, target.health)
    def take_damage(self, damage, defense):
        if self.health > 0:
            if self.defense > 0:
                damage -= defense
            self.health -= damage
            if self.health <= 0:
                print "%s is questioning life and will no longer catch your hands." % self.name
            else:
                print "%s has caught some hands." % self.name
        
class Enemy(Character):
    def __init__(self, name, hp, armor, description):
        super(Enemy, self).__init__(name, hp, armor, description)
        
class Item(object):
    def __init__(self, name, description):
       self.name = name
       self.description = description
    def inspect(self, item):
        print self.description
       
class Weapon(Item):
    def __init__(self, name, damage, description):
        super(Weapon, self).__init__(name, damage, description)
        self.damage = damage
    def equip(self, Weapon):
        print "You have now have %s equipped." % Weapon
        
class Sword(Weapon):
    def __init__(self, name, damage, description):
        super(Sword, self).__init__(name, damage, description)
            
class Armor(Item):
    def __init__(self, defense):
        super(Armor, self).__init__(self.name, self.description)
        self.defense = defense
    def block(self):
        print "You prepare to take a hit."
    def equip(self, Armor):
        player.armor += self.defense

class Consumable(Item):
    def __init__(self, name, hp, description):
        super(Consumable, self).__init__(name, hp, description)
        
class Potion(Consumable):
    def __init__(self, name, hp, description):
       super(Potion, self).__init__(name, hp, description) 
    def eat(self, Food):
        player.hp += self.food
        print "You eat the %s and gain %s. You now have %s health." %(self.name, self.hp, player.hp)
        
class Food(Consumable):
    def __init__(self, name, hp, description):
        super(Food, self).__init_(name, hp, description)
    def eat(self, Food):
        player.hp += self.food
        print "You eat the %s and gain %s. You now have %s health." %(self.name, self.hp, player.hp)
        
player = Player("Walter", 500, 0, )